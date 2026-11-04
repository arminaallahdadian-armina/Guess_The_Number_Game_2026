🎮 Guess The Number Game

1. Project Overview

Guess The Number is a graphical number guessing game developed using Python and the Tkinter library.

The program generates a random number between 1 and 100, and the player must guess the secret number within a limited number of attempts.

The game provides visual feedback, tracks the player's remaining chances, and displays different messages based on the player's performance.

2. Project Objectives

The main objectives of this project are:

- Practicing Python programming.
- Working with functions and conditional statements.
- Using loops and variables.
- Generating random numbers.
- Developing a graphical user interface (GUI).
- Handling user input and validating data.
- Working with Tkinter widgets and event handling.

3. Technologies Used

- Programming Language: Python
- GUI Library: Tkinter
- Random Number Generation: Python Random Module
- Development Environment: Visual Studio Code

4. Game Features

- Generates a random secret number between 1 and 100.
- Provides five chances to guess the correct number.
- Displays helpful hints such as "Too High" and "Too Low".
- Shows the remaining chances using heart icons.
- Validates user input.
- Invalid inputs do not reduce the remaining chances.
- Displays different messages based on the game result.
- Reveals the secret number when the player loses.
- Includes a ranking system.
- Displays an emoji animation when the player wins.
- Provides a Play Again button to restart the game.

5. Game Rules

1. The computer randomly selects a number between 1 and 100.
2. The player enters a guess.
3. If the guess is too high, the game displays a "Too High" message.
4. If the guess is too low, the game displays a "Too Low" message.
5. The player has five valid attempts.
6. If the player guesses correctly, the game displays a winning message.
7. If all attempts are used, the game ends and reveals the secret number.
8. The player can start a new round using the Play Again button.

6. Input Validation

The program checks the player's input before processing it.

- Empty inputs are not accepted.
- Non-numeric inputs are rejected.
- Numbers outside the range of 1 to 100 are not accepted.
- Invalid inputs do not consume a game attempt.

7. How to Run the Project

Requirements

- Python 3.x
- Tkinter (usually included with standard Python installations)

Steps

1. Install Python 3 if it is not already installed.
2. Download or clone this repository.
3. Open the project folder.
4. Run the following command in the terminal:

python guessing_game_gui.py.py

8. Project Structure

Guess-The-Number-Game/
│
├── guessing_game_gui.py.py
│
└── README.md

9. Conclusion

This project demonstrates the use of basic Python programming concepts in a practical graphical application.

It combines random number generation, conditional logic, input validation, functions, and GUI development to create an interactive and user-friendly game.

---

Developed as a Python Programming Course Project.
