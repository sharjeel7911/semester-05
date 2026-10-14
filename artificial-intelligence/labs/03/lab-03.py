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
# 	1. A list of the squares of the numbers from 1 to 20.
# 	2. A list of the multiples of 3 between 1 and 50.
# 	3. A list of the lengths of the words in ["python", "is", "easy", "to", "learn"] .

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
# 	1. Write five student names to a file names.txt , one per line.
# 	2. Read the file and print each name with a number, e.g. 1. Ali .
# 	3. Append one more name to the file.
# 	4. Read the file again and print how many names it contains.


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
    names.append(name)
    write_file(names)

read_file()
append_file(input("Enter one more student name to append: "))
read_file()

# =====================================================================================================

# %%
# Exercise 3.8
# Read a sentence from the user. Use split() and a dictionary to
# count how many times each word appears, then print the result. For example, "the cat
# saw the dog" gives the: 2 , cat: 1 , saw: 1 , dog: 1 .


def word_count() -> None:
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    words = [word.lower() for word in words]
    word_dict = {}
    for word in words:
        word_dict[word] = word_dict.get(word, 0) + 1
    print("Word count:")
    for word, count in word_dict.items():
        print(f"{word}: {count}")


word_count()

# ====================================================================================================

# %%
# Exercise 3.9
# Read a full name from the user (e.g. ali raza ). Remove the extra spaces, then print it
# with the first letter of each word capitalised (use strip() and title() ), its length, and
# the name in upper case.


def format_name() -> None:
    full_name = input("Enter your full name: ")
    formatted_name = (
        full_name.strip().title()
    )  # strip spaces from start and end and capitalize first letter of each word
    formatted_name = "".join(
        formatted_name.split()
    )  # or formatted_name = formatted_name.replace("  ", "")
    name_length = len(formatted_name)
    upper_case_name = formatted_name.upper()

    print(f"Formatted Name: {formatted_name}")
    print(f"Length of Name: {name_length}")
    print(f"Name in Upper Case: {upper_case_name}")


format_name()

# ====================================================================================================

# %%
# Exercise 3.10
# Read a sentence from the user and print:
# 	1. The number of words.
# 	2. The number of characters, with and without spaces.
# 	3. The sentence with the words in reverse order (use split() , reverse() and join() ).
# 	4. The longest word in the sentence.


def analyze_sentence() -> None:
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    num_words = len(words)
    num_chars_with_spaces = len(sentence)
    num_chars_without_spaces = len(sentence.replace(" ", ""))
    reversed_sentence = " ".join(reversed(words))
    longest_word = max(words, key=len)

    print(f"Number of words: {num_words}")
    print(f"Number of characters (with spaces): {num_chars_with_spaces}")
    print(f"Number of characters (without spaces): {num_chars_without_spaces}")
    print(f"Sentence with words in reverse order: {reversed_sentence}")
    print(f"Longest word in the sentence: {longest_word}")


analyze_sentence()

# ====================================================================================================

# %%
# Exercise 3.11
# Write a function reverse_string(text) that returns a string reversed, first using a for
# loop and then using slicing ( text[::-1] ). Check that both give the same result for
# "python" .


def reverse_string(text: str) -> tuple[str, str]:
    reversed_for_loop = ""
    for char in text:
        reversed_for_loop = char + reversed_for_loop
    reversed_slicing = text[::-1]
    return reversed_for_loop, reversed_slicing


res = reverse_string("python")
print("For loop:", res[0], " Slicing:", res[1])

# ====================================================================================================

# %%
# Exercise 3.12
# Write a function count_characters(text) that returns a dictionary with the number of
# times each character appears. For example, count_characters("banana") returns {'b':
# 1, 'a': 3, 'n': 2} .


def count_characters(text: str) -> dict[str, int]:
    char_count = {}
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count


res = count_characters("banana")
print(res)


# =====================================================================================================

# %%
# Exercise 3.13
# Temperature converter. Show a menu with two options: Celsius to Fahrenheit ( F = C *
# 9/5 + 32 ) and Fahrenheit to Celsius. Keep showing the menu in a while loop until the
# user chooses Exit. Use try / except for invalid numbers and print results with one
# decimal place using an f-string.


