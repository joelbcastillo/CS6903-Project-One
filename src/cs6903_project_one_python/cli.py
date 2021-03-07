"""Console script for CS6903-Project-One-python."""
import click

from cs6903_project_one_python import __version__
from cs6903_project_one_python import vigenere

@click.group()
def cli():
    """CS6903 Project One - CLI"""
    pass

@cli.command()
@click.option("--text", type=str, prompt=True)
@click.option("--key", type=str, prompt=True)
def encrypt(text: str, key: str) -> int:
    """Encrypt a string passed in on the CLI."""
    click.echo(vigenere.encrypt(text, key))
    return 0


@cli.command()
@click.option("--text", type=str, prompt=True)
@click.option("--key", type=str, prompt=True)
def decrypt(text: str, key: str) -> int:
    """Encrypt a string passed in on the CLI."""
    click.echo(vigenere.decrypt(text, key))
    return 0


if __name__ == "__main__":
    cli()  # pragma: no cover
