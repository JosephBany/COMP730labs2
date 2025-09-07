"""Player abstractions for 21 Nim.

Author: JosephBany
Created: 2025-09-05
Collaborators: ChatGPT (AI assistant)

This module defines a minimal :class:`Player` used by the CLI.
"""
from __future__ import annotations
from typing import Callable

class Player:
    """Represents a human (or strategy-driven) player.

    Attributes:
        name (str): Display name for the player.
        move_provider (Callable[[], int]): A no-argument callable that returns the number of sticks to take.
    """
    def __init__(self, name: str, move_provider: Callable[[], int]):
        """Create a Player.

        Args:
            name (str): Player's name.
            move_provider (Callable[[], int]): Function returning the next move as an int.

        Raises:
            ValueError: If name is empty or move_provider is not callable.
        """
        if not name:
            raise ValueError("Player name must be non-empty.")
        if not callable(move_provider):
            raise ValueError("move_provider must be callable.")
        self.name = name
        self.move_provider = move_provider
