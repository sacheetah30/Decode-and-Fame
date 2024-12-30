# Decode & Fame 
#### Video Demo: https://youtu.be/GTJYM44zid4
## Project Overview

"Decode and Fame" is a fun and interactive console-based guessing game where players decrypt the encrypted name of an actor using hints and logical deduction. The names of the actors and their famous movies are preloaded, and the names are encrypted using a Caesar cipher with a randomly generated key. Players attempt to guess the actor’s name, request hints, or quit the game at any point.


## Features
- **Caesar Cipher Encryption:** Encrypts the actor’s name using a randomly generated shift key.
- **Interactive Gameplay:** Players can guess letters, request hints, or quit the game.
- **Hints:** Provides movie hints for the selected actor to assist the player.
- **Colored Text Display:** Uses ANSI escape codes to provide visual feedback for correctly guessed letters.
- **Random Selection:** Randomly selects an actor’s name and movies for each round.

## Technologies Used
- **Python 3.8 or higher**
- **ANSI Escape Codes:** For colored output in the terminal.
- **Random Module:** To generate random shift keys and select movies for hints.

## How It Works
1. **Initialization:**
   - A random actor’s name is selected along with their list of movies.
   - The actor’s name is encrypted using a Caesar cipher with a randomly generated key.
2. **Gameplay Loop:**
   - The player’s progress is displayed with underscores representing unguessed letters.
   - The player can choose one of the following actions:
     1. Guess the actor’s name.
     2. Request a hint (a movie starring the actor is revealed).
     3. Quit the game.
3. **Guessing:**
   - Players enter their guesses. Correct guesses reveal the respective letters in the encrypted name.
   - The game ends when the player successfully decrypts the name or decides to quit.
4. **Hint System:**
   - Provides the player with a movie hint to aid in guessing the actor’s name.

## Setup Instructions
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/sacheetah30/Decode-and-Fame.git
   ```
2. **Run the Game:**

 Ensure you have Python installed on your system, then execute the following command:

```bash
python project.py
```
3. **Run the Tests:** 

Run the test file using pytest:

```bash
pytest test_project.py
```

**File Structure**

- `project.py`: The main game logic.
- `test_project.py`: Contains unit tests for verifying the functionality of the project.

**Sample Gameplay**
```bash
WELCOME TO THE GUESSING GAME!!!
Encrypted quote:
_ _ _ _ _
A D S J K

Options:
1. Guess the actor's name
2. Ask for a hint
3. Quit
Enter your option (1, 2, or 3): 
```
**Example Hint:**
```
Hint: The actor stars in the movie 'Inception'.
```

**Testing**
The project includes unit tests written using pytest to ensure:

- The Caesar cipher encrypts and decrypts names correctly.
- Hints are correctly generated and displayed.
- User progress updates appropriately with each correct guess.



**Future Improvements**

- Add support for multi-word actor names and partial matches.
- Implement difficulty levels with variable cipher complexities.
- Add a leaderboard to track high scores and completion times.
- Provide additional hints, such as genres or co-stars.
- Contribution Guidelines
- Fork the repository and create a new branch for your feature or bug fix.
- Write descriptive commit messages and document your code.
- Submit a pull request with a detailed explanation of your changes.
---
**License**

This project is licensed under the MIT License.

---