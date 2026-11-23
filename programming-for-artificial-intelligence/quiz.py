#Q1
celsius_to_fahrenheit = lambda c: (c * 1.8) + 32

def process_stream(data_list, transform_lambda):
    for temp in data_list:
        converted_temp = transform_lambda(temp)
        yield converted_temp 

celsius_temps = [0, 15, 25, 30, 40]
temp_generator = process_stream(celsius_temps, celsius_to_fahrenheit)

print("--- Fahrenheit Data Stream (Using Iterator & Loop) ---")
print("First value using next():", next(temp_generator))
print("Second value using next():", next(temp_generator))

print("\nRemaining values using for loop:")
for fahrenheit in temp_generator:
    print(fahrenheit)
    
# %%
#Q2
def verify_session(func):
    def wrapper(user_role, prices):
        if user_role in ["Admin", "Customer"]:
            print("[Access Granted] Executing operation...")
            t = func(prices)
            return t
        print("[Access Denied] Unauthorized User! Operation Blocked.")
        return []
    return wrapper


@verify_session
def apply_conditional_discounts(prices):
    discount_lambda = lambda items: [item * 0.8 if item > 100 else item for item in items]
    return discount_lambda(prices)


cart_prices = [45, 120, 80, 250, 60]

print("--- Test 1: Authorized User ---")
result_authorized = apply_conditional_discounts("Customer", cart_prices)
print("Output:", result_authorized)

print("\n--- Test 2: Unauthorized User ---")
result_unauthorized = apply_conditional_discounts("Guest", cart_prices)
print("Output:", result_unauthorized)
# %%

def verify_session(func):
    def wrapper(user_role, prices):
        output = []
        if user_role in ["Admin", "Customer"]:
            print("[Access Granted] Executing operation...")
            output = func(prices)
        else:
            print("[Access Denied] Unauthorized User! Operation Blocked.")
            output = []
        return output
    return wrapper


@verify_session
def apply_conditional_discounts(prices):
    discount_lambda = lambda items: [item * 0.8 if item > 100 else item for item in items]
    return discount_lambda(prices)


cart_prices = [45, 120, 80, 250, 60]

print("--- Test 1: Authorized User ---")
result_authorized = apply_conditional_discounts("Customer", cart_prices)
print("Output:", result_authorized)

print("\n--- Test 2: Unauthorized User ---")
result_unauthorized = apply_conditional_discounts("Guest", cart_prices)
print("Output:", result_unauthorized)