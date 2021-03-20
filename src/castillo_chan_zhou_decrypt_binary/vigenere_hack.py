"""Hacks for the Vigénere Cipher."""

import itertools
import time
from difflib import SequenceMatcher
from typing import Any, Dict, List, Optional, Tuple

from castillo_chan_zhou_decrypt_binary.constants import (
    MAX_KEY_LENGTH,
    MESSAGE_SPACE,
    NUM_MOST_FREQ_LETTERS,
    PLAINTEXT_DICTIONARY_ONE,
    PLAINTEXT_DICTIONARY_TWO,
)
from castillo_chan_zhou_decrypt_binary.detect_english import is_english
from castillo_chan_zhou_decrypt_binary.frequency_analysis import frequency_match_score
from castillo_chan_zhou_decrypt_binary.vigenere import decrypt


def get_item_at_index_one(items: Any) -> Any:
    """Return the item at the specified index from the iterable.

    Used to sort lists.

    Args:
        items (Any): Iterable of items to parse.

    Returns:
        Any: the item at index one from the iterable
    """
    return items[1]


def find_repeated_ciphertext_sequences(text: str) -> Dict[str, List[int]]:
    """Find repeated sequences of characters in the provided ciphertext.

    Args:
        text (str): The ciphertext

    Returns:
        dict(str, list(int)): A dictionary with the sequence and a list of the
                              distances between each occurrence of the sequence.
    """
    sequence_spacings: Dict[str, List[int]] = {}

    # Look for sequences of length 3, 6 characters that are repeated
    # This is generally a good amount of characters to find potentially repeated
    # sequences in the plaintext that were encrypted by the same ciphertext
    # characters.
    for sequence_length in range(3, 6):
        for sequence_start_ndx in range(len(text) - sequence_length):
            sequence_end_ndx = sequence_start_ndx + sequence_length
            sequence = text[sequence_start_ndx:sequence_end_ndx]

            for current_character_ndx in range(
                sequence_start_ndx + sequence_length, len(text) - sequence_length
            ):

                next_sequence_ndx = current_character_ndx + sequence_length
                # When a second sequence matching the current sequence is found
                # store the distance between the beginning of the current sequence
                # and the beginning of the next occurrence in the dictionary.
                if text[current_character_ndx:next_sequence_ndx] == sequence:
                    if sequence not in sequence_spacings:
                        sequence_spacings[sequence] = []

                    current_sequence_ndx_difference = current_character_ndx - sequence_start_ndx

                    sequence_spacings[sequence].append(current_sequence_ndx_difference)
    return sequence_spacings


def get_useful_factors(num: int, max_key_length: int = MAX_KEY_LENGTH) -> List[int]:
    """Return a list of useful factors of num.

    Useful is defined as 1 < x < max_key_length + 1.

    For example:
        num = 144
        returns [2,3,4,6,8,9,12,16]

    Args:
        num (int): Number to find the useful factors of.
        max_key_length (int): Maximum length of the key for the cipher. Defaults to MAX_KEY_LENGTH.

    Returns:
        List[int]: List of useful factors
    """
    if num < 2:
        # Numbers less than 2 are essentially a Caesar Cipher and do not have useful factors.
        return []

    factors = []

    # Find factors up to the maximum key length possible
    # See note above to explain why 1 should not be tested.
    for i in range(2, max_key_length + 1):
        if num % i == 0:
            factors.append(i)
            factor_pair = int(num / i)  # This is the pair of i that is used to get num
            if factor_pair < max_key_length + 1 and factor_pair != 1:
                factors.append(factor_pair)

    useful_factors = list(set(factors))  # Remove duplicate factors

    return useful_factors


