"""Detect if words are English."""

from typing import Optional

from cs6903_project_one.constants import PLAINTEXT_DICTIONARY_TWO


def get_english_count(message: str) -> float:
    """Count the number of english words in a message to determine it's
       percentage of valid english words.

    Args:
        message (str): Message to check for english words

    Returns:
        float: Percentage of valid english words in the message
    """
    possible_words = message.split(" ")

    if possible_words == []:
        return 0.0

    matches = 0
    for word in possible_words:
        if word in PLAINTEXT_DICTIONARY_TWO:
            matches += 1
    return float(matches) / len(possible_words)


def is_english(
    message: str,
    min_valid_word_percentage: Optional[int] = 20,
    min_valid_letter_percentage: Optional[int] = 85,
) -> bool:
    """Determine if a message is english.

    Args:
        message (str): The message to check
        min_valid_word_percentage (int, optional): The percentage of words that must be english to make the message english. Defaults to 20.
        min_valid_letter_percentage (int, optional): The number of letters that must match to make the message english. Defaults to 85.

    Returns:
        bool: True if the message is english
    """
    matching_words = get_english_count(message) * 100 >= min_valid_word_percentage
    num_letters = len(message)
    message_letter_percentage = float(num_letters) / len(message) * 100
    letters_match = message_letter_percentage >= min_valid_letter_percentage
    return matching_words and letters_match
