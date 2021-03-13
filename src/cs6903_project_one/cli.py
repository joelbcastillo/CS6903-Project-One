"""Console script for CS6903-Project-One."""
import click

from cs6903_project_one import __version__, cs6903_custom_cipher, vigenere


@click.group()
@click.version_option(__version__)
def cli() -> int:
    """CS6903 Project One - CLI."""
    return 0


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
@click.option("--random-seed", type=int, prompt=False, default=0)
def cs6903_encrypt(text: str, key: str, random_seed: int) -> int:
    """Encrypt a string passed in on the CLI using the CS6903 Project One Cipher."""
    click.echo(cs6903_custom_cipher.encrypt(text, key, random_seed))
    return 0


@cli.command()
@click.option("--text", type=str, prompt=True)
@click.option("--key", type=str, prompt=True)
def decrypt(text: str, key: str) -> int:
    """Decrypt a string passed in on the CLI."""
    click.echo(vigenere.decrypt(text, key))
    return 0


if __name__ == "__main__":
    cli()  # pragma: no cover
