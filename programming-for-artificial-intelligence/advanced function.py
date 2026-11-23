# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 09:17:22 2026

@author: faiza.khadim
"""

def url_builder(domain):
    def get_url(endpoint):
        return f"https://{domain}{endpoint}"
    return get_url


github = url_builder("github.com")
print(github("/user"))  # Output: https://github.com/user


google = url_builder("google.com")
print(google("/maps"))  # Output: https://google.com/maps
print(google("/search"))
print(google("/settings"))

# %%
def outer():
    name="faiza"
    def innr():
        nonlocal name 
        name="xyz"
        print(name)
        return name
    t=innr()
    print(name)
    return t

g=outer()
print(g)

# %%

def multiple(a):
    def inner(x):
        return a*x;
    return inner;

b=multiple(5)
print(b(6));

q=multiple(10)
print(q(8))
# %%
def outer(numbers):
    def inner():
        numbers.append(30)
        print(numbers)
    return inner

my_list = [10, 20]
f = outer(my_list)
f()
f()
print(my_list)
# %%
# A function is an object
def greet():
    print("Hello students!")
x = greet
x()

# %%
# A function can receive another function
def greet():
    print("Hello students!")

def call_function(func):
    func()

call_function(greet)
#A function that accepts another 
# function as an argument is using a 
# concept called a higher-order function.
# %%
# A function can return another function
def outer():
    def inner():
        print("Hello students!")

    return inner

result = outer()
result()

# %%

def welcome(func):
    def implement():
        print("aslamualikum")
        func()
        print("end of class")
    return implement
        
@welcome
def greet():
    print("welcome students of PAI")
        

# h=welcome(greet)
# h()
# %%


def welcome(func):
    def implement(*arg):
        print("aslamualikum")
        func(*arg)
        print("end of class",*arg)
    return implement
            
    
def greet(name):
    print(f"welcome{name} ")

q=welcome(greet)
#q("ali")
q(name="ali") # for this need kawarg

# %%

def welcome(func):
    def implement(*arg, **kward):
        print("aslamualikum")
        func(*arg,**kward)
        print("end of class",arg,kward)
    return implement

def greet(name, age, department):
    print(f"{name}, {age}, {department}")


y=welcome(greet)
y("ali",20,"cs")

print("************************")
y("ahamd",19,department="cs")

# %%


def welcome(func):
    def implement(*arg, **kward):
        print("aslamualikum")
        func(*arg,**kward)
        print("end of class",arg,kward)
    return implement

@welcome
def greet(name, age, department):
    print(f"{name}, {age}, {department}")


greet("ahamd",19,department="cs")
# %%

def welcome(func):
    def implement(*arg, **kward):
        print("aslamualikum")
        q=func(*arg,**kward)
        print("end of class",arg,kward,q)
    return implement

@welcome
def greet(name):
    print("Hello", name)

@welcome
def add(a, b):
    return a + b

greet("Ali")
add(10, 20)

# %%
def first(func):
    def wrapper():
        print("First: before")
        func()
        print("First: after")
    return wrapper


def second(func):
    def wrapper():
        func()
        print("Second: after")
    return wrapper


@first
@second
def greet():
    print("Hello!")

greet()

#second(greet)
# greet = first(second(greet))
# greet()
# %%

def repeat(times):

    def decorator(func):

        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)

        return wrapper

    return decorator

@repeat(3)
def greet():
    print("Hello!")


greet()
# %%

def require_role(required_role):

    def decorator(func):

        def wrapper(user_role, *args, **kwargs):
            if user_role != required_role:
                print("Access denied")
                return None

            return func(user_role, *args, **kwargs)

        return wrapper

    return decorator


@require_role("admin")
def delete_record(user_role):
    print("Record deleted")


delete_record("student")
delete_record("admin")

# %%

def my_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@my_decorator
def calculate_sum(a, b):
    """Calculate the sum of two numbers."""
    return a + b


print(calculate_sum.__name__)
# %%

from functools import wraps

def my_decorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@my_decorator
def calculate_sum(a, b):
    """Calculate the sum of two numbers."""
    return a + b


print(calculate_sum.__name__)
# %%
for name in ["Ali", "Sara", "Ahmed"]:
    print(name, "Welcome!")