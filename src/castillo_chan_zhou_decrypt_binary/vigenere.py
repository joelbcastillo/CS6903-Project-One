"""Vigenere - Poly-Alphabetic Substitution Cipher."""

from castillo_chan_zhou_decrypt_binary.constants import MESSAGE_SPACE
from castillo_chan_zhou_decrypt_binary.exceptions import InvalidModeException


def encrypt(text: str, key: str) -> str:
    """Encrypt a string using the polyalphabetic substitution cipher (e.g. Vigénere) and
       the provided key.

    Args:
        text (str): The plaintext message (m) to encrypt.
        key (str): The key to use to encrypt the plaintext message (m).

    Returns:
        str: The encrypted ciphertext from plaintext message (m).
    """
    return shift_message(text, key, "encrypt")


def decrypt(text: str, key: str) -> str:
    """Decrypt a string encrypted using the polyalphabetic substitution cipher (e.g. Vigénere) and
       the provided key.

    Args:
        text (str): The ciphertext message (c) to encrypt.
        key (str): The key to use to encrypt the ciphertext message (c).

    Returns:
        str: The decrypted plaintext from the ciphertext message (m).
    """
    return shift_message(text, key, "decrypt")


def shift_message(text: str, key: str, mode: str) -> str:
    """Perform the letter shifting for the polyalphabetic substitution cipher (e.g. Vigénere).

    Args:
        text (str): The string that is being shifted.
        key (str): The key used to shift the string.
        mode (str): The mode (either "encrypt" or "decrypt") of the shift.

    Returns:
        str: The shifted string.

    Raises:
        InvalidModeException: When the mode is not in (encrypt, decrypt).
    """
    shifted_string = []  # Stores the shifted (encrypted / decrypted) string

    key_ndx = 0

    for char in text:
        num = MESSAGE_SPACE.find(char)
        if char in MESSAGE_SPACE:
            if mode == "encrypt":
                num += MESSAGE_SPACE.find(key[key_ndx])
            elif mode == "decrypt":
                num -= MESSAGE_SPACE.find(key[key_ndx])
            else:
                raise InvalidModeException(mode)
            num %= len(MESSAGE_SPACE)

            shifted_string.append(MESSAGE_SPACE[num])

            key_ndx += 1
            if key_ndx == len(key):
                key_ndx = 0
        else:
            shifted_string.append(char)

    return "".join(shifted_string)
