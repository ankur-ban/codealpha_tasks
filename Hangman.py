import random

def play_hangman():
    stages = [
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / \\
           |
        """, # 0 lives left
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / 
           |
        """, # 1 life left
        """
           --------
           |      |
           |      O
           |     /|\\
           |      
           |
        """, # 2 lives left
        """
           --------
           |      |
           |      O
           |     /|
           |      
           |
        """, # 3 lives left
        """
           --------
           |      |
           |      O
           |      |
           |      
           |
        """, # 4 lives left
        """
           --------
           |      |
           |      O
           |    
           |      
           |
        """, # 5 lives left
        """
           --------
           |      |
           |      
           |    
           |      
           |
        """  # 6 lives left
    ]
    # 1. Setup: Predefined list and game variables
    words = ["python", "keyboard", "mountain", "coffee", "galaxy"]
    secret_word = random.choice(words)
    guessed_letters = []
    attempts_left = 6

    print("--- Welcome to Hangman! ---")

    # 2. Game Loop
    while attempts_left > 0:
        # show the stages
        print(stages[attempts_left])
        # Display the current progress (e.g., "p _ t h _ n")
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print(f"\nWord: {display_word}")
        print(f"Attempts left: {attempts_left}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")

        # Check if the player won
        if "_" not in display_word:
            print("Congratulations! You guessed the word!")
            break

        # 3. Handle Input
        guess = input("Guess a letter: ").lower()

        # Validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
        
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try again.")
            continue

        guessed_letters.append(guess)

        # 4. Check Guess
        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            attempts_left -= 1
            print(f"Sorry, '{guess}' is not there.")

    # 5. End Game State
    if attempts_left == 0:
        print(stages[attempts_left])
        print("\nGAME OVER!")
        print(f"The word was: {secret_word}")

if __name__ == "__main__":
    play_hangman()