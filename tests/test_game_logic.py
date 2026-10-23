from logic_utils import check_guess, get_range_for_difficulty, new_game_state

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Even-attempt string comparison fix ---

def test_check_guess_compares_numbers_not_text():
    # As text, "100" sorts before "89", which used to make this guess "Too Low"
    outcome, message = check_guess(100, 89)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"


# --- Difficulty range fix ---

def test_hard_range_is_larger_than_normal():
    # Hard used to be 1-50, smaller than Normal's 1-100, which made Hard easier
    easy_low, easy_high = get_range_for_difficulty("Easy")
    normal_low, normal_high = get_range_for_difficulty("Normal")
    hard_low, hard_high = get_range_for_difficulty("Hard")
    assert easy_high - easy_low < normal_high - normal_low < hard_high - hard_low

def test_each_difficulty_returns_expected_range():
    # Each difficulty should return its own range, with Hard now 1-200 instead of 1-50
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 200)


# --- New game reset fix ---

def test_new_game_state_resets_everything():
    # New Game used to leave the status, history and attempts from the last game
    state = new_game_state(1, 20)
    assert 1 <= state["secret"] <= 20
    assert state["attempts"] == 0
    assert state["score"] == 0
    assert state["status"] == "playing"
    assert state["history"] == []
