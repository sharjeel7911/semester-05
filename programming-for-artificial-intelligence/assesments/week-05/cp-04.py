# %%
# Task 1
# Write a script that maintains a global variable call_count = 0. Create a function execute_task() that
# increments this global counter every time it is called.
#   Without passing the variable as an argument, ensure the function modifies the global instance
#   rather than creating a local one.
#   Why is this pattern generally avoided in large-scale AI pipelines?

call_count = 0


def execute_task() -> None:
    global call_count
    call_count += 1
    print("Task executed!")


execute_task()
execute_task()
execute_task()

print("Total calls:", call_count)
print("Var Value:", call_count)

# Global variables are generally avoided because:
# - Concurrency issues: Multiple processes or threads may modify the same counter, potentially causing incorrect results.
# - Debugging difficulties: Any function can modify the global variable, making the code harder to trace and debug.
# - Testing difficulties: The variable retains its value between function calls, potentially affecting test results.
# - Scalability: In distributed AI pipelines, different workers may run on separate machines, so a global variable cannot reliably maintain a shared count across all workers.
# Better approach: Use a class to maintain the counter as instance state, or use a dedicated shared counter or tracking service when multiple workers need to update it.

# ====================================================================================================

# %%
# Task 2
# Write a function math_operation(operator, *numbers) where:
# · operator is a string (e.g., "add", "mul").
# · *numbers collects any amount of numerical data.
# · If the operator is "add", return the sum. If "mul", return the product.
# Example: math_operation("mul", 2, 3, 4) should return 24.


def math_operation(operator: str, *numbers: tuple) -> float | int:
    if operator == "add":
        return sum(numbers)
    elif operator == "sub":
        if len(numbers) < 2:
            return "Subtraction requires at least two numbers"
        result = numbers[0]
        for num in numbers[1:]:
            result -= num
        return result
    elif operator == "mul":
        result = 1
        for num in numbers:
            result *= num
        return result
    elif operator == "div":
        if len(numbers) < 2:
            return "Division requires at least two numbers"
        result = numbers[0]
        for num in numbers[1:]:
            if num == 0:
                return "Division by zero is not allowed"
            result /= num
        return result
    else:
        return "Invalid operator"


print("Addition:", math_operation("add", 2, 3, 4))
print("Multiplication:", math_operation("mul", 2, 3, 4))
print("Subtraction:", math_operation("sub", 10, 3, 2, 99, 91))
print("Division:", math_operation("div", 20, 2, 2, 3))


# ====================================================================================================

# %%
# Task 3
# In Machine Learning, we often pass many settings to a model. Write a function
# print_config(model_name, **hyperparams) that:
# 1. Prints the model_name in uppercase.
# 2. Iterates through the **hyperparams and prints them in the format: [Setting Name] -> [Value].
# Example:
# print_config("RandomForest", n_estimators=100, max_depth=5, random_state=42)


def print_config(model_name: str, **hyperparams: dict) -> None:
    print("Model name:", model_name.upper())

    for setting, value in hyperparams.items():
        print(f"{setting} -> {value}")


print_config("RandomForest", n_estimators=100, max_depth=5, random_state=42)

# ====================================================================================================

# %%
# Task 4
# Create a function base_calculator(a, b, operation="sum"). Then, create a "wrapper" function
# called smart_wrapper(*args, **kwargs). The smart_wrapper should:
# 1. Print "Logging: Function call initiated."
# 2. Pass all received arguments and keyword arguments directly into base_calculator using the Unpacking (Splat) Operator.
# 3. Return the result of the calculation.


def base_calculator(a: float, b: float, operation: str = "sum") -> float | int | str:
    if operation == "sum":
        return a + b
    elif operation == "mul":
        return a * b
    elif operation == "sub":
        return a - b
    elif operation == "div":
        return a / b
    else:
        return "Invalid operation"


def smart_wrapper(*args: tuple, **kwargs: dict) -> float | int | str:
    print("Logging: Function call initiated.")
    return base_calculator(*args, **kwargs)


print(smart_wrapper(10, 5))
print(smart_wrapper(10, 5, operation="mul"))
print(smart_wrapper(a=10, b=5, operation="sub"))


# ====================================================================================================

# %%
# Task 5
# Implement a recursive function to navigate and "flatten" a deeply nested directory structure.
# Scenario: In large-scale AI datasets, metadata is often stored in complex, non-uniform formats. You are
# provided with a variable named files that represents a file system. This structure is a mix of:
# 1. Dictionaries: Representing folders (Keys are folder names, Values are content).
# 2. Lists: Representing a collection of multiple sub-folders or file groups.
# 3. Strings: Representing the actual filenames (the "leaves" of our tree).
#
# Task: Write a recursive function list_all_files(data) that traverses this entire structure. The function must:
# · Identify if the current object is a Dictionary, a List, or a String.
# · Recursively dive into dictionaries and lists until a string is found.
# · Print the name of every directory and the names of files found within, regardless of its depth.
# · Handle Empty Cases: Ensure the function does not crash if it encounters an empty list [] or an empty dictionary {}.
#
# Example:
# files = {
#     "docs": [
#     {"work": ["resume.pdf", "project.docx"]},
#     {"personal": [
#     {"pictures": ["photo.jpg", "vacation1.jpg", "vacation2.jpg"]},
#     {"videos": []}
#     ]},
#     "todo.txt", "logfile.csv",
#     {"downloads": []}
# ]
# # Expected Output:
# Directory: docs
# Directory: work
# -> File: resume.pdf
# -> File: project.docx
# Directory: personal
# Directory: pictures
# -> File: photo.jpg
# -> File: vacation1.jpg
# -> File: vacation2.jpg
# Directory: videos
# -> File: todo.txt
# -> File: logfile.csv
# Directory: downloads


def list_all_files(data: dict) -> None:
    if isinstance(data, dict):
        for directory, contents in data.items():
            print(f"Directory: {directory}")
            list_all_files(contents)

    elif isinstance(data, list):
        for item in data:
            list_all_files(item)

    elif isinstance(data, str):
        print(f"-> File: {data}")


files = {
    "docs": [
        {"work": ["resume.pdf", "project.docx"]},
        {
            "personal": [
                {"pictures": ["photo.jpg", "vacation1.jpg", "vacation2.jpg"]},
                {"videos": []},
            ]
        },
        "todo.txt",
        "logfile.csv",
        {"downloads": []},
    ]
}

list_all_files(files)