def temperature_converter() -> None:
    while True:
        print("\nTemperature Converter Menu:")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == "1":
            try:
                celsius = float(input("Enter temperature in Celsius: "))
                fahrenheit = celsius * 9 / 5 + 32
                print(f"{celsius:.1f}°C is {fahrenheit:.1f}°F")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == "2":
            try:
                fahrenheit = float(input("Enter temperature in Fahrenheit: "))
                celsius = (fahrenheit - 32) * 5 / 9
                print(f"{fahrenheit:.1f}°F is {celsius:.1f}°C")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


temperature_converter()

# ====================================================================================================

# %%
# Exercise 3.14
# Write a program that asks the user for a positive integer n and prints:
# 	1. All the even numbers from 1 to n .
# 	2. The sum of all the numbers from 1 to n .
# 	3. The factorial of n using a while loop (compare it with math.factorial(n) ).


def positive_integer_operations() -> None:
    try:
        n = int(input("Enter a positive integer: "))
        if n <= 0:
            print("Please enter a positive integer.")
            return

        # 1. All the even numbers from 1 to n
        even_numbers = [x for x in range(1, n + 1) if x % 2 == 0]
        print(f"Even numbers from 1 to {n}: {even_numbers}")

        # 2. The sum of all the numbers from 1 to n
        total_sum = sum(range(1, n + 1))
        print(f"Sum of all numbers from 1 to {n}: {total_sum}")

        # 3. The factorial of n using a while loop
        factorial = 1
        i = 1
        while i <= n:
            factorial *= i
            i += 1
        print(f"Factorial of {n} using while loop: {factorial}")

        # Compare with math.factorial(n)
        import math

        math_factorial = math.factorial(n)
        print(f"Factorial of {n} using math.factorial: {math_factorial}")

    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")


positive_integer_operations()

# ====================================================================================================

# %%
# Exercise 3.15
# Write a function is_prime(n) that returns True if n is prime. Then use a list
# comprehension to build a list of all prime numbers between 1 and 100 and print it.


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


primes = [n for n in range(1, 101) if is_prime(n)]
print(f"Prime numbers between 1 and 100: {primes}")

# ====================================================================================================

# %%
# Exercise 3.16
# Print the multiplication tables of 2 to 5 side by side using nested for loops, formatted like
# this:
# 2 x 1 = 2  3 x 1 = 3  4 x 1 = 4  5 x 1 = 5
# 2 x 2 = 4  3 x 2 = 6  4 x 2 = 8  5 x 2 = 10
# Continue up to 10.


def multiplication_tables() -> None:
    for i in range(1, 11):
        row = ""
        for j in range(2, 6):
            row += f"{j} x {i} = {j * i}\t"
        print(row.strip())


multiplication_tables()


# ====================================================================================================

# %%
# Exercise 3.17
# Write a program that generates a list of 10 random integers between 1 and 100 using
# random.randint() . Then print:
# 	1. The list, the largest and the smallest value (use max() and min() ).
# 	2. The sum and the average.
# 	3. The list sorted in ascending and descending order.
# 	4. Only the numbers greater than the average (use a list comprehension).

import random


def random_integer_operations() -> None:
    random_numbers = [
        random.randint(1, 100) for _ in range(10)
    ]  # "_" is used as a throwaway variable since we don't need the index
    print(f"Random numbers: {random_numbers}")

    # 1. Largest and smallest value
    largest = max(random_numbers)
    smallest = min(random_numbers)
    print(f"Largest value: {largest}, Smallest value: {smallest}")

    # 2. Sum and average
    total_sum = sum(random_numbers)
    average = total_sum / len(random_numbers)
    print(f"Sum: {total_sum}, Average: {average:.2f}")

    # 3. Sorted in ascending and descending order
    sorted_asc = sorted(random_numbers)
    sorted_desc = sorted(random_numbers, reverse=True)
    print(f"Sorted ascending: {sorted_asc}")
    print(f"Sorted descending: {sorted_desc}")

    # 4. Numbers greater than the average
    numbers_greater_than_average = [num for num in random_numbers if num > average]
    print(f"Numbers greater than the average: {numbers_greater_than_average}")


random_integer_operations()


# ====================================================================================================

# %%
# Exercise 3.18
# Student marks file.
# 	1. Create a file marks.txt where each line has a name and a mark separated by a
# 	comma, e.g. Ali,85 . Enter at least five students.
# 	2. Read the file and store the data in a dictionary ( name: mark ). Use split(",") and
# 	int() .
# 	3. Print each student's name and mark, the class average, and the name of the student
# 	with the highest mark.
# 	4. Write the names of the students who scored below the average to a new file
# 	below_average.txt .


