"""Tests for `cs6903_project_one`.cli module."""
from typing import List

import pytest
from click.testing import CliRunner

import cs6903_project_one
from cs6903_project_one import cli

USAGE = """Usage: cli [OPTIONS] COMMAND [ARGS]...

  CS6903 Project One - CLI.

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  decrypt  Encrypt a string passed in on the CLI.
  encrypt  Encrypt a string passed in on the CLI."""


@pytest.mark.parametrize(
    "options,expected",
    [
        ([], USAGE),
        (["--help"], USAGE),
        (["--version"], f"cli, version { cs6903_project_one.__version__ }\n"),
    ],
)
def test_command_line_interface(options: List[str], expected: str) -> None:
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.cli, options)
    assert result.exit_code == 0
    assert expected in result.output
