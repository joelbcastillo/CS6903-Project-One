"""Hacks for the Vigénere Cipher."""

from typing import Dict, List

from cs6903_project_one.constants import VALID_CHARACTERS_PATTERN


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
