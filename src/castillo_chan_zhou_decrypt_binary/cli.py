"""Console script for CS6903-Project-One."""
import click

from castillo_chan_zhou_decrypt_binary import __version__, vigenere_hack


@click.group()
@click.version_option(__version__)
def cli() -> int:
    """CS6903 Project One - CLI."""
    return 0


@cli.command()
def test_one() -> int:
    """Attempt to decrypt ciphertext using Kasiski examination + known plaintext attack."""
    ciphertext = click.prompt("Enter the ciphertext")
    plaintext = vigenere_hack.hack_vigenere(ciphertext, "test_one")
    click.echo(f"My plaintext guess is: {plaintext}")
    return 0


@cli.command()
def test_two() -> int:
    """Attempt to decrypt ciphertext using Kasiski examination + brute force."""
    ciphertext = click.prompt("Enter the ciphertext")
    plaintext = vigenere_hack.hack_vigenere(ciphertext, "test_two")
    click.echo(f"My plaintext guess is: {plaintext}")
    return 0


if __name__ == "__main__":
    cli()  # pragma: no cover