def get_common_factors(
    sequence_factors: Dict[str, List[int]], max_key_length: int = MAX_KEY_LENGTH
) -> List[Tuple[int, int]]:
    """Return a sorted list of the most common factors (which provides the most likely key length).

    Args:
        sequence_factors (Dict[str, List[int]]): A dictionary containing repeated sequences in the
                                                 ciphertext and the most common factors of
                                                 the distances between the sequences.
        max_key_length (int): Maximum length of the key for the cipher. Defaults to MAX_KEY_LENGTH.

    Returns:
        List[Tuple[int, int]]: A list of the most common sequences spacings factors and
                               the number of times occur.
    """
    # Key: Factor
    # Value: Number of occurrences of the factor
    factor_counts = {}

    for sequence in sequence_factors:
        factor_list = sequence_factors[sequence]
        for factor in factor_list:
            if factor not in factor_counts:
                factor_counts[factor] = 0
            factor_counts[factor] += 1

    # Create list of tuples of factors and frequency of occurrence
    factors_by_frequency = []
    for factor in factor_counts:
        if factor <= max_key_length:
            factors_by_frequency.append((factor, factor_counts[factor]))

    # Sort list of tuples by the frequency of occurence
    factors_by_frequency.sort(key=get_item_at_index_one, reverse=True)

    return factors_by_frequency


def kasiski_examination(ciphertext: str) -> List[int]:
    """Perform Kasiski examination on the ciphertext to determine likely key lengths.

    Args:
        ciphertext (str): The ciphertext to analyze.

    Returns:
        List[int]: List of likely key lengths
    """
    # Step 1: Find the sequences of 3 to 6 letters that occur multiple times in the ciphertext.
    repeated_sequence_spacings = find_repeated_ciphertext_sequences(ciphertext)

    # Step 2: Get the useful factors of the spacings for each sequence
    sequence_factors = {}
    for sequence in repeated_sequence_spacings:
        sequence_factors[sequence] = []
        for spacing in repeated_sequence_spacings[sequence]:
            sequence_factors[sequence].extend(get_useful_factors(spacing))

    # Step 3: Get most common factors from sequence_factors
    factors_by_frequency = get_common_factors(sequence_factors)

    # Step 4: Determine likely key lengths
    all_likely_key_lengths = []
    for pairs in factors_by_frequency:
        all_likely_key_lengths.append(pairs[0])

    return all_likely_key_lengths


def get_nth_subkey_letters(nth: int, key_length: int, message: str) -> str:
    """Return every nth letter in the message for each set of key_length letters in the message.

    Args:
        nth (int): Index to return for every key_length set of letters.
        key_length (int): Length of the key.
        message (str): The message

    Returns:
        str: The string of the nth letters
    """
    # Remove non-valid characters from the message
    # message = VALID_CHARACTERS_PATTERN.sub("", message)

    i = nth - 1
    letters = []
    while i < len(message):
        letters.append(message[i])
        i += key_length

    return "".join(letters)


def key_length_hack_test_one(text: str, key_length: int) -> Optional[str]:
    """Attempt to brute force the key based on key length and frequency analysis.

    Args:
        text (str): The ciphertext
        key_length (int): The expected length of the key.

    Returns:
        Optional(str): The decrypted text.
    """
    # Create list to store nested list of frequency scores
    all_frequency_scores = []
    for i in range(1, key_length + 1):
        nth_letter = get_nth_subkey_letters(i, key_length, text)

        frequency_scores = []
        for key in MESSAGE_SPACE:
            decrypted_text = decrypt(nth_letter, key)
            # Create key_score_tuple to store key and match score
            key_score_tuple = (key, frequency_match_score(decrypted_text, "test_one"))
            frequency_scores.append(key_score_tuple)
        # Sort by score
        frequency_scores.sort(key=get_item_at_index_one, reverse=True)

        all_frequency_scores.append(frequency_scores[:NUM_MOST_FREQ_LETTERS])

    key_length = min(key_length, 4)
    for indexes in itertools.product(range(NUM_MOST_FREQ_LETTERS), repeat=key_length):
        # Create attempt key from letters in all_frequency_scores
        key = ""
        for i in range(key_length):
            key += all_frequency_scores[i][indexes[i]][0]

        decrypted_text = decrypt(text[:key_length], key)

        for word in PLAINTEXT_DICTIONARY_ONE:
            if SequenceMatcher(None, word[:key_length], decrypted_text).ratio() > 0.7:
                return word

    return None


def get_possible_keys_for_first_word_test_two(text: str) -> Dict[str, str]:
    """Attempt to decrypt the first word of the ciphertext and generate possible keys.

    Args:
        text (str): Ciphertext to decrypt

    Returns:
        Dict[str, str]: Dictionary of possible first words and keys
    """
    first_word_key_dict = {}
    for word in PLAINTEXT_DICTIONARY_TWO:
        first_word_key_dict[word] = decrypt(text[: len(word)], word)
    return first_word_key_dict


def key_length_hack_test_two(text: str, key: str, key_length: int) -> Optional[str]:
    """Attempt to brute force the key based on key length and frequency analysis.

    Args:
        text (str): The ciphertext
        key (str): The possible key
        key_length (int): The expected length of the key.

    Returns:
        Optional(str): The decrypted text.
    """
    plaintext = []
    ctr = 0
    ciphertext_length = len(text)

    while ctr < ciphertext_length:
        decrypted_text = decrypt(text[ctr : ctr + key_length], key)
        words = decrypted_text.split(" ")
        for decrypted_word in words:
            for word in PLAINTEXT_DICTIONARY_TWO:
                word_match_score = SequenceMatcher(
                    None, decrypted_word.upper(), word.upper()
                ).ratio()
                if word_match_score > 0.7:
                    plaintext.append(word)
                    break
        ctr += 1
    return plaintext


def key_length_hack_test_two_kasiski(text: str, key_length: int) -> Optional[str]:
    """Attempt to brute force the key based on key length and frequency analysis.

    Args:
        text (str): The ciphertext
        key_length (int): The expected length of the key.

    Returns:
        Optional(str): The decrypted text.
    """
    # Create list to store nested list of frequency scores
    all_frequency_scores = []
    for i in range(1, key_length + 1):
        nth_letter = get_nth_subkey_letters(i, key_length, text)

        frequency_scores = []
        for key in MESSAGE_SPACE:
            decrypted_text = decrypt(nth_letter, key)
            # Create key_score_tuple to store key and match score
            key_score_tuple = (key, frequency_match_score(decrypted_text, "test_two"))
            frequency_scores.append(key_score_tuple)
        # Sort by score
        frequency_scores.sort(key=get_item_at_index_one, reverse=True)

        all_frequency_scores.append(frequency_scores[:NUM_MOST_FREQ_LETTERS])

    key_length = min(key_length, 4)
    for indexes in itertools.product(range(NUM_MOST_FREQ_LETTERS), repeat=key_length):
        # Create attempt key from letters in all_frequency_scores
        key = ""
        for i in range(key_length):
            key += all_frequency_scores[i][indexes[i]][0]

        decrypted_text = decrypt(text[:key_length], key)

        if is_english(decrypted_text):
            return decrypted_text

    return None


def hack_vigenere(text: str, test_id: str) -> Optional[str]:
    """Attempt to determine

    Args:
        text (str): The encrypted text we are trying to hack.
        test_id (str): Specify whether using test one (known plaintext) or test two (dictionary attack)

    Returns:
        Optional[str, None]: The decrypted plain text.
    """
    decrypted_text = None
    text = text.lower()

    if test_id == "test_one":
        all_likely_key_lengths = kasiski_examination(text)

        for key_length in all_likely_key_lengths:

            decrypted_text = key_length_hack_test_one(text, key_length)
            if decrypted_text is not None:
                return decrypted_text

    if test_id == "test_two":
        start = time.time()
        most_likely_plaintext_word_count = 0
        possible_keys = get_possible_keys_for_first_word_test_two(text)
        for key in possible_keys:
            plaintext_test = key_length_hack_test_two(
                text, possible_keys[key], len(possible_keys[key])
            )
            if len(plaintext_test) > most_likely_plaintext_word_count:
                most_likely_plaintext_word_count = len(plaintext_test)
                decrypted_text = " ".join(plaintext_test)
        guess_one = decrypted_text

        guess_two = None
        end = time.time()
        if end - start < 175:
            all_likely_key_lengths = kasiski_examination(text)
            for key_length in all_likely_key_lengths:
                decrypted_text = key_length_hack_test_two_kasiski(text, key_length)
                if decrypted_text is not None:
                    guess_two = decrypted_text

        if guess_two is not None and guess_one is not None:
            if len(guess_two.split(" ")) > len(guess_one.split(" ")):
                return guess_two
            else:
                return guess_one
        else:
            if guess_two is not None:
                return guess_two
            else:
                return guess_one

    if decrypted_text is None:
        for key_length in range(1, MAX_KEY_LENGTH + 1):
            if key_length not in all_likely_key_lengths:
                decrypted_text = key_length_hack_test_two_kasiski(text, key_length)
                if decrypted_text is not None:
                    return decrypted_text

    return decrypted_text
