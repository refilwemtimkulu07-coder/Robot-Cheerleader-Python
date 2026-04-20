# Step 1 — Get the word
word = input("Enter your favourite word: ")

# Convert word to uppercase (for finale)
word_upper = word.upper()

# Step 2 — Cheer each letter
for letter in word_upper:
    
    # Check if the letter is a vowel
    if letter in ["A", "E", "I", "O", "U"]:
        print(f"Give me an {letter}!")
    else:
        print(f"Give me a {letter}!")

# Step 3 — Grand Finale
print(f"What does it say????? {word_upper}!!!!!!")
