# %%
# Exercise 1.1
print(type(250))
print(type(28 % 5))
print(type(2.5e2))
print(type(3e5))
print(type(3 * 10**5))

print(
    "First:", 20 + 35 * 2, type(20 + 35 * 2)
)  # in this case, the multiplication is evaluated first
print(
    "Second:", (20 + 35) * 2, type((20 + 35) * 2)
)  # in this case, the addition is evaluated first
print()
print("First:", 2 / 3 * 3, type(2 / 3 * 3))  # single / means floating point division
print("Second:", 2 // 3 * 3, type(2 // 3 * 3))  # double // means integer division
print()
print(
    "First:", 20 + 35 * 2, type(20 + 35 * 2)
)  # this will multiply 35 by 2, then add 20 to the result
print(
    "Second:", ((25 - 5) * 2) - 9, type(((25 - 5) * 2) - 9)
)  # this will first subtract 25 from 5, then multiply by 2, then subtract 9
print(
    "Third:", 25 - ((5 * 2) - 9), type(25 - ((5 * 2) - 9))
)  # this will first multiply 5 by 2, then subtract 9, then subtract the result from 25

# ====================================================================================================


# %%
# Exercise 1.2
def sundaes(flavors: list[str], sauces: list[str]) -> int:
    count = 0
    for i in flavors:
        for j in sauces:
            count += 1
            # print(flavor + " ice cream sundae with " + sauce + " sauce")
            print(f"{i} ice cream sundae with {j} sauce")
    return count


flavors = ["vanilla", "chocolate", "strawberry", "pistacchio"]
sauces = ["caramel", "butterscotch", "chocolate"]
count = sundaes(flavors, sauces)
print()
print(f"Total sundaes: {count}")

# ====================================================================================================


# %%
# Exercise 1.3
def triangle():
    value = 1
    row = 1
    while row <= 10:
        column = 1
        while column <= row:
            if column != row:
                print(
                    value, " ", sep="", end=""
                )  # sep is the separator between values, end is what to print at the end of the line
            else:
                print(value)
            value = value + 1
            column = column + 1
        row = row + 1


triangle()

# ====================================================================================================


# %%
# Exercise 1.4
# 1. Write the following functions:
# cube(n), which takes in a number and returns its cube.
def cube(n: int | float) -> int | float:
    return n**3


print("Cube:", cube(4), "\n")


# factorial(n), which takes in a non-negative integer n and returns n!, which is the product of the integers from 1 to n
def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print("Factorial:", factorial(5), "\n")


# count_pattern(pattern lst), which counts the number of times a certain pattern of symbols appears in a list, including overlaps.
# So count_pattern( ('a', 'b'), ('a','b', 'c', 'e', 'b', 'a', 'b', 'f')) should return 2
# and count_pattern(('a', 'b', 'a'), ('g', 'a', 'b', 'a', 'b', 'a','b', 'a')) should return 3.
def count_pattern(pattern: tuple, lst: tuple) -> int:
    count = 0
    for i in range(len(lst) - len(pattern) + 1):
        if lst[i : i + len(pattern)] == pattern:
            count += 1
    return count


print(
    "Count pattern:",
    count_pattern(("a", "b"), ("a", "b", "c", "e", "b", "a", "b", "f")),
)
print(
    "Count pattern:",
    count_pattern(("a", "b", "a"), ("g", "a", "b", "a", "b", "a", "b", "a")),
)
print()


# Write a python program to print the multiplication table for the given number?
def print_multiplication_table(n: int) -> None:
    for i in range(1, 10 + 1):
        print(f"{i} * {n} = {i * n}", end="\n")
    print()


print_multiplication_table(9)


# Write a python program to implement Simple Calculator program? (+, -, / ,*)
def simple_calculator(a: int | float, b: int | float, operator: str) -> int | float:
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b
    else:
        raise ValueError("Invalid operator")


print("Simple calculator:", simple_calculator(5, 3, "+"), "\n")


# Write a python program to sort the sentence in alphabetical order?
def sort_sentence(sentence: str) -> str:
    words = sentence.split()
    words.sort()
    return " ".join(words)


print("Sorted sentence:", sort_sentence("world hello python apple"), "\n")


# %%
# 2. Write a Python class to convert an integer to a roman numeral.
class IntegerToRoman:
    def __init__(self, num: int):
        self.num = num

    def convert_int_to_roman(self) -> str:
        roman_numerals = {
            1000: "M",
            500: "D",
            100: "C",
            50: "L",
            10: "X",
            5: "V",
            1: "I",
        }

        result = ""
        for value, numeral in roman_numerals.items():
            while self.num >= value:
                result += numeral
                self.num -= value

        return result


number = IntegerToRoman(8)
print("Roman numeral:", number.convert_int_to_roman())


# %%
# 3. Write a Python class to find a pair of elements (indices of the two numbers) from a given array
# whose sum equals a specific target number. Input: numbers= [10,20,10,40,50,60,70], target=50
# Output: 3, 4
class FindPair:
    def __init__(self, numbers: list[int], target: int) -> None:
        self.numbers = numbers
        self.target = target

    def find_pair(self) -> tuple[int, int]:
        seen = {}
        for i, num in enumerate(self.numbers):
            complement = self.target - num
            if complement in seen:
                return seen[complement], i
            seen[num] = i
        return -1, -1


numbers = [10, 20, 10, 40, 50, 60, 70]
target = 50

pair = FindPair(numbers, target)
print("Indices:", pair.find_pair())
