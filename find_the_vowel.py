# Working the muscle for common loop patterns

word = input("Enter the word that you would like to find the vowels \n")


for letter in word:
    if letter in "aeiou":
        letter.lower()
        vowel = letter
        # print(f"Here is your vowel {vowel}")
        break

print(f"THe first vowel is: {vowel}")

