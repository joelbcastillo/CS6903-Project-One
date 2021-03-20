"""Tests for `castillo_chan_zhou_decrypt_binary.vigenere` module."""
import pytest

from castillo_chan_zhou_decrypt_binary import vigenere
from castillo_chan_zhou_decrypt_binary.exceptions import InvalidModeException


@pytest.mark.parametrize(
    "message, key, ciphertext",
    [("nancy", "mykey", " zyhw"), ("nancy!", "mykey", " zyhw!")],
)
def test_encrypt(
    message: str,
    key: str,
    ciphertext: str,
) -> None:
    """Ensure encryption works properly."""
    result = vigenere.encrypt(message, key)

    assert result == ciphertext


@pytest.mark.parametrize(
    "ciphertext, key, message",
    [(" zyhw", "mykey", "nancy"), (" zyhw!", "mykey", "nancy!")],
)
def test_decrypt(ciphertext: str, key: str, message: str) -> None:
    """Ensure decryption works properly."""
    result = vigenere.decrypt(ciphertext, key)

    assert result == message


def test_shift_method_invalid_mode() -> None:
    """Ensure shift method works properly."""
    message = "nancy"
    key = "mykey"
    mode = ""
    with pytest.raises(InvalidModeException):
        vigenere.shift_message(message, key, mode)
