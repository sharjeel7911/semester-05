# %%
# Task - 01
# Write a Python function extract_high_multiples(matrix) that accepts a 2-d matrix
# The function must return a list of dictionaries.
# 1.
# Selection Criteria: An element should be included only if:
# 	· It is strictly greater than 5.
# 	· It is a multiple of 3.
# 2.
# Output Format: Each entry in the returned list must be a dictionary with the following keys:
# 	· 'row': The row index of the element.
# 	· 'col': The column index of the element.
# 	· 'val': The actual value of the element.
# 3.
# Constraint: You must implement the core logic using a single nested list comprehension
# (no multi-line for loops or .append() calls inside the function).


def extract_high_multiples(matrix: list[list[int]]) -> list[dict]:
    result = [
        {"row": i, "col": j, "val": val}
        for i, row in enumerate(matrix)
        for j, val in enumerate(row)
        if val > 5 and val % 3 == 0
    ]
    return result


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
extract_high_multiples(matrix)

# ====================================================================================================


# %%
# Task - 02
# The Goal: You have three lists: cities = ["Lahore", "Karachi", "Islamabad"], temps = [32, 35, 28],
# and humidity = [60, 70, 45].
# The Problem: Write a Python function summerize(cities, temps, humidity) using list
# comprehension and zip(). The function must return a list of strings that says:
# · “The weather in Lahore is 32C with 60% humidity.” (and so on for all cities).


def summerize(cities: list, temps: list, humidity: list) -> list[str]:
    result = [
        f"The weather in in {city} is {temp}C with {hum}% humidity."
        for city, temp, hum in zip(cities, temps, humidity)
    ]
    return result


cities = ["Lahore", "Karachi", "Islamabad"]
temps = [32, 35, 28]
humidity = [60, 70, 45]
summerize(cities, temps, humidity)

# ====================================================================================================


# %%
# Task - 03
# You have a list of messy emails: emails = [“ ALI@gooGle.coM”, “sara@Yahoo.com ”,
# “ AHMED@uCP.EdU.PK ”]
# Problem: Write a Python function sanitize(emails)using a list comprehension to strip the
# whitespace and make them all lowercase. The function must return the sanitized list.


def sanitize(emails: list) -> list:
    result = [i.strip().lower() for i in emails]
    return result


emails = [" ALI@gooGle.coM", "sara@Yahoo.com ", " AHMED@uCP.EdU.PK "]
sanitize(emails)

# ====================================================================================================

# %%
# Task - 04
# Given a list of temperatures in Celsius: c_temps = [0, 12, 34, 100, -5, 25]
# Problem:
# 	1. Use filter and a lambda to keep only positive temperatures. The lambda must stored in
# 	a variable and passed to the filter as a parameter.
# 	2. Use map to convert the remaining positive temps to Fahrenheit (F=C×9/5+32). Use 2nd
# 	lambda function for mapping.

c_temps = [0, 12, 34, 100, -5, 25]
positive_temp = list(filter((lambda x: x >= 0), c_temps))
print("Positive tempratures:", positive_temp)

fahrenheit_temp = list(map(lambda x: (x * 9 / 5) + 32, positive_temp))
print("Temprature in Fahrenheit:", fahrenheit_temp)

# ====================================================================================================


# %%
# Task - 05
# Given two lists: keys = ["ID", "Name", "Role"] values = [101, "Awais", "Faculty"]
# Problem: Write a Python function combine(keys, values)using a dictionary comprehension
# and zip() to combine them into one dictionary. The function must return the dictionary.


def combine(keys: list, values: list) -> dict:
    result = {key: value for key, value in zip(keys, values)}
    return result


keys = ["ID", "Name", "Role"]
values = [101, "Awais", "Faculty"]
print(combine(keys, values))
