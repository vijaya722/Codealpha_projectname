import random

# Step 1: Word list
words = ["apple", "banana", "grapes", "mango", "peach"]

# Step 2: Choose random word
word = random.choice(words)

# Step 3: Create blank display
guessed = ["_"] * len(word)

attempts = 6
guessed_letters = []

print("🎮 Welcome to Hangman Game!")

# Step 4: Game loop
while attempts > 0 and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    print("Attempts left:", attempts)

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct!")
        # Fill the blanks
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        print("Wrong!")
        attempts -= 1

# Step 5: Result
if "_" not in guessed:
    print("\n You Won! The word is:", word)
else:
    print("\n You Lost! The word was:", word)