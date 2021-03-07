"""Tests for `cs6903_project_one` module."""
from typing import Generator

import pytest

import cs6903_project_one


@pytest.fixture
def version() -> Generator[str, None, None]:
    """Sample pytest fixture."""
    yield cs6903_project_one.__version__


def test_version(version: str) -> None:
    """Sample pytest test function with the pytest fixture as an argument."""
    assert version == "0.1.0"
