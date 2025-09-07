"""Command-line interface (CLI) for playing 21 Nim.

Author: JosephBany
Created: 2025-09-05
Collaborators: ChatGPT (AI assistant)
"""
from __future__ import annotations
from .game import NimGame
from .exceptions import InvalidMoveError
from .player import Player


def prompt_int(prompt: str) -> int:
    """Prompt the user for an integer with validation.

    Args:
        prompt (str): The message shown to the user.

    Returns:
        int: The user's numeric input.

    Raises:
        ValueError: If input cannot be parsed as an integer.
    """
    raw = input(prompt).strip()
    return int(raw)


def play() -> None:
    """Play a full game of 21 Nim in the console.

    This function handles user interaction, error handling, and displays the outcome.
    """
    print("Welcome to 21 Nim!")
    name0 = input("Enter Player 1 name: ").strip() or "Player 1"
    name1 = input("Enter Player 2 name: ").strip() or "Player 2"

    game = NimGame(total_sticks=21, max_take=3, starting_player=0)
    players = [
        Player(name0, lambda: prompt_int(f"{name0}, take 1-{game.max_take} ({game.remaining} left): ")),
        Player(name1, lambda: prompt_int(f"{name1}, take 1-{game.max_take} ({game.remaining} left): ")),
    ]

    while not game.is_over():
        current = players[game.current_player]
        try:
            take = current.move_provider()
            mv = game.apply_move(take)
            print(f"{current.name} took {mv.taken} ({mv.before} -> {mv.after} left)")
        except ValueError:
            print("Invalid input. Please enter a whole number.")
        except InvalidMoveError as e:
            print(f"Invalid move: {e}")

    winner_index = game.winner()
    print(f"\nGame over! Winner: {players[winner_index].name}")


def main() -> None:
    """Entry point for `python -m nim21.cli`."""
    play()


if __name__ == "__main__":
    main()