def write_marks_file() -> None:
    students = []
    for i in range(5):
        name = input(f"Enter name of student {i + 1}: ")
        mark = input(f"Enter marks of student {i + 1}: ")
        students.append(f"{name},{mark}\n")
    with open("marks.txt", "w") as f:
        f.writelines(students)


def read_marks_file() -> dict[str, int]:
    marks_dict = {}
    with open("marks.txt", "r") as f:
        for line in f:
            name, mark = line.strip().split(",")
            marks_dict[name] = int(mark)
    return marks_dict


def analyze_marks(marks_dict: dict[str, int]) -> None:
    total_marks = sum(marks_dict.values())
    average_mark = total_marks / len(marks_dict)
    highest_student = max(marks_dict, key=marks_dict.get)

    print("Student Marks:")
    for name, mark in marks_dict.items():
        print(f"{name}: {mark}")
    print(f"Class Average: {average_mark:.2f}")
    print(f"Highest Mark: {highest_student} with {marks_dict[highest_student]}")

    below_average_students = [
        name for name, mark in marks_dict.items() if mark < average_mark
    ]
    with open("below_average.txt", "w") as f:
        for student in below_average_students:
            f.write(student + "\n")


write_marks_file()
marks_dict = read_marks_file()
analyze_marks(marks_dict)

# ====================================================================================================

# %%
# Exercise 3.19
# Password checker. Write a function check_password(password) that returns True only
# if the password has at least 8 characters, contains at least one digit, and contains at least
# one upper case letter. (Hint: use isdigit() and isupper() inside a loop.) Keep asking
# the user for a password until a valid one is entered.


def check_password(password: str) -> bool:
    if len(password) < 8:
        return False
    has_digit = any(char.isdigit() for char in password)
    has_upper = any(char.isupper() for char in password)
    return has_digit and has_upper


while True:
    password = input("Enter a password: ")
    if check_password(password):
        print("Password is valid.")
        break
    else:
        print(
            "Password must be at least 8 characters long, contain at least one digit, and contain at least one upper case letter. Please try again."
        )

# ====================================================================================================

# %%
# Exercise 3.20
# Mini contact book. Use a dictionary to store contacts ( name: phone number ) and show a
# menu in a while loop with these options: add a contact, search for a contact, delete a
# contact, show all contacts, and exit. Save the contacts to a file contacts.txt when the
# user exits, and load them from the file when the program starts.


class ContactBook:
    def __init__(self):
        self.contacts = {}
        self.load_contacts()

    def load_contacts(self):
        try:
            with open("contacts.txt", "r") as f:
                for line in f:
                    line = line.strip()
                    if line and "," in line:
                        name, phone = line.split(",", 1)
                        self.contacts[name.lower()] = (name, phone)
        except FileNotFoundError:
            pass

    def save_contacts(self):
        with open("contacts.txt", "w") as f:
            for name, phone in self.contacts.values():
                f.write(f"{name},{phone}\n")

    def add_contact(self):
        name = input("Enter contact name: ")
        phone = input("Enter contact phone number: ")
        self.contacts[name.lower()] = (name, phone)
        print(f"Contact {name} added.")

    def search_contact(self):
        name = input("Enter contact name to search: ").strip().lower()
        if name in self.contacts:
            print(f"{name}: {self.contacts[name]}")
        else:
            print(f"Contact {name} not found.")

    def delete_contact(self):
        name = input("Enter contact name to delete: ").strip().lower()
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} deleted.")
        else:
            print(f"Contact {name} not found.")

    def show_all_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for name, phone in self.contacts.items():
                print(f"{name}: {phone}")

    def run(self):
        while True:
            print("\nContact Book Menu:")
            print("1. Add a contact")
            print("2. Search for a contact")
            print("3. Delete a contact")
            print("4. Show all contacts")
            print("5. Exit")
            choice = input("Choose an option (1-5): ")

            if choice == "1":
                self.add_contact()
            elif choice == "2":
                self.search_contact()
            elif choice == "3":
                self.delete_contact()
            elif choice == "4":
                self.show_all_contacts()
            elif choice == "5":
                self.save_contacts()
                print("Exiting the program. Contacts saved.")
                break
            else:
                print("Invalid choice. Please select a valid option.")


contact = ContactBook()
contact.run()
