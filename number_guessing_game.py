import random

# 🎲 Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

print("Welcome to the Number Guessing Game with Clues!")
print("I'm thinking of a number between 1 and 100. Can you guess it?")

# 🔍 Give some clues before the guessing starts
print("\nHere are some clues to help you out:")
print(f"- The number is {'even' if secret_number % 2 == 0 else 'odd'}.")
if secret_number % 5 == 0:
    print("- It's divisible by 5.")
elif secret_number % 3 == 0:
    print("- It's divisible by 3.")
else:
    print("- It's not divisible by 3 or 5.")

if secret_number > 50:
    print("- It's greater than 50.")
else:
    print("- It's 50 or less.")

if secret_number % 10 in [1, 9]:
    print("- It's close to a multiple of 10.")

# 🎮 Start the guessing loop
while True:
    guess = int(input("\nEnter your guess: "))

    if guess < secret_number:
        print("Too low! Try a higher number.")
    elif guess > secret_number:
        print("Too high! Try a lower number.")
    else:
        print("🎉 Boom! You nailed it!")
        break
