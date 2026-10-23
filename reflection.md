# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Select Hard difficulty | Hard difficulty has larger range| Hard range is smaller than Normal's range | none   |
| 56 > 12 > 78| 56, 12, and 78 appear in history|Only 56 appears| none  |
| Select 'New Game'| Start over with a fresh game| Stuck on "Game over" or "You already won"| none |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  
  I used Claude Code on this project. Claude Code functioned as a pair programmer that would make suggestions, explain code, and summarize information. 
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

  Claude noticed that the hints for the guesses were pointed the wrong way. A guess that was too high would say "Go HIGHER!" and a low guess would say "Go LOWER!" Claude suggested swapping the hint messages. I verified this suggestion by looking through the existing code, identifying the defect, and confirming that the new change provided the correct hints.
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version).It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

  I asked Claude to test the history fix by creating tests in test_game_logic.py; the tests consisted of multiple functions that would start up the app, submit guesses, and verify the history. I thought that the tests were too over-engineered, so I opted to instead check the app manually using various inputs and confirm that submitting each input (guess) produced the correct state. I essentially used the generated tests as an outline and manually checked each one using the provided inputs.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  
  I decided that a bug was really fixed if it passed manual testing, pytest, or both. If I only ran pytest for a certain fix, I would follow up with manual testing to confirm functionality. Ideally, both pytest and manual testing would be done to show that a bug was truly fixed.
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
  
  I ran tests test_winning_guess(), test_guess_too_high(), and test_guess_too_low(). These tests were from the original file and initially failed because, although the results were correct, the tests expected a single outcome like "Win" or "Too High" from check_guess, but check_guess actually returns a tuple like ("Win","🎉 Correct!"). After updating the tests, I ran them with pytest and all test passed, showing that the code fixes function as intended.
- Did AI help you design or understand any tests? How?
  
  Yes. Claude Code helped me design simple tests after I prompted it for a test for each fix. Claude also helped me understand the tests by providing helpful comments for each function and a tabular summary of test inputs, what each test checks, and what each test returns. If I had any questions or modifications, Claude would rework the design to fit my specification.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
