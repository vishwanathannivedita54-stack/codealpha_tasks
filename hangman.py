import random

# Predefined list of 5 words
WORDS = ["python", "coding", "hangman", "laptop", "github"]

def display_state(guessed_letters, word, wrong_guesses):
    print("\n--- HANGMAN GAME ---")
    print(f"Wrong guesses left: {6 - wrong_guesses}")
    print("Word: " + " ".join(letter if letter in guessed_letters else "_" for letter in word))
    print("Guessed letters: " + ", ".join(sorted(guessed_letters)) if guessed_letters else "Guessed letters: None")

def hangman():
    word = random.choice(WORDS)
    guessed_letters = set()
    wrong_guesses = 0

    print("Welcome to Hangman! Guess the word letter by letter.")

    while wrong_guesses < 6:
        display_state(guessed_letters, word, wrong_guesses)

        # Check if word is fully guessed
        if all(letter in guessed_letters for letter in word):
            print(f"\n🎉 Congratulations! You guessed the word: '{word}'")
            return

        guess = input("\nEnter a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("⚠️  You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"✅ Good guess! '{guess}' is in the word.")
        else:
            wrong_guesses += 1
            print(f"❌ Wrong! '{guess}' is not in the word. ({6 - wrong_guesses} guesses left)")

    print(f"\n💀 Game Over! The word was: '{word}'")

if __name__ == "__main__":
    hangman()
