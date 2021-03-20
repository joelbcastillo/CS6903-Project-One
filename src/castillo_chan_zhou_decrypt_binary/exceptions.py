"""CS6903 - Project One - Exceptions."""


class InvalidModeException(Exception):
    """Exception for when an invalid mode is passed to a function.

    i.e. when the mode is something other than "encrypt" or "decrypt"
    """

    def __init__(self: Exception, mode: str) -> None:
        """Initialize the InvalidModeException Class

        Args:
            mode (str): The invalid mode string passed in.
        """
        super().__init__(  # type: ignore
            f"Invalid Mode: {mode}. Mode must be one of (encrypt, decrypt)."
        )
