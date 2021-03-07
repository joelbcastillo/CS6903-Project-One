"""Tests for `cs6903_project_one_python`.cli module."""
from typing import List

import pytest
from click.testing import CliRunner

import cs6903_project_one_python
from cs6903_project_one_python import cli


@pytest.mark.parametrize(
    "options,expected",
    [
        ([], "cs6903_project_one_python.cli.main"),
        (["--help"], "Usage: main [OPTIONS]"),
        (["--version"], f"main, version { cs6903_project_one_python.__version__ }\n"),
    ],
)
def test_command_line_interface(options: List[str], expected: str) -> None:
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main, options)
    assert result.exit_code == 0
    assert expected in result.output
