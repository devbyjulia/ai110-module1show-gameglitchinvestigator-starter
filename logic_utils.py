def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


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

