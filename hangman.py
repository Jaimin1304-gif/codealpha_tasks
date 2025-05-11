import random

# List of words for the game
words_list = ['python', 'java', 'javascript', 'html', 'css', 'bootstrap', 'react', 'node', 'angular', 'django']

# Function to choose a random word
def get_random_word():
    return random.choice(words_list)

# Function to display the current state of the game
def display_hangman(tries):
    stages = [
        """
           -------
           |     |
           |     O
           |    /|\\
           |    / \\
           |
        ---------
        """,
        """
           -------
           |     |
           |     O
           |    /|\\
           |    / 
           |
        ---------
        """,
        """
           -------
           |     |
           |     O
           |    /|\\
           |
           |
        ---------
        """,
        """
           -------
           |     |
           |     O
           |    /|
           |
           |
        ---------
        """,
        """
           -------
           |     |
           |     O
           |     |
           |
           |
        ---------
        """,
        """
           -------
           |     |
           |     O
           |
           |
           |
        ---------
        """,
        """
           -------
           |     |
           |
           |
           |
           |
        ---------
        """
    ]
    return stages[tries]

# Function to play the game
def play_hangman():
    word = get_random_word().lower()
    word_letters = set(word)
    guessed_letters = set()
    tries = 6

    print("\nWelcome to Hangman! Let's play!\n")

    while len(word_letters) > 0 and tries > 0:
        print(display_hangman(tries))
        print("Guessed letters: ", " ".join(sorted(guessed_letters)))
        word_display = [letter if letter in guessed_letters else '_' for letter in word]
        print("Current word: ", " ".join(word_display))

        guess = input("\nGuess a letter: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("\nYou already guessed that letter. Try another one.")
            elif guess in word_letters:
                guessed_letters.add(guess)
                word_letters.remove(guess)
                print("\nGood job! The letter is in the word.")
            else:
                guessed_letters.add(guess)
                tries -= 1
                print("\nIncorrect guess. Try again.")
        else:
            print("\nInvalid input. Please enter a single letter.")

    if tries == 0:
        print(display_hangman(tries))
        print(f"\nSorry, you lost. The word was: {word}")
    else:
        print(f"\nCongratulations! You guessed the word: {word}!")

# Start the game
if __name__ == '__main__':
    play_hangman()
