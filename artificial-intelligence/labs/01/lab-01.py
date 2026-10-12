# %%
# ===================================
# ========== Exercise 1.1 ==========
# ===================================

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
# ===================================
# ========== Exercise 1.1 ==========
# ===================================


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
# ===================================
# ========== Exercise 1.1 ==========
# ===================================


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
# ===================================
# ========== Exercise 1.1 ==========
# ===================================


# 1. Write the following functions:
# cube(n), which takes in a number and returns its cube.
def cube(n: int | float) -> int | float:
    return n**3


print("Cube:", cube(4), "\n")

# ====================================================================================================


# %%
# factorial(n), which takes in a non-negative integer n and returns n!, which is the product of the integers from 1 to n
def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print("Factorial:", factorial(5), "\n")

# ====================================================================================================


# %%
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

# ====================================================================================================


# %%
# Write a python program to print the multiplication table for the given number?
def print_multiplication_table(n: int) -> None:
    for i in range(1, 10 + 1):
        print(f"{i} * {n} = {i * n}", end="\n")
    print()


print_multiplication_table(9)

# ====================================================================================================


# %%
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

# ====================================================================================================


# %%
# Write a python program to sort the sentence in alphabetical order?
def sort_sentence(sentence: str) -> str:
    words = sentence.split()
    words.sort()
    return " ".join(words)


print("Sorted sentence:", sort_sentence("world hello python apple"), "\n")

# ====================================================================================================


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

# ====================================================================================================


# %%
# 3. Write a Python class to find a pair of elements (indices of the two numbers) from a given array
# whose sum equals a specific target number. Input: numbers = [10,20,10,40,50,60,70], target = 50
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

# ====================================================================================================

# %%
# 4. Write a Python class to find the three elements that sum to zero from a set of n real numbers.
# Input array : [-25, -10, -7, -3, 2, 4, 8, 10] Output : [[-10, 2, 8], [-7, -3, 10]]


class FindTriplet:
    def __init__(self, numbers: list[int]) -> None:
        self.numbers = numbers

    def find_triplet(self) -> list[list[int]]:
        triplets = []
        for i in range(len(self.numbers) - 2):
            for j in range(i + 1, len(self.numbers) - 1):
                for k in range(j + 1, len(self.numbers)):
                    if self.numbers[i] + self.numbers[j] + self.numbers[k] == 0:
                        triplets.append(
                            [self.numbers[i], self.numbers[j], self.numbers[k]]
                        )
        return triplets


numbers = [-25, -10, -7, -3, 2, 4, 8, 10]
triplet = FindTriplet(numbers)
print("Triplet:", triplet.find_triplet())

# ====================================================================================================

# %%
# 5. Write a Python class to reverse a string word by word.
# Input string : 'hello .py'
# Expected Output : '.py hello'


class ReverseString:
    def __init__(self, string: str) -> None:
        self.string = string

    def reverse_by_word(self) -> str:
        return " ".join(self.string.split()[::-1])

    def reverse_by_character(self) -> str:
        return self.string[::-1]


string = "hello .py"
reverser = ReverseString(string)
print("Reversed by word:", reverser.reverse_by_word())
print("Reversed by character:", reverser.reverse_by_character())

# ====================================================================================================

# %%
# 6. Count the numbers of characters in the string
# a. Read the string.
# b. Count the characters
# c. Display the result


def count_chars(string: str) -> int:
    return len(string)


print("Number of characters:", count_chars(string))

# ====================================================================================================

# %%
# 7. Addition of two square matrices.
# a. Create a lists to read matrix elements
# b. Read the elements of to matrices add the elements
# c. Store the result in third matrix.
# d. Repeat steps 2 and 3 till the addition of all elements


def add_matrices(matrix1: list[list[int]], matrix2: list[list[int]]) -> list[list[int]]:
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result


matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1], [12, 11, 10]]
print("Matrix addition:", add_matrices(matrix1, matrix2))

# ====================================================================================================

# %%
# 8. Display the result Multiplication of two matrices
# a. Create a list to read matrix elements
# b. Read the elements of two matrices, multiply the elements
# c. Store the result in third matrix.
# d. Repeat steps 2 and 3 till the multiplication of all elements
# e. Display the result.


