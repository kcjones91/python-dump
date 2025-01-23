sentence = input("Enter a sentence: ")
vowel_count = 0
vowels_found = ""

for char in sentence:
    if char.lower() in "aeiou":
        vowel_count += 1
        vowels_found += char
        
print(f"Number of vowels: {vowel_count}")
print(f"Vowels {vowels_found}")

