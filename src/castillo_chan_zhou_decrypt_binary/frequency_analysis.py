"""Frequency Analysis for the Vigénere Cipher."""

from typing import Any, Dict

from castillo_chan_zhou_decrypt_binary.constants import (
    DICTIONARY_LETTER_FREQUENCY,
    LETTER_COUNT_DICT,
    MESSAGE_SPACE,
)


def get_item_at_index_zero(items: Any) -> Any:
    """Return the item at the specified index from the iterable.

    Used to sort lists.

    Args:
        items (Any): Iterable of items to parse.

    Returns:
        Any: the item at index one from the iterable
    """
    return items[0]


def get_letter_count(message: str) -> Dict[str, int]:
    """Get the number of valid letters in the message

    Args:
        message (str): The message.

    Returns:
        Dict[str, int]: A dictionary where keys are the letters, and
                        values are the number of occurrences
    """
    letter_count_dict = LETTER_COUNT_DICT.copy()
    for letter in message:
        if letter in MESSAGE_SPACE:
            letter_count_dict[letter] += 1
    return letter_count_dict


def get_frequency_order(message: str) -> str:
    """Return a string of letters ordered by frequency of occurence in the message.

    Args:
        message (str): The message

    Returns:
        str: The string of letters ordered by frequency
    """
    # Create dictionary with key being letter and value being the frequency count
    letter_count_dict = get_letter_count(message)

    # Create dictionary with key being frequency count and value being letter
    frequency_count_dict = {}
    for letter in MESSAGE_SPACE:
        if letter_count_dict[letter] not in frequency_count_dict:
            frequency_count_dict[letter_count_dict[letter]] = [letter]
        else:
            frequency_count_dict[letter_count_dict[letter]].append(letter)

    # Sort list of letters in reverse DICTIONARY_LETTER_FREQUENCY order and convert into a string
    for frequency in frequency_count_dict:
        frequency_count_dict[frequency].sort(key=DICTIONARY_LETTER_FREQUENCY.find, reverse=True)
        frequency_count_dict[frequency] = "".join(frequency_count_dict[frequency])

    # Convert the frequency_count_dict into a tuple and sort
    frequency_tuple = list(frequency_count_dict.items())
    frequency_tuple.sort(key=get_item_at_index_zero, reverse=True)

    # Store letters ordered by frequency into list
    ordered_frequency = []
    for ft in frequency_tuple:
        ordered_frequency.append(ft[1])

    return "".join(ordered_frequency)


def frequency_match_score(message: str) -> int:
    """Return an integer score for the number of matches in the letter frequency
    compared to the English letter frequency.

    Args:
        message (str): The message

    Returns:
        int: The string of letters ordered by frequency
    """
    frequency_ordered_string = get_frequency_order(message)

    score = 0
    for common_letter in DICTIONARY_LETTER_FREQUENCY[:6]:
        if common_letter in frequency_ordered_string[:6]:
            score += 1

    for least_common_letter in DICTIONARY_LETTER_FREQUENCY[-6:]:
        if least_common_letter in frequency_ordered_string[-6:]:
            score += 1

    return score
