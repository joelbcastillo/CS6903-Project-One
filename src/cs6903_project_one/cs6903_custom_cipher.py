"""CS6903 - Project 1 - Custom Cipher."""
from random import randint
from typing import Tuple

from cs6903_project_one.constants import MESSAGE_SPACE


def encrypt(message: str, key: str) -> str:
    """Encode a message using the CS6903 Permutation of the Vigenere Cipher.

    Args:
        message (str): Message to be encrypted.
        key (str): The key for the encryption

    Returns:
        str: Encrypted plaintext message (i.e. ciphertext)
    """
    input_len = len(message)
    expanded_key = expand_key(key, input_len)

    input_char_ndx = 0
    random_char_ctr = 0

    encrypted_string = ""

    while input_char_ndx < input_len:
        if message[input_char_ndx] in MESSAGE_SPACE:
            message_space_ndx = MESSAGE_SPACE.find(message[input_char_ndx])
            ciphertext_char_ndx, random_char = scheduling_algorithm(
                input_char_ndx, message_space_ndx, input_len, expanded_key
            )
            encrypted_string += MESSAGE_SPACE[ciphertext_char_ndx]
            if random_char:
                message = (
                    message[:input_char_ndx]
                    + MESSAGE_SPACE[ciphertext_char_ndx]
                    + message[input_char_ndx:]
                )
                random_char_ctr += 1
        else:
            encrypted_string += message[input_char_ndx]

        input_char_ndx += 1

    return encrypted_string


def expand_key(key: str, string_length: int) -> str:
    """Expand the length of the encryption key so that it is longer than the the input.

    Args:
        key (str): Encryption key for the encryption algorithm.
        string_length (int): Length of the inputted plaintext.

    Returns:
        str: New key for encryption.
    """
    expanded_key = key

    while len(expanded_key) < string_length:
        expanded_key += key

    return expanded_key


def scheduling_algorithm(
    input_ndx: int, input_char_ndx: int, input_len: int, key: str
) -> Tuple[int, bool]:
    """Scheduling algorithm used to encrypt a specific character.

    Args:
        input_ndx (int): Index of the current character in the plaintext.
        input_char_ndx (int):  Index of the input character in the MESSAGE_SPACE
        input_len (int): length of the plaintext
        key (str): The encryption key

    Returns:
        (int, int, bool): A tuple containing
                            - the index of the encrypted character in the alphabet
                            - A bool that is true if a random character was inserted
    """
    key_ndx = (input_len * input_ndx) % len(key)

    if key_ndx > 0 and key_ndx < len(key):
        key_char = key[key_ndx]

        key_char_ndx = MESSAGE_SPACE.find(key_char)

        new_char_ndx = input_char_ndx + key_char_ndx

        if new_char_ndx > 26:
            new_char_ndx -= 27

        return new_char_ndx, False
    else:
        return randint(0, 26), True
