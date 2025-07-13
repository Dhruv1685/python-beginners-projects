import random

words = ['python', 'hangman', 'programming', 'developer', 'challenge']

chosen_word = random.choice(words)

guessed_letters = []  
tries = 6  
display_word = ['_' for _ in chosen_word]  

print("🎮 Welcome to Hangman Game!")
print("Guess the word!")

while tries > 0 and '_' in display_word:
    print("\nCurrent word: ", ' '.join(display_word))
    guess = input("Guess a letter: ").strip().lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❗ Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        print("✅ Correct guess!")

        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display_word[i] = guess
    else:
        tries -= 1
        print(f"❌ Wrong guess. You have {tries} tries left.")

# Game Result
if '_' not in display_word:
    print("\n🎉 Congratulations! You guessed the word:", chosen_word)
else:
    print("\n💀 Game Over! The word was:", chosen_word)
