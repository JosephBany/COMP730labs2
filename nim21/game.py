"""Core game logic for 21 Nim.

Author: JoseBany
Created: 2025-09-05
Collaborators: ChatGPT (AI assistant)

This module exposes the :class:`NimGame` class that models a two-player game
with a pile of 21 sticks and legal moves of removing 1 to 3 sticks per turn.

Docstring style: Google style (chosen for consistency).
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, List

from .exceptions import InvalidMoveError

@dataclass
class Move:
    """Represents a single move in Nim.

    Attributes:
        player_index (int): Index of the player who made the move (0 or 1).
        taken (int): Number of sticks taken in the move.
        before (int): Number of sticks before the move.
        after (int): Number of sticks after the move.
    """
    player_index: int
    taken: int
    before: int
    after: int


class NimGame:
    """A two-player 21 Nim game with configurable parameters.

    Attributes:
        total_sticks (int): The initial number of sticks (default 21).
        max_take (int): The maximum number of sticks a player can take per turn (default 3).
        current_player (int): The index of the current player (0 or 1).
        remaining (int): The number of sticks left in the pile.
        history (List[Move]): A list of moves made so far.

    Note:
        - By default, the starting player is 0.
        - The player who removes the last stick **wins** in this variant.
    """

    def __init__(self, total_sticks: int = 21, max_take: int = 3, starting_player: int = 0):
        """Initialize a new Nim game.

        Args:
            total_sticks (int): Starting number of sticks (must be >= 1).
            max_take (int): Maximum sticks removable per turn (must be >= 1).
            starting_player (int): Index of the starting player (0 or 1).

        Raises:
            ValueError: If provided parameters are out of valid ranges.
        """
        if total_sticks < 1:
            raise ValueError("total_sticks must be >= 1")
        if max_take < 1:
            raise ValueError("max_take must be >= 1")
        if starting_player not in (0, 1):
            raise ValueError("starting_player must be 0 or 1")

        self.total_sticks: int = total_sticks
        self.max_take: int = max_take
        self.current_player: int = starting_player
        self.remaining: int = total_sticks
        self.history: List[Move] = []

    def legal_take_range(self) -> range:
        """Return the legal inclusive range of sticks that can be taken now.

        Returns:
            range: A Python range from 1 to min(max_take, remaining) inclusive.
        """
        return range(1, min(self.max_take, self.remaining) + 1)

    def validate_move(self, take: int) -> None:
        """Validate a requested move or raise an error.

        Args:
            take (int): Number of sticks the current player wants to take.

        Raises:
            InvalidMoveError: If the move is not within the legal range or exceeds remaining sticks.
        """
        if not isinstance(take, int):
            raise InvalidMoveError("Move must be an integer.")
        if take < 1:
            raise InvalidMoveError("You must take at least 1 stick.")
        if take > self.max_take:
            raise InvalidMoveError(f"You cannot take more than {self.max_take} sticks.")
        if take > self.remaining:
            raise InvalidMoveError("You cannot take more sticks than remain in the pile.")

    def apply_move(self, take: int) -> Move:
        """Apply a validated move, update state, and switch turns.

        Args:
            take (int): Number of sticks to remove.

        Returns:
            Move: A record of the move that was applied.

        Raises:
            InvalidMoveError: If the move is illegal.
        """
        self.validate_move(take)
        before = self.remaining
        self.remaining -= take
        mv = Move(self.current_player, take, before, self.remaining)
        self.history.append(mv)
        # Switch player only if game not over
        if self.remaining > 0:
            self.current_player = 1 - self.current_player
        return mv

    def is_over(self) -> bool:
        """Check whether the game has ended.

        Returns:
            bool: True if no sticks remain; otherwise False.
        """
        return self.remaining == 0

    def winner(self) -> Optional[int]:
        """Return the index of the winning player if the game is over.

        Returns:
            Optional[int]: 0 or 1 if the game is over; otherwise None.
        """
        if not self.is_over():
            return None
        # The player who took the last stick is the one who made the last move.
        return self.history[-1].player_index if self.history else None

    def reset(self, starting_player: Optional[int] = None) -> None:
        """Reset the game to a fresh state.

        Args:
            starting_player (Optional[int]): If provided, sets the starting player (0 or 1).

        Raises:
            ValueError: If starting_player is not 0 or 1 when provided.
        """
        if starting_player is not None and starting_player not in (0, 1):
            raise ValueError("starting_player must be 0 or 1 when provided")
        self.current_player = self.current_player if starting_player is None else starting_player
        self.remaining = self.total_sticks
        self.history.clear()
