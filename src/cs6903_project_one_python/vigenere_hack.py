"""Hacks for the Vigénere Cipher."""

from re import L
from typing import Dict

from cs6903_project_one_python.constants import VALID_CHARACTERS_PATTERN

def find_repeated_ciphertext_sequences(text: str) -> Dict(str):
    """[summary]

    Args:
        text (str): [description]
    """
    valid_text = VALID_CHARACTERS_PATTERN.sub('', text)

    sequence_spacings = {}

    for sequence_length in range(3, 6):
        for sequence_start_ndx in range(len(valid_text) - sequence_length):
            sequence = valid_text[sequence_start_ndx:sequence_start_ndx + sequence_length]

            for current_character_ndx in range(sequence_start_ndx + sequence_length, len(valid_text) - sequence_length):

                next_sequence_ndx = current_character_ndx + sequence_length

                if valid_text[current_character_ndx:next_sequence_ndx] == sequence:
                    if sequence not in sequence_spacings:
                        sequence_spacings[sequence] = []
                    
                    current_sequence_ndx_difference = current_character_ndx - sequence_start_ndx

                    sequence_spacings[sequence].append(current_sequence_ndx_difference)
    return sequence_spacings