def multiply_matrices(
    matrix1: list[list[int]], matrix2: list[list[int]]
) -> list[list[int]]:
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            cell = 0
            for k in range(len(matrix2)):
                cell += matrix1[i][k] * matrix2[k][j]
            row.append(cell)
        result.append(row)
    return result


matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
matrix2 = [[9, 8, 7, 6], [5, 4, 3, 2], [1, 12, 11, 10]]
print("Matrix multiplication:", multiply_matrices(matrix1, matrix2))

# ====================================================================================================

# %%
# 9. Write a function called calculator. It should take the following parameters: two numbers, an
# arithmetic operation (which can be addition, subtraction, multiplication or division and is addition
# by default), and an output format (which can be integer or floating point, and is floating point by
# default). Division should be floating-point division. The function should perform the requested
# operation on the two input numbers, and return a result in the requested format (if the format is
# integer, the result should be rounded and not just truncated). Raise exceptions as appropriate if
# any of the parameters passed to the function are invalid.


def calculator(
    num1: float, num2: float, operation: str = "add", output_format: str = "float"
) -> float | int:
    if operation not in ["add", "sub", "mul", "div"]:
        raise ValueError("Invalid operation")
    if output_format not in ["float", "int"]:
        raise ValueError("Invalid output format")
    result = 0
    if operation == "add":
        result = num1 + num2
    elif operation == "sub":
        result = num1 - num2
    elif operation == "mul":
        result = num1 * num2
    elif operation == "div":
        result = num1 / num2
    if output_format == "int":
        return round(result)
    return result


print("Division:", calculator(3.5, 2.5, "div", "int"))
print("Division:", calculator(3.5, 2.5, "div", "float"))
print("Subtraction:", calculator(3.5, 2.5, "sub", "float"))
print("Multiplication:", calculator(3.5, 2.5, "mul", "float"))
print("Addition:", calculator(3.5, 2.5, "add", "float"))

# ====================================================================================================

# %%
# 10. Create a class called Numbers, which has a single class attribute called MULTIPLIER, and a
# constructor which takes the parameters x and y (these should all be numbers).
# a. Write a method called add which returns the sum of the attributes x and y.
# b. Write a class method called multiply, which takes a single number parameter a and
# returns the product of a and MULTIPLIER.
# c. Write a static method called subtract, which takes two number parameters, b and c, and
# returns b - c.
# d. Write a method called value which returns a tuple containing the values of x and y. Make
# this method into a property, and write a setter and a deleter for manipulating the values
# of x and y.


class Numbers:
    # Class attribute
    MULTIPLIER = 5.0

    def __init__(self, x: float | int, y: float | int):
        self._x = x
        self._y = y

    def add(self) -> float | int:
        return self._x + self._y

    # class method is a method that operates on the class itself, not on instances of the class.
    @classmethod
    def multiply(cls, a: float | int) -> float | int:
        return a * cls.MULTIPLIER

    # static method is a method that does not operate on the class or its instances.
    @staticmethod
    def subtract(b: float | int, c: float | int) -> float | int:
        return b - c

    # property is a way to define a getter, setter, and deleter for a class attribute.
    @property
    def value(self) -> tuple[float | int, float | int]:
        return (self._x, self._y)

    # value setter
    @value.setter
    def value(self, new_values: tuple[float | int, float | int]) -> None:
        if not isinstance(new_values, (tuple, list)) or len(new_values) != 2:
            raise ValueError("Value must be a sequence of two numbers: (x, y)")
        self._x, self._y = new_values

    # value deleter
    @value.deleter
    def value(self) -> None:
        self._x = 0
        self._y = 0


# Example Usage & Testing
nums = Numbers(10, 4)

# a. Instance method
print("Add:", nums.add())  # 14

# b. Class method
print("Multiply:", Numbers.multiply(3))  # 15.0

# c. Static method
print("Subtract:", Numbers.subtract(10, 3))  # 7

# d. Property getter
print("Value:", nums.value)  # (10, 4)

# d. Property setter
nums.value = (20, 8)
print("New Value:", nums.value)  # (20, 8)
# %
# d. Property deleter
del nums.value
print("Deleted Value:", nums.value)  # (0, 0)
