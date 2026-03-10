import random

def hangman():
    # Predefined list of 5 words
    words = ['python', 'java', 'github', 'intern', 'coding']
    word_to_guess = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("--- Welcome to Hangman! ---")
    print(f"I'm thinking of a {len(word_to_guess)} letter word.")

    while attempts > 0:
        # Display the current state of the word
        display_word = ""
        for letter in word_to_guess:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print(f"\nWord: {display_word}")
        print(f"Attempts left: {attempts}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")

        if "_" not in display_word:
            print("Congratulations! You won!")
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print(f"Good job! '{guess}' is in the word.")
        else:
            attempts -= 1
            print(f"Sorry, '{guess}' is not in the word.")

    if attempts == 0:
        print(f"\nGame Over! The word was: {word_to_guess}")

if __name__ == "__main__":
    hangman()