"""Tests for `castillo_chan_zhou_decrypt_binary` module."""
from typing import Generator

import pytest

import castillo_chan_zhou_decrypt_binary


@pytest.fixture
def version() -> Generator[str, None, None]:
    """Sample pytest fixture."""
    yield castillo_chan_zhou_decrypt_binary.__version__


def test_version(version: str) -> None:
    """Sample pytest test function with the pytest fixture as an argument."""
    assert version == "1.0.0"
