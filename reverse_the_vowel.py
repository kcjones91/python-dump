word = input("Enter a word: ")
no_vowels = ""

for letter in word:
    if letter in "aeiouAEIOU":
        continue
    no_vowels += letter

print(f"Word without the vowels: {no_vowels}")