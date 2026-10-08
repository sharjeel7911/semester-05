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
