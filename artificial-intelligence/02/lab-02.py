# %%
# Exercise 2.1
# selection sort
from tkinter.constants import N
from turtle import resetscreen
from unittest import result


def selection_sort(items: list) -> list:
    for i in range(len(items)):
        min_index = i
        for j in range(i + 1, len(items)):
            if items[j] < items[min_index]:
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items


items = [5, 3, 8, 4, 2]
print(selection_sort(items))

# ====================================================================================================


# %%
# Exercise 2.2
# merge sort
def merge_sort(items: list) -> list:
    if len(items) <= 1:
        return items
    mid = len(items) // 2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])
    return merge(left, right)


def merge(left: list, right: list) -> list:
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


items = [5, 3, 8, 4, 2]
print(merge_sort(items))

# ====================================================================================================

# %%
# Exercise 2.3.
# Consider the list of characters: [‘P’,‘Y’,‘T’,‘H’,‘O’,‘N’]. Show how this list is sorted using the following algorithms:
# bubble sort
# selection sort
# insertion sort
# merge sort


class SortingAlgorithms:
    def __init__(self, items: list) -> None:
        self.items = items

    def bubble_sort(self) -> list:
        for i in range(len(self.items)):
            for j in range(len(self.items) - 1):
                if self.items[j] > self.items[j + 1]:
                    self.items[j], self.items[j + 1] = self.items[j + 1], self.items[j]
        return self.items

    def selection_sort(self) -> list:
        for i in range(len(self.items)):
            min_index = i
            for j in range(i + 1, len(self.items)):
                if self.items[j] < self.items[min_index]:
                    min_index = j
            self.items[i], self.items[min_index] = self.items[min_index], self.items[i]
        return self.items

    def insertion_sort(self) -> list:
        for i in range(1, len(self.items)):
            key = self.items[i]
            j = i - 1
            while j >= 0 and self.items[j] > key:
                self.items[j + 1] = self.items[j]
                j -= 1
            self.items[j + 1] = key
        return self.items

    def merge_sort(self, items=None) -> list:
        if items is None:
            items = self.items
        if len(items) <= 1:
            return items
        mid = len(items) // 2

        left = self.merge_sort(items[:mid])
        right = self.merge_sort(items[mid:])
        return self.merge(left, right)

    def merge(self, left: list, right: list) -> list:
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result


item = SortingAlgorithms(["P", "Y", "T", "H", "O", "N"])
print("Bubble Sort -> O(n^2):", item.bubble_sort())
print("Selection Sort -> O(n^2):", item.selection_sort())
print("Insertion Sort -> O(n^2):", item.insertion_sort())
print("Merge Sort -> O(n log n):", item.merge_sort())

# ====================================================================================================

# %%
# Exercise 2.4.
# Write a function to find mean, median, mode for the given set of numbers in a list.
# 1. Read the elements into a list.
# 2. Calculate the sum of list elements.
# 3. Calculate the mean, median.
# 4. Display the result.


def find_mean_median_mode(items: list) -> tuple:
    sum_ = sum(items)
    mean = sum_ / len(items)
    median = sorted(items)[len(items) // 2]
    mode = max(set(items), key=items.count)
    return (mean, median, mode)


items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 3, 4, 9]
res = find_mean_median_mode(items)
print("Mean:", res[0])
print("Median:", res[1])
print("Mode:", res[2])

# ====================================================================================================

# %%
# Exercise 2.5
# Write a function dups to find all duplicates in the list.
# 1. Create a list to read elements.
# 2. Pass the list as parameter to dup function.
# 3. Define function dup to identify duplicate elements in the list.
# 4. Return the final list to called function.
# 5. Display the result


def dups(items: list) -> list:
    return [item for item in set(items) if items.count(item) > 1]


items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 3, 4, 9]
print("Duplicates:", dups(items))


# ====================================================================================================

# %%
# Exercise 2.6
# Implement the following instructions.
# 1. Create a list a which contains the first three odd positive integers and a list b which contains the first three even positive integers.
# 2. Create a new list c which combines the numbers from both lists (order is unimportant).
# 3. Create a new list d which is a sorted copy of c, leaving c unchanged.
# 4. Reverse d in-place.
# 5. Set the fourth element of c to 42.
# 6. Append 10 to the end of d.
# 7. Append 7, 8 and 9 to the end of c.
# 8. Print the first three elements of c.
# 9. Print the last element of d without using its length.
# 10. Print the length of d.

