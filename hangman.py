import random

words = ["python", "hangman", "coding", "developer", "script"]
word = random.choice(words)
guessed = []
attempts = 6

print("🎮 Hangman Game")
while attempts > 0:
    display = [letter if letter in guessed else "_" for letter in word]
    print(" ".join(display))
    if "_" not in display:
        print("🎉 You won!")
        break
    guess = input("Guess a letter: ").lower()
    if guess in guessed:
        print("Already guessed!")
    elif guess in word:
        guessed.append(guess)
        print("Correct!")
    else:
        guessed.append(guess)
        attempts -= 1
        print(f"Wrong! Attempts left: {attempts}")
else:
    print(f"❌ Game over! The word was: {word}")