"""Vigenere - Poly-Alphabetic Substitution Cipher."""

from cs6903_project_one_python.constants import MESSAGE_SPACE

def encrypt(text: str, key: str) -> str:
    """Encrypt a string using the polyalphabetic substitution cipher (e.g. Vigénere) and the provided key.

    Args:
        string (str): The plaintext message (m) to encrypt.
        key (str): The key to use to encrypt the plaintext message (m).

    Returns:
        str: The encrypted ciphertext from plaintext message (m).
    """
    return shift_message(text, key, 'encrypt')

def decrypt(text: str, key: str) -> str:
    """Decrypt a string encrypted using the polyalphabetic substitution cipher (e.g. Vigénere) and the provided key.

    Args:
        string (str): The ciphertext message (c) to encrypt.
        key (str): The key to use to encrypt the ciphertext message (c).

    Returns:
        str: The decrypted plaintext from the ciphertext message (m).
    """
    return shift_message(text, key, 'decrypt')

def shift_message(text: str, key: str, mode: str) -> str:
    """Perform the letter shifting for the polyalphabetic substitution cipher (e.g. Vigénere).

    Args:
        string (str): The string that is being shifted.
        key (str): The key used to shift the string.
        mode (str): The mode (either "encrypt" or "decrypt") of the shift.

    Returns:
        str: The shifted string.
    """
    shifted_string = [] # Stores the shifted (encrypted / decrypted) string

    key_ndx = 0
    key = key.upper()

    for char in text:
        num = MESSAGE_SPACE.find(char.upper())
        if char.upper() in MESSAGE_SPACE:
            if mode == 'encrypt':
                num += MESSAGE_SPACE.find(key[key_ndx])
            elif mode == 'decrypt':
                num -= MESSAGE_SPACE.find(key[key_ndx])
            num %= len(MESSAGE_SPACE)

            if char.isupper():
                shifted_string.append(MESSAGE_SPACE[num])
            elif char.islower():
                shifted_string.append(MESSAGE_SPACE[num].upper())

            key_ndx += 1
            if key_ndx == len(key):
                key_ndx = 0
        else:
            shifted_string.append(char)
        print(char)
        print(shifted_string[-1])
    
    return ''.join(shifted_string)
