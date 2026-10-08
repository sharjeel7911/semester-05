def calculate_area(length, width=10):  # width has a default value
    area = length * width
    return area

# Calling the function
result1 = calculate_area(5, 20)
result2 = calculate_area(5) # Uses default width of 10

print(f"Area 1: {result1}, Area 2: {result2}")