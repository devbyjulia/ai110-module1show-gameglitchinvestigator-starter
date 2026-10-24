# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.

  Game Glitch Investigator is a number guessing game built with Streamlit. The game picks a secret number, and the player tries to guess it within a set number of attempts. After each guess, a hint says whether to go higher or lower. The difficulty setting changes the range and the number of attempts: Easy is 1–20 with 6 attempts, Normal is 1–100 with 8, and Hard is 1–200 with 5. The player earns more points for winning in fewer guesses. The project's real goal is to find and fix the bugs in AI-generated code, move the game logic into `logic_utils.py`, and test it with `pytest`.

- [x] Detail which bugs you found.

  1. **Guesses were missing from the history.** If you entered several guesses quickly, some were never recorded. For example, entering 56, 12 and 78 gave a history with only 56 in it.
  2. **The debug panel was one guess behind.** It showed the history from before your latest guess.
  3. **The hints were backwards.** A guess that was too high said "Go HIGHER!" and a guess that was too low said "Go LOWER!"
  4. **Every other guess was compared as text.** On even-numbered attempts, the secret was turned into a string, so the guess and secret were compared alphabetically. For example, `"100" < "89"`. That made some hints wrong.
  5. **Hard was easier than Normal.** Hard used a range of 1–50, which is smaller than Normal's 1–100.
  6. **Changing difficulty kept the old secret.** The secret could fall outside the new range. For example, Normal's secret of 87 stayed when you switched to Easy (1–20).
  7. **The prompt always said "between 1 and 100,"** whatever the difficulty.
  8. **New Game always picked a secret from 1 to 100,** whatever the difficulty.
  9. **New Game didn't really start over.** It reset only the secret and attempts. After you won or lost, you stayed stuck on "You already won" or "Game over," and the old history and score carried over.
  10. **Attempts started at 1 instead of 0.** You lost one attempt before you made a guess.
  11. **The debug panel was empty after a game ended.** The app stopped before the panel was filled in.

- [x] Explain what fixes you applied.

  1. **Put the guess box and Submit button in a form** (`st.form`). The guess and the submit now go through together, so every guess is recorded. Pressing Enter also submits.
  2. **Fill in the debug panel after the guess is processed.** Its spot on the page is reserved first, and it's filled in by `show_debug_info()` once the new guess is in the history.
  3. **Swapped the hint messages** in `check_guess`. Too high now says "📉 Go LOWER!" and too low says "📈 Go HIGHER!"
  4. **Removed the string conversion** in `app.py` and the text-comparison fallback in `check_guess`. Every guess is now compared as a number.
  5. **Changed Hard's range to 1–200** in `get_range_for_difficulty`, so each difficulty's range is larger than the one before it.
  6. **Start a new game whenever the difficulty changes.** The app saves the current difficulty and starts a fresh game when the player picks a different one.
  7. **Show the range for the chosen difficulty** in the prompt.
  8. **New Game now uses the difficulty's range** for the new secret.
  9. **Added `new_game_state()`** in `logic_utils.py`. It returns everything a fresh game needs: secret, attempts, score, status and history. New Game and a difficulty change both use it.
  10. **Attempts now start at 0** in `new_game_state()`.
  11. **Fill in the debug panel before the app stops** when a game is over.

  **Refactoring and tests:** Moved `check_guess` and `get_range_for_difficulty` from `app.py` into `logic_utils.py` so they can be tested on their own. Added `pytest` tests for the hints, the difficulty ranges and the New Game reset.

## 📸 Demo Walkthrough

The secret number is random each game, so this example uses 42.

1. **Start the game.** Run `python -m streamlit run app.py`. The page shows **🎮 Game Glitch Investigator**. The sidebar shows the default difficulty, **Normal**: `Range: 1 to 100` and `Attempts allowed: 8`. The blue info box says *"Guess a number between 1 and 100. Attempts left: 8"*.
2. **Peek at the secret (optional).** Open **Developer Debug Info**. It shows `Secret: 42`, `Attempts: 0`, `Score: 0`, `Difficulty: Normal` and `History: []`. The secret stays the same each time you submit a guess.
3. **Make a first guess that's too high.** Type `50` and press **Submit Guess 🚀** (or press Enter). A yellow hint says **"📉 Go LOWER!"** The debug panel now shows `Attempts: 1`, `Score: -5` and `History: [50]`.
4. **Make a guess that's too low.** Type `25` and submit. The hint says **"📈 Go HIGHER!"** The debug panel shows `Attempts: 2`, `Score: -10` and `History: [50, 25]`. The new guess appears in the history right away.
5. **Get closer.** Type `40` and submit. The hint says **"📈 Go HIGHER!"** You now have `Attempts: 3`, `Score: -15` and `History: [50, 25, 40]`.
6. **Win.** Type `42` and submit. The hint says **"🎉 Correct!"**, balloons appear, and a green message says *"You won! The secret was 42. Final score: 35"*. A win on attempt 4 is worth 100 − 10 × 5 = 50 points, which brings the score from −15 to 35.
7. **Try to keep playing.** Submit another guess. The game says *"You already won. Start a new game to play again."* and doesn't count it.
8. **Start a new game.** Click **New Game 🔁**. The game picks a new secret from 1 to 100 and resets everything: `Attempts: 0`, `Score: 0`, `History: []`, and the status goes back to playing.
9. **Change difficulty.** In the sidebar, choose **Hard**. The range becomes `1 to 200` with `5` attempts, and the info box changes to match. A new game starts on its own with a secret inside the new range. **Easy** works the same way, with a range of 1 to 20 and 6 attempts.
10. **Lose a game.** On Easy, make 6 wrong guesses. After the sixth, a red message says *"Out of attempts! The secret was N. Score: X"*, and any more guesses are blocked with *"Game over. Start a new game to try again."*
11. **Enter something that isn't a number.** Type `abc` and submit. The game says *"That is not a number."*

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
platform win32 -- Python 3.13.13, pytest-9.1.1, pluggy-1.6.0

rootdir: C:\ai110-module1show-gameglitchinvestigator-starter

plugins: anyio-4.15.1

collected 7 items                                                                                                                                                                          

tests\test_game_logic.py .......                                                                                                                                                     [100%]

=========================== 7 passed in 0.03s ============================
```


## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
