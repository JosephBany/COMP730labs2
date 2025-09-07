"""Custom exceptions for the 21 Nim game.

Author: JosephBany
Created: 2025-09-05
Collaborators: ChatGPT (AI assistant)
"""

class InvalidMoveError(Exception):
    """Raised when a player attempts an invalid move in Nim.

    Attributes:
        message (str): Explanation of the error.
    """
    def __init__(self, message: str):
        """You have made an invalid move.

        Args:
            message (str): Explanation of what made the move invalid.
        """
        super().__init__(message)
        self.message = message
