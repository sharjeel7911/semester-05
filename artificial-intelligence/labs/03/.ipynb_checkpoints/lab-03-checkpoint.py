# %%
# Exercise 3.1

s = "Hello World"
print(s.upper())
print(s.lower())
print(s[0:5])
print(s[-1])
print(s.replace("World", "Python"))
print(s.split(" "))
print(len(s))
print(s.count("l"))
print(s.find("W"))

# ====================================================================================================

# %%
# Exercise 3.2
# Write a function count_vowels(text) that returns the number of vowels (a, e, i, o, u) in a
# string. For example, count_vowels("Artificial") returns 5.


def count_vowels(text: str) -> int:
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


string = "Artificial"
print(f"The number of vowels in '{string}' is: {count_vowels(string)}")

# ====================================================================================================

# %%
# Exercise 3.3
# Write a function is_palindrome(text) that returns True if a word reads the same
# forwards and backwards (e.g. "madam" ), otherwise False . Ignore upper/lower case.


def is_palindrome(text: str) -> bool:
    text = text.lower()
    return text == text[::-1]


word = "madam"
print(f"Is '{word}' a palindrome? {is_palindrome(word)}")

# ====================================================================================================

# %%
# Exercise 3.4
# Write a program that keeps asking the user for numbers using a while loop until the user
# types done . Then print the sum and the average of the numbers entered. Use
# try / except so that invalid input prints a message instead of crashing.


def sum_and_average() -> None:
    total = 0
    count = 0
    while True:
        user_input = input("Enter a number (or type 'e/E' to finish): ")
        if user_input.lower() == "e":
            break
        try:
            number = float(user_input)
            total += number
            count += 1
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    if count > 0:
        average = total / count
        print(f"Sum: {total}, Average: {average}")
    else:
        print("No numbers were entered.")


print("Welcome to the sum and average calculator!")
sum_and_average()

# ====================================================================================================

# %%
# Exercise 3.5
# Guessing game. Use random.randint(1, 20) to pick a secret number. Ask the user to
# guess in a while loop and print "Too high" or "Too low" after each guess. When the guess
# is right, stop the loop with break and print how many guesses it took.

import random


def guessing_game() -> None:
    secret_number = random.randint(1, 20)
    count = 0
    print("Welcome to the guessing game! Guess a number between 1 and 20.")

    while True:
        user_input = input("Enter your guess: ")
        try:
            guess = int(user_input)
            count += 1
            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print(
                    f"Congratulations! You've guessed the number {secret_number} in {count} guesses."
                )
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


guessing_game()

# ====================================================================================================

# %%
# Exercise 3.6
# Using list comprehensions, create:
# 1. A list of the squares of the numbers from 1 to 20.
# 2. A list of the multiples of 3 between 1 and 50.
# 3. A list of the lengths of the words in ["python", "is", "easy", "to", "learn"] .

squares = [x**2 for x in range(1, 21)]
multiples_of_3 = [x for x in range(1, 51) if x % 3 == 0]
words = ["python", "is", "easy", "to", "learn"]
lengths_of_words = [len(word) for word in words]

print("Squares of numbers from 1 to 20:", squares)
print("Multiples of 3 between 1 and 50:", multiples_of_3)
print("Lengths of the words:", lengths_of_words)

# ====================================================================================================

# %%
# Exercise 3.7
# 1. Write five student names to a file names.txt , one per line.
# 2. Read the file and print each name with a number, e.g. 1. Ali .
# 3. Append one more name to the file.
# 4. Read the file again and print how many names it contains.


def write_file(name: list[str]) -> None:
    with open("names.txt", "w") as f:
        for n in name:
            f.write(n + "\n")


def read_file() -> None:
    with open("names.txt", "r") as f:
        names = f.readlines()
        for i, name in enumerate(names, start=1):
            print(f"{i}. {name.strip()}")
        print(f"Total names: {len(names)}")


def append_file(name: str) -> None:
    with open("names.txt", "a") as f:
        f.write(name + "\n")


names = []
for i in range(5):
    name = input(f"Enter student name {i + 1}: ")
    write_file(names)

read_file()
append_file(input("Enter one more student name to append: "))
read_file()
