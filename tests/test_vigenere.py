"""Tests for `cs6903_project_one_python` module."""
from cs6903_project_one_python import vigenere


def test_encrypt() -> None:
    """Ensure encryption works properly."""
    key = "mykey"
    message = "nancy"

    result = vigenere.encrypt(message, key)

    assert result == " zyhw"


def test_decrypt() -> None:
    """Ensure decryption works properly."""
    key = "mykey"
    message = " zyhw"

    result = vigenere.decrypt(message, key)

    assert result == "nancy"
