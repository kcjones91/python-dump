vowels = input("Enter a word: ").lower()

for vowel in vowels:
    if vowel in "aeiou":
        print(f"{vowel}")