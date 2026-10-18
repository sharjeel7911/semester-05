# %%
# Write a function process_coordinates(points, min_dist) that takes a list of strings representing 2D coordinates.
# Each string contains a PointID and an (x, y) coordinate pair separated by colons (e.g., "P1:3:4").
# Define a "distance" rule that calculates the Euclidean distance from the origin.
# Use a List Comprehension to apply this lambda, but only include points whose distance is strictly greater than min_dist.
# Return a list of dictionaries with keys pointId and distance. The final list must be sorted by distance in descending order.
# Example:
# ["P1:3:4", "P2:1:1", "P3:0:5", "P4:10:10", "P5:2:2"]


def process_coordinates(points: list[str], min_dist: int) -> list[dict]:
    distance = lambda x, y: (x**2 + y**2) ** 0.5
    parsed_str = [p.split(":") for p in points]
    print("Parced Str:", parsed_str)

    res = [
        {"pointId": pid, "distance": distance(int(x), int(y))}
        for pid, x, y in parsed_str
        if distance(int(x), int(y)) > min_dist
    ]
    return sorted(res, key=lambda x: x["distance"], reverse=True)


points = ["P1:3:4", "P2:1:1", "P3:0:5", "P4:10:10", "P5:2:2"]
min_dist = 5
res = process_coordinates(points, min_dist)
print(res)

# ====================================================================================================

# %%
# Write a function analyze_inventory(stock_data, min_value) that takes a list of strings representing warehouse stock.
# Each string contains a SKU, Category, UnitPrice, and StockCount separated by colons (e.g., "SKU45:Electronics:200.0:15").
# Define a "valuation" rule that calculates the total value of that stock item (UnitPrice × StockCount) using lambda function.
# Use a List Comprehension to apply this logic, but only include items where the total valuation is greater than min_value.
# Return a list of dictionaries with keys sku, category, and totalValue. The final list must be sorted alphabetically by category.
# Example
# ["A1:Office:10:50", "B2:Hardware:100:2", "C3:Office:5:10", "D4:Hardware:50:20", "D5:Accounts:20:80"]


def analyze_inventory(stock_data: list[str], min_value: int) -> list[dict]:
    valuation = lambda price, stock: price * stock
    parsed_str = [s.split(":") for s in stock_data]
    res = [
        {"sku": sku, "category": cat, "totalValue": valuation(int(price), int(count))}
        for sku, cat, price, count in parsed_str
        if valuation(int(price), int(count)) > min_value
    ]
    return sorted(res, key=lambda x: x["category"])


stock_data = [
    "A1:Office:10:50",
    "B2:Hardware:100:2",
    "C3:Office:5:10",
    "D4:Hardware:50:20",
    "D5:Accounts:20:80",
]
min_value = 1000
res = analyze_inventory(stock_data, min_value)
print(res)
