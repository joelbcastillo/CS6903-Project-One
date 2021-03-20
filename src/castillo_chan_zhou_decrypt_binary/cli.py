"""Console script for castillo-chan-zhou-decrypt-binary."""
import click

from castillo_chan_zhou_decrypt_binary import __version__, vigenere_hack


@click.group()
@click.version_option(__version__)
def cli() -> int:
    """CS6903 Project One - Cryptanalysis of a Class of Ciphers using Kasiski Examination"""
    return 0


@cli.command()
def test_one() -> int:
    """Decrypt ciphertext using a chosen-message attack.

    This method uses a known dictionary of possible plaintexts (e.g. chosen messages)
    to attempt to decrypt ciphertext. The key is determined by using the Kasiski Examination
    method of Cryptanalysis combined with an optimized check of the decrypted text using the
    prefix of the known plaintexts to return a plaintext guess.

    Prints the plaintext guess to the CLI.

    Returns:
        int: Return code
    """
    ciphertext = click.prompt("Enter the ciphertext")
    plaintext = vigenere_hack.hack_vigenere(ciphertext, "test_one")
    click.echo(f"My plaintext guess is: {plaintext}")
    return 0


@cli.command()
def test_two() -> int:
    """Decrypt ciphertext using a chosen-message attack.

    This method uses a known dictionary of possible plaintext words to
    attempt to decrypt ciphertext. The key is determined by decrypting
    the first (x) ciphertext characters (where x is the length of each
    word in the dictionary). We then use the same key to decrypt
    the rest of the ciphertext. The key with the most words
    decrypted is returned as the guess of the plaintext.

    Prints the plaintext guess to the CLI.

    Returns:
        int: Return code
    """
    ciphertext = click.prompt("Enter the ciphertext")
    plaintext = vigenere_hack.hack_vigenere(ciphertext, "test_two")
    click.echo(f"My plaintext guess is: {plaintext}")
    return 0


if __name__ == "__main__":
    cli()  # pragma: no cover
