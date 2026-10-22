import random


def new_game_state(low: int, high: int):
    """Return the session values for a fresh game with a secret in [low, high]."""
    # FIX: New Game used to reset only the secret and attempts, so a finished game
    # stayed "won"/"lost" and the old history carried over. This returns every value
    # a fresh game needs, and both New Game and a difficulty change use it.
    # FIX: Attempts start at 0. They used to start at 1 on the first load, which cost
    # the player one guess before they had made any.
    return {
        "secret": random.randint(low, high),
        "attempts": 0,
        "score": 0,
        "status": "playing",
        "history": [],
    }


def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    # FIX: Moved here from app.py so the difficulty ranges can be tested on their own.
    # FIX: Hard used to be 1-50, a smaller range than Normal's 1-100, which made Hard
    # easier. Hard is now 1-200 so each difficulty's range is larger than the last.
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 200
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    # FIX: Moved here from app.py so the game logic can be tested on its own.
    if guess == secret:
        return "Win", "🎉 Correct!"

    # FIX: The hint messages were swapped. A guess that is too high now says to go
    # lower, and a guess that is too low says to go higher.
    # FIX: Removed the fallback that compared the guess and secret as text when their
    # types didn't match. It only existed for the even-attempt conversion in app.py,
    # and it hid that bug by giving alphabetical hints instead of raising an error.
    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")

