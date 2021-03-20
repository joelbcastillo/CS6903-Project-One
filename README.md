
CS6903 Project One Python
===

[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

CS6903 (Spring 2021) - Project One - Cryptanalysis of a Class of Ciphers

* GitHub repo: <https://github.com/joelbcastillo/CS6903-Project-One.git>
* Report - [castillo-chan-zhou-report.pdf](https://github.com/joelbcastillo/CS6903-Project-One/blob/main/castillo-chan-zhou-report.pdf)
* Free software: MIT

Features
---

```markdown
Usage: castillo-chan-zhou-decrypt-binary [OPTIONS] COMMAND [ARGS]...

  CS6903 Project One - Cryptanalysis of a Class of Ciphers using Kasiski Examination

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  test-one  Decrypt ciphertext using a chosen-message attack.

            This method uses a known dictionary of possible plaintexts (e.g. chosen
            messages) to attempt to decrypt ciphertext. The key is determined by using
            the Kasiski Examination method of Cryptanalysis combined with an optimized
            check of the decrypted text using the prefix of the known plaintexts to
            return a plaintext guess.

  test-two  Decrypt ciphertext using a chosen-message attack.

            This method uses a known dictionary of possible plaintext words to
            attempt to decrypt ciphertext. The key is determined by decrypting  the
            first (x) ciphertext characters (where x is the length of each  word in
            the dictionary). We then use the same key to decrypt the rest of the
            ciphertext. The key with the most words decrypted is returned as the guess
            of the plaintext.
```

Installation
---

To install castillo-chan-zhou-decrypt-binary, run this command in your terminal:

```shell
$ python3 -m venv venv
$ source venv/bin/activate
$ curl -H "Accept: application/vnd.github.v3+json" \
        https://api.github.com/repos/joelbcastillo/CS6903-Project-One/releases/latest \
    | grep "browser_download_url.*whl" \
    | cut -d : -f 2,3 \
    | tr -d \" \
    | wget -qi - 
$ pip install *.whl
```

This is the preferred method to install castillo-chan-zhou-decrypt-binary, as it will always install the most recent stable release.

Authors
---

* Ho Yin Kenneth Chan ([@kenliya](https://github.com/kenliya))
* Gary Zhou ([@g-zhou](https://github.com/g-zhou))
* Joel Castillo ([@joelbcastillo](https://github.com/joelbcastillo))

Credits
---

This package was created with [Cookiecutter][cookiecutter] and the [fedejaure/cookiecutter-modern-pypackage][cookiecutter-modern-pypackage] project template.

[cookiecutter]: https://github.com/cookiecutter/cookiecutter
[cookiecutter-modern-pypackage]: https://github.com/fedejaure/cookiecutter-modern-pypackage
