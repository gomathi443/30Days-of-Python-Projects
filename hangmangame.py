import random
words = '''apple banana mango strawberry orange grape pineapple apricot lemon coconut 
watermelon cherry papaya berry peach lychee muskmelon'''.split()
word = random.choice(words)
word_letters = set(word)  # Unique letters in the word
guessed_letters = set()
chances = len(word) + 3
print("🎯 HANGMAN GAME - GUESS THE FRUIT NAME 🎯")
print("HINT: It's a type of fruit.")
print("Word: ", ' '.join(['_' for _ in word]))
while chances > 0:
    print("\n🔎 Letters guessed so far:", ' '.join(sorted(guessed_letters)))
    print(f"💡 Remaining chances: {chances}")
    guess = input("👉 Enter a letter: ").lower()
    if not guess.isalpha() or len(guess) != 1:
        print("❌ Please enter a SINGLE LETTER (A-Z only).")
        continue
    if guess in guessed_letters:
        print("⚠️ You've already guessed that letter.")
        continue
    guessed_letters.add(guess)
    if guess in word_letters:
        print("✅ Good job! You found a correct letter.")
        word_letters.remove(guess)
    else:
        print("❌ Oops! Wrong guess.")
        chances -= 1
    current_status = [letter if letter in guessed_letters else '_' for letter in word]
    print("Word: ", ' '.join(current_status))
    if not word_letters:
        print("\n🎉 Congratulations! You guessed the word:", word.upper())
        break
else:
    print("\n💀 Game Over! You ran out of chances.")
    print("The word was:", word.upper())
