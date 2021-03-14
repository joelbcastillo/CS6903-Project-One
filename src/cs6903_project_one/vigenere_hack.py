"""Hacks for the Vigénere Cipher."""

import itertools
from typing import Any, Dict, List, Optional, Tuple

from cs6903_project_one.constants import VALID_CHARACTERS_PATTERN
from cs6903_project_one.vigenere import decrypt
from cs6903_project_one.freqency_analysis import frequency_match_score


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
    valid_text = VALID_CHARACTERS_PATTERN.sub("", text)

    sequence_spacings: Dict[str, List[int]] = {}

    for sequence_length in range(3, 6):
        for sequence_start_ndx in range(len(valid_text) - sequence_length):
            sequence_end_ndx = sequence_start_ndx + sequence_length
            sequence = valid_text[sequence_start_ndx:sequence_end_ndx]

            for current_character_ndx in range(
                sequence_start_ndx + sequence_length, len(valid_text) - sequence_length
            ):

                next_sequence_ndx = current_character_ndx + sequence_length

                if valid_text[current_character_ndx:next_sequence_ndx] == sequence:
                    if sequence not in sequence_spacings:
                        sequence_spacings[sequence] = []

                    current_sequence_ndx_difference = current_character_ndx - sequence_start_ndx

                    sequence_spacings[sequence].append(current_sequence_ndx_difference)
    return sequence_spacings


def get_useful_factors(num: int, max_key_length: int = 16) -> List[int]:
    """Return a list of useful factors of num.

    Useful is defined as 1 < x < max_key_length + 1.

    For example:
        num = 144
        returns [2,3,4,6,8,9,12,16]

    Args:
        num (int): Number to find the useful factors of.
        max_key_length (int): Maximum length of the key for the cipher. Defaults to 16.

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
    sequence_factors: Dict[str, List[int]], max_key_length: int = 16
) -> List[Tuple[int, int]]:
    """Return a sorted list of the most common factors (which provides the most likely key length).

    Args:
        sequence_factors (Dict[str, List[int]]): A dictionary containing repeated sequences in the
                                                 ciphertext and the most common factors of
                                                 the distances between the sequences.
        max_key_length (int): Maximum length of the key for the cipher. Defaults to 16.

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
            factors_by_frequency.append(factor, factor_counts[factor])

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
    message = VALID_CHARACTERS_PATTERN.sub("", message)

    i = nth + 1
    letters = []
    while i < len(message):
        letters.append(message[i])
        i += key_length

    return "".join(letters)


def key_length_hack(text: str, key_length: int) -> Optional[str]:
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
        for key in LETTERS:
            decrypted_text = decrypt(key, nth_letter)
            # Create key_score_tuple to store key and match score
            key_score_tuple = (key, frequency_match_score(decrypted_text))
            frequency_scores.append(key_score_tuple)
        # Sort by score
        frequency_scores.sort(key=get_item_at_index_one, reverse=True)

        all_frequency_scores.append(frequency_scores[:4])

    for indexes in itertools.product(range(4), repeat=key_length):
        # Create attempt key from letters in all_frequency_scores
        key = ''
        for i in range(key_length):
            key += all_frequency_scores[i][indexes[i]][0]

        decrypted_text = decrypt(key, text)

        if is_english(decrypted_text):
            pass

    return None
