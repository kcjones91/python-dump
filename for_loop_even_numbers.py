# Noob lesson learned int is not iterable
# https://www.freecodecamp.org/news/int-object-is-not-iterable-python-error-solved/
number = int(input("Enter a number: "))

for i in range(number):
    if i % 2 == 0:
        print(f"Even: {i}")