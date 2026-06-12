import random

# Step 1: Word list
words = ["apple", "banana", "grapes", "mango", "peach"]

# Step 2: Choose random word
word = random.choice(words)

# Step 3: Initialize
guessed = ["_"] * len(word)
attempts = 6
guessed_letters = []

print("🎮 Welcome to Hangman Game!")

# Step 4: Game loop
while attempts > 0 and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    print("Attempts left:", attempts)
    print("Guessed letters:", guessed_letters)

    guess = input("Enter a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("⚠️ Already guessed!")
        continue

    guessed_letters.append(guess)

    # Check correct or wrong
    if guess in word:
        print("✅ Correct!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        print("❌ Wrong!")
        attempts -= 1

# Step 5: Result
if "_" not in guessed:
    print("\n🎉 You Win! The word is:", word)
else:
    print("\n💀 You Lose! The word was:", word)