a = [1, 3, 5]
b = [2, 4, 6]
c = a + b
d = sorted(c)
d.reverse()
c[3] = 42
d.append(10)
c.extend([7, 8, 9])
print("c:", c[:3])
print("d:", d[-1])
print("d length:", len(d))

# ====================================================================================================

# %%
# Exercise 2.7
# 1. Create a list a which contains three tuples. The first tuple should contain a single element, the
# second two elements and the third three elements.
# 2. Print the second element of the second element of a.
# 3. Create a list b which contains four lists, each of which contains four elements.
# 4. Print the last two elements of the first element of b.

a = [(1,), (1, 2), (1, 2, 3)]
print("a:", a[1][1])

b = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print("b:", b[0][-2:])

# ====================================================================================================

# %%
# Exercise 2.8
# 1. Write a program which uses a nested for loop to populate a three-dimensional list representing a
# calendar: the top-level list should contain a sub-list for each month, and each month should
# contain four weeks. Each week should be an empty list.
# 2. Modify your code to make it easier to access a month in the calendar by a human-readable month
# name, and each week by a name which is numbered starting from 1. Add an event (in the form of
# a string description) to the second week in July.


def create_calendar() -> list:
    calendar = []
    for month in range(12):
        month_list = []
        for week in range(4):
            week_list = []
            month_list.append(week_list)
        calendar.append(month_list)
    return calendar


calendar = create_calendar()
print("calendar:", calendar)
print()


def modify_calendar() -> dict:
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    calendar = {}

    for month in months:
        month_dict = {}

        for week in range(1, 5):
            month_dict[f"Week {week}"] = []

        calendar[month] = month_dict

    return calendar


calendar = modify_calendar()

# Add an event to the second week of July
calendar["July"]["Week 2"].append("University assignment deadline")

print("Event:", calendar["July"]["Week 2"])
print("July calender:", calendar["July"])

# ====================================================================================================

# %%
# Exercise 2.9
# Create a list whose elements contain the integers from 100,000 through 300,000, inclusive (be careful!
# what should the range be?) and set the variable big_list to contain that list.
# NOTE: Put the assignment that creates big_list in your python file outside the scope of a function.
# Do NOT assign to big_list in the timer or search functions because it will invalidate the timing and
# search results.
# a. Time how long it takes the search function above to find each of the following in big_list:
# 	i.element at front (100000)
# 	ii.element in middle (200000)
# 	iii.element at back (300000)
# 	iv.element not in the list (3)
# 	How long does each take?
# b. If you repeat the same searches, does it take exactly the same amount of time? Why do you think
# this is?
# c. How would you describe the relationship between the position of the item you are searching for
# in the list and how long it takes to find that item? (Is the search time independent of the position,
# or is there some mathematical relationship between the two quantities?)

# 1.
import time

# Create the list outside all functions
big_list = list(range(100000, 300001))


def search(int_list: list, key: int) -> int | None:
    for i in range(len(int_list)):
        if int_list[i] == key:
            return i
    return None


def timer(key: int) -> float:
    start = time.perf_counter()  # or use time.time()
    search(big_list, key)
    end = time.perf_counter()
    return end - start


# Test searches
keys = [100000, 200000, 300000, 3]

for key in keys:
    elapsed_time = timer(key)
    print(f"Searching for {key}: {elapsed_time:.8f} seconds")


# 2.
# No, repeated searches will not take exactly the same amount of time.
# Small differences can occur because of:
# - Operating system scheduling and background processes.
# - CPU load and processor frequency.
# - Python interpreter overhead.
# - Measurement precision.

# 3.
# The search time depends on the position of the element because this is a linear search.
# - Best case: O(1) — the first element matches.
# - Average case: O(n) — the search examines roughly half the list for a uniformly distributed successful search.
# - Worst case: O(n) — the element is last or is absent.
# Here, n is the number of elements in the list.
# As the target's position moves toward the end, the search generally takes longer. For a missing element, every element must be checked.

# ===================================================================================================
