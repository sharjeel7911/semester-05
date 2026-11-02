# %%
# TASK 1
# Given a list with duplicate elements, write a function to remove duplicates and return the same list with unique elements.
def remove_duplicates(lst: list) -> list:
    return list(dict.fromkeys(lst))


numbers = [1, 2, 3, 2, 4, 1, 5]
print(remove_duplicates(numbers))

# ====================================================================================================


#
# TASK 2
# Given a dictionary, write a function that takes a string as an input and returns a dictionary with words as keys and their frequencies as values.
def word_frequency(text: str) -> dict:
    words = text.split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency


text = "apple banana apple orange banana apple"
print(word_frequency(text))


# ====================================================================================================

# TASK 3
# Given two tuples, concatenate them to form a new tuple.


def concatenate_tuples(t1: tuple, t2: tuple) -> tuple:
    return t1 + t2


tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

print(concatenate_tuples(tuple1, tuple2))

# ====================================================================================================


# TASK 4
# Given a list of integers, write a function that returns the sum of all even numbers in the list.
def sum_even(numbers: list) -> int:
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total


numbers = [1, 2, 3, 4, 5, 6, 8]
print(sum_even(numbers))

# ====================================================================================================
# TASK 5


# Write a function that takes a string as input and returns True if it is a palindrome (ignoring case and spaces), otherwise returns False.
def is_palindrome(text: str) -> bool:
    text = text.replace(" ", "").lower()
    return text == text[::-1]


print(is_palindrome("Madam"))
print(is_palindrome("nurses run"))
print(is_palindrome("Hello"))
