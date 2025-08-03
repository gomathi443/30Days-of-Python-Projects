import random
num = str(random.randrange(1000, 10000))
attempts = 0
max_attempts = 10
guessed_numbers = []
print("🔢 Welcome to Mastermind!")
print("Try to guess the 4-digit number. You have", max_attempts, "tries.\n")
while attempts < max_attempts:
    guess = input(f"Attempt {attempts + 1}: Enter your 4-digit guess: ")
    if not guess.isdigit() or len(guess) != 4:
        print("❗ Please enter a valid 4-digit number.\n")
        continue
    if guess in guessed_numbers:
        print("⚠️ You've already guessed that number. Try something else.\n")
        continue
    guessed_numbers.append(guess)
    attempts += 1
    if guess == num:
        print("🎉 Great! You guessed the number in", attempts, "tries! You're a Mastermind!")
        break
    feedback = []
    correct_pos = 0
    wrong_pos = 0
    for i in range(4):
        if guess[i] == num[i]:
            correct_pos += 1
            feedback.append("✅")
        elif guess[i] in num:
            wrong_pos += 1
            feedback.append("🔄")
        else:
            feedback.append("❌")
    print("Feedback:", ' '.join(feedback))
    print(f"✅ Correct digit & place: {correct_pos} | 🔄 Correct digit, wrong place: {wrong_pos} | ❌ Incorrect: {4 - correct_pos - wrong_pos}\n") 
else:
    print("❌ You've used all your attempts. The correct number was:", num)
    print("Better luck next time!")
