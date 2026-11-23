# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 11:31:57 2026

@author: faiza.khadim
"""
# %%
class instructor:
    def display(self):
        print(id(self))
        print("I am a student")


s1 = instructor()
s2 = instructor()

s1.display()
s2.display()

# %%

class instructor:
    def __init__(self):
        print("construtcor calling")

    def display(self):
        pass
   
s1 = instructor()
s2 = instructor()

s1.display() #EQUIVALENT instructor.display(s1)
s2.display()
# %%

class instructor:
    def display(self):
        print(f"{self.name}, {self.id}, {self.salary}")

ints1=instructor()
ints1.name="ali"
ints1.id=14242
ints1.salary=50000
ints1.display()

s2=instructor()
s2.name="misb"
s2.id=101
s2.salary=45
s2.display()  #s2 ka loiye be teeno cheezain dena zarori ha

# %%
#constructor is there
class instructor:
    def __init__(self, name, id, salary):
        self.name=name
        self.id=id;
        self.salary=salary
        
    def display(self):
        print(f"{self.name}, {self.id}, {self.salary}")


ints1=instructor("ali",4564,50000)
ints1.display()

s2=instructor("fiza",54545,60000)
s2.display()  
# %%
class instructor:
    def __init__(self, name="unknown", id="unknow", salary="unknow"):
        self.name=name
        self.id=id;
        self.salary=salary
        
    def display(self):
        print(f"{self.name}, {self.id}, {self.salary}")
    
ints1=instructor("ali",4564,50000)
ints1.display()

s2=instructor("fiza",54545,60000)
s2.display()  

s3=instructor()
s3.display()

# %%
class instructor:
    
    def __init__(self, name, id, salary):
        self.name=name
        self.id=id;
        self.salary=salary
        self.follower=0 # default attributes
        
    def display(self):
        print(f"{self.name}, {self.id}, {self.salary}, {self.follower}")


ints1=instructor("ali",4564,50000)
ints1.display()

s2=instructor("fiza",54545,60000)
s2.display() 
# %%
# class attributes
class instructor:
    
    company="UCP" # class attributes
    def __init__(self, name, id, salary):
        self.name=name #instance attributes
        self.id=id;
        self.salary=salary
        self.follower=0 # default attributes
        
    def display(self):
        print(f"{self.name}, {self.id}, {self.salary}, {self.follower},{instructor.company}")

ints1=instructor("ali",4564,50000)
ints1.display()

s2=instructor("fiza",54545,60000)
s2.display() 

print(s2.company)
# %%

class Student:
    university = "UCP"

s1 = Student()
s2 = Student()

s1.university = "COMSATS"
s2.university="UMT"

print(s1.university)       # COMSATS
print(s2.university)       # UMT

print(Student.university)  # UCP

#Python creates an instance attribute for s1. 
#It does not modify the original class attribute.
# %%
class Employee:
    count = 0
    def __init__(self, name):
        self.name = name
        Employee.count += 1


e1 = Employee("Ali")
e2 = Employee("Ahmed")
e3 = Employee("Sara")

print(Employee.count)  # 3
# %%
class instructor:
    company="UCP" 
    def __init__(self, name, id, salary):
        self.name=name
        self.id=id;
        self.__salary=salary
        self.follower=0 # default attributes
    def display(self):
        print(f"{self.name}, {self.id}, {self.__salary}, {self.follower},{instructor.company}")

ints1=instructor("ali",4564,50000)
ints1.display()

s2=instructor("fiza",54545,60000)
s2.display()  #s2 ka loiye be teeno cheezain dena zarori ha

print(s2.company)

#print(S2.__salary) #private it will error
print(s2._instructor__salary) # privates, name mangling
# %%
#if we create clas avarible as a a privates
class instructor:
    
    __company="UCP" # class attributes ko be self sa printkarna
    
    def __init__(self, name, id, salary):
        self.name=name
        self.id=id;
        self.__salary=salary
        self.follower=0 # default attributes
        
        
    def display(self):  # class name be likha ja skta qwith class variable
        print(f"{self.name}, {self.id}, {self.__salary}, {self.follower},{instructor.__company}")

ints1=instructor("ali",4564,50000)
ints1.display()

s2=instructor("fiza",54545,60000)
s2.display() 

print(instructor._instructor__company) #now ab instructor ka under _instructor__company


#print(S2.__salary) #private it will error
print(s2._instructor__salary) # privates, name mangling

#but you can access it by name mangling
print(vars(instructor))# 	Class ke apne stored attributes
print(vars(s2)) #Sirf object ke apne stored attributes

# %%
#single inheritence
class person:
    def __init__(self, name):
        self.name=name;
    
class teacher(person):
    def  __init__(self, name, subject):
        super().__init__(name) # calling parent class constructor
        self.subject=subject
        
    def display(self):
        print(f"{self.name}, {self.subject}")

t1=teacher("faiza","python")
t1.display()

# %%
#single inheritence
class person:
    def __init__(self, name):
        self.__name=name;
    
class teacher(person):
    def  __init__(self, name, subject):
        super().__init__(name) # calling parent class constructor
        self.subject=subject

    def display(self):
        print(f"{self._person__name}, {self.subject}")#### important

t1=teacher("faiza","python")
t1.display()
# %%

#single inheritence
class person:
    def __init__(self, name):
        self.__name=name;
    
    def getname(self):
        return self.__name
    
class teacher(person):
    def  __init__(self, name, subject):
        super().__init__(name) # calling parent class constructor
        self.subject=subject

    def display(self):
        print(f"  {super().getname()},{self.subject}")

t1=teacher("faiza","python")
t1.display()
# %%
#single inheritence with base privarte members with function  further extension
class person:
    def __init__(self, name):
        self.__name=name;
        
    def display(self):
        print(f"{self.__name}")
    
class teacher(person):
    def  __init__(self, name, subject):
        super().__init__(name) # calling parent class constructor
        self.subject=subject

    def display(self):
        super().display()
        print(f"{self.subject}")

t1=teacher("faiza","python")
t1.display()

# %%
#method overriding
class Person:
    def display(self):
        print("I am a Person")

class Student(Person):
    def display(self):
        print("I am a Student")


p1 = Person()
s1 = Student()

p1.display()
s1.display()
# %%

#Task solution
class BankAccount:
    def __init__(self, account_holder, balance):
        self.__account_holder = account_holder
        self._balance = balance

    def display_account(self):
        print("Account Holder:", self.__account_holder)
        print("Balance:", self._balance)
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self._balance * self.interest_rate / 100

    def deposit(self, amount):
        self._balance += amount

    def display_savings(self):
        super().display_account()
        print("Interest Rate:", self.interest_rate, "%")
        print("Annual Interest:", self.calculate_interest())
# List of multiple objects
accounts = [
    SavingsAccount("Ali", 50000, 5),
    SavingsAccount("Sara", 80000, 4),
    SavingsAccount("Ahmed", 60000, 3)
]
# Display all accounts
for account in accounts:
    account.display_savings()
    print("-------------------")
# %% complete class
class PatientRecord:
    # 1. The Constructor (Equivalent to C++ ClassName())
    def __init__(self, p, a, d="Normal"):
        # Member Properties (Instance Variables)
        self.patient_id = p
        self.age = a
        self.diagnosis = d
        self.is_processed = False  # Default property
        
        self.__medicine = "Panadol"     #private member
        self._doctor = "Arsalan"#protected
    
    # 2. Member Function (Instance Method)
    def update_diagnosis(self, new_diag):
        print(f"Updating diagnosis for Patient {self.patient_id}...")
        self.diagnosis = new_diag
        self.__medicine = "Calpol"
    
    # 3. Member Function with Logic
    def get_patient_summary(self):
        status = "Processed" if self.is_processed else "Pending"
        return f"ID: {self.patient_id} | Age: {self.age} | Diag: {self.diagnosis} | Status: {status}"

    def get_medicine(self):
        return self.__medicine

# --- Using the Class ---
# Creating an instance (No 'new' keyword required)
p1 = PatientRecord("Pno-001", 65, "MI")

# Accessing properties
print(p1.get_medicine()) 
p1.update_diagnosis("Helathy")
print(p1.get_medicine()) 

print(p1._doctor)

# # Calling member functions
# p1.update_diagnosis("Recovered")
# print(p1.get_patient_summary())
# %%
class Student:
    def __init__(self, marks):
        self.marks = marks

    def __len__(self):
        return len(self.marks)

s1 = Student([80, 90, 75])

print(len(s1))
# %%

#dunder method __str__, __len__
class Student:
    university = "UCP"

    def __init__(self, name, roll_no, department, semester):
        self.name = name
        self.roll_no = roll_no
        self.department = department
        self.semester = semester

    def __str__(self):
        return f"Name: {self.name}\nRoll No: {self.roll_no}\nDepartment: {self.department}\nSemester: {self.semester}\nUniversity: {Student.university}"

    def __len__(self):
        return len(self.name)
        
        
        
s1 = Student("Ali", 101, "Artificial Intelligence", 5)

print(s1)
print(len(s1))
# %%
#@property is a decorator that allows us to access a class method like 
#an attribute without using parentheses.
class Employee:
    def __init__(self, emp_id):
        self._emp_id = emp_id

    @property
    def getemp_id(self):
        return self._emp_id


e1 = Employee(101)

print(e1.getemp_id)  # 101

e1.getemp_id = 202   # AttributeError
# %%

class Employee:
    def __init__(self, emp_id):
        self._emp_id = emp_id

    @property
    def getemp_id(self):
        return self._emp_id

    @getemp_id.setter
    def getemp_id(self, value):
        self._emp_id = value


e1 = Employee(101)

print(e1.getemp_id)  # 101

e1.getemp_id = 202

print(e1.getemp_id)  # 202
# %%
#dunder method __add__
class Signal:
    def __init__(self, data):
        self.data = data # List of voltages
        
    def __len__(self):
        return len(self.data)
    
    def __add__(self, other):
        result=[]
        for a, b in zip(self.data, other.data):
            sum_value = a + b
            result.append(sum_value)
        return Signal(result)
        #return Signal([a + b for a, b in zip(self.data, other.data)])
    
# Create two signal objects
sig1 = Signal([1.2, 2.4, 3.6])
sig2 = Signal([0.8, 1.6, 2.4])

# Using __len__
print(f"Signal length: {len(sig1)}")  # Output: 3

# Using __add__ (Operator Overloading)
combined_sig = sig1 + sig2 
print(f"Combined data: {combined_sig.data}")  # Output: [2.0, 4.0, 6.0]


# %%
class DatabaseSession:
    def __init__(self):
        print("the constructor")
        self.data = [11, 12, 13, 14, 15]
        
    def __enter__(self):
        print("Connecting to Clinic DB...")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing Connection.")
        print(exc_type,exc_val, exc_tb)
        
    def execute(self):
        print("inside execute")
        for i in self.data:
            print("processing: ", i)
        print("exiting execute")

# This mimics the C++ scope-based resource management
with DatabaseSession() as db:
    print("Executing AI Query on patient records...")
    db.execute()
    # Logic happens here...
# Connection closes automatically here even if an error occurs inside the block



# %%
class MyCollection:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

    def __delitem__(self, index):
        del self.data[index]

    def __contains__(self, value):
        return value in self.data


obj = MyCollection([10, 20, 30])

print(obj[0])         # 10

obj[0] = 100
print(obj.data)       # [100, 20, 30]

del obj[1]
print(obj.data)       # [100, 30]

print(30 in obj)      # True
# %%

class MyCollection:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

    def __contains__(self, key):
        return key in self.data


obj = MyCollection({"name": "Ali", "age": 23, "salary": 50000})

# Access value
print(obj["name"])       # Ali

# Update value
obj["age"] = 25
print(obj.data)

# Add new key-value pair
obj["city"] = "Lahore"
print(obj.data)

# Delete key
del obj["salary"]
print(obj.data)

# Check key
print("name" in obj)     # True


# %%
#Multiple Inheritance (MRO): When one child class inherits from two 
#or more parent classes, it is called Multiple Inheritance.

# class Father {
# public:
#     void show() {
#         cout << "Father";
#     }
# };

# class Mother {
# public:
#     void show() {
#         cout << "Mother";
#     }
# };

# class Child : public Father, public Mother {
# };

# int main() {
#     Child obj;
#     obj.show();  // ERROR: Ambiguous obj.Father::show()
# }

class father:
    def show(self):
        print("father method")
class mother:
    def show(self):
        print("mother method")
class boy(father, mother):
    pass

boy_1=boy()
boy_1.show()# MRO order, method resolution order

# mother.show(boy_1) 
print(boy.mro())
# %%
#multipleinheritence constructors
# class Father {
# public:
#     Father() {
#         cout << "Father Constructor\n";
#     }
# };

# class Mother {
# public:
#     Mother() {
#         cout << "Mother Constructor\n";
#     }
# };

# class Child : public Father, public Mother {
# public:
#     Child() {
#         cout << "Child Constructor\n";
#     }
# };

# int main() {
#     Child obj;
# }
class Father:
    def __init__(self):
        print("Father Constructor")
class Mother:
    def __init__(self):
        print("Mother Constructor")

class Child(Father, Mother):
    def __init__(self):
        print("Child Constructor")
        super().__init__()
       
        
obj = Child()
# %%

class Father:
    def __init__(self):
        print("Father Constructor")
        super().__init__()

class Mother:
    def __init__(self):
        print("Mother Constructor")
        super().__init__()
        
class Child(Father, Mother):
    def __init__(self):
        print("Child Constructor")
        super().__init__()
        
obj = Child()

print(Child.mro())
# %%
#diamond problem
class A:
    def speak(self): print("A")
class B(A):
    def speak(self): print("B"); super().speak()
class C(A):
    def speak(self): print("C"); super().speak()
class D(B, C):
    def speak(self): super().speak()
    
d_obj = D()
d_obj.speak()
print(D.mro())

# Notice: 'A' is only called ONCE because of Python's C3 Linearization(ALGO).
#super() does not necessarily call the direct parent class.
# It calls the next class in the Method Resolution Order (MRO) of the current object.
# %%
#diamond problem
class A:
    def show(self):
        print("Class A")
class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

obj = D()
obj.show()

print(D.mro())
# %%
class A:
    def show(self):
        print("A")


class B:
    def show(self):
        print("B")


class C(A, B):
    pass


class D(B, A):
    pass


obj1 = C()
obj2 = D()

obj1.show()
obj2.show()
print(D.mro())

# %%
# output
class Person: 
    def __init__(self, n, a, **kwargs):
        print("Constructor: Person")
        self.name = n
        self.age = a
        super().__init__(**kwargs)
        
    def __str__(self):
        return f"Person: name = {self.name}, age = {str(self.age)}" + "\n" + super().__str__()

class Employee: 
    def __init__(self, d, e, **kwargs):
        print("Constructor: Employee")
        self.department = d
        self.experience = e
        super().__init__(**kwargs)
        
    def __str__(self):
        return f"Employee: Depart = {self.department}, Exp = {str(self.experience)}" + "\n" + super().__str__()

class Faculty(Employee, Person):
    
    def __init__(self, n, a, d, e):
        print("Constructor: Faculty")
        super().__init__(n = n, a = a, d =  d, e = e)
        
    def __str__(self):
        return super().__str__()
    
# MRO: Faculty -> Person -> Employee -> object

t1 = Faculty("ahmad", 40, "CS", 20)
print(t1)
# Check the Method Resolution Order (The "Search Path")
# print(Faculty.mro()) 
# Output: [<class 'Faculty'>, <class 'Person'>, <class 'Employee'>, <class 'object'>]

# %%

# Dynamically creating a class. 
class CommonBase:
    def info(self): print("Common Base")
    
class BaseData:
    def info(self): print("Base Data")

class SQL_Source:
    def info(self): print("SQL Source")


# ClassName = type(
#     "ClassName",
#     (Parent1, Parent2),
#     {"attribute": value}
# )
# We decide the MRO (SQL_Source first, then BaseData) at runtime.
DynamicModel = type("DynamicModel", (SQL_Source, BaseData, CommonBase), {"version": 1.0})


# class DynamicModel(SQL_Source, BaseData, CommonBase):
#     version = 1.0

# Testing the MRO
obj = DynamicModel()
obj.info()  # Output: SQL Source
print(DynamicModel.mro()) 


#Golden rule: Python searches from left to right according to MRO and 
#executes the first matching method it finds.
# [<class 'DynamicModel'>, <class 'SQL_Source'>, <class 'BaseData'>, <class 'object'>]
# %%
def show(self):
    print("Employee Information")

def display_salary(self):
    print("Salary: 50000")

def display_department(self):
    print("Department: IT")

Employee = type(
    "Employee",
    (),
    {
        "show": show,
        "display_salary": display_salary,
        "display_department": display_department
    }
)
obj = Employee()
obj.show()
obj.display_salary()
obj.display_department()

# %%
def display_info(self):
    print("\nUser Information")
    print("Name:", self.name)
    print("Role:", self.role)
    
class Student:
    def study(self):
        print("Student is studying.")
    def submit_assignment(self):
        print("Student has submitted the assignment.")
        
class Teacher:
    def teach(self):
        print("Teacher is teaching.")

    def check_assignment(self):
        print("Teacher is checking assignments.")

choice = input("Enter role (Student/Teacher): ")
if choice == "Student":
    Parent = Student
else:
    Parent = Teacher
    
User = type(
    "User",
    (Parent,),
    {
        "showed": display_info, # now method name would be showed
        "name": "Faiza",
        "role": choice
    }
)

obj = User()
obj.showed() # see

if choice == "Student":
    obj.study()
    obj.submit_assignment()

else:
    obj.teach()
    obj.check_assignment()

# %%
from abc import ABC, abstractmethod
#ABC: Helps us create an abstract base class.
#abstractmethod: Marks a method as abstract.
class AIModel(ABC):
    @abstractmethod
    def train(self, data):
        """This is a pure virtual function equivalent"""
        pass

    def save_model(self):
        """Abstract classes can still have concrete methods"""
        print("Saving weights to disk...")

class NeuralNet(AIModel):
    def train(self, data):
        print(f"Training Neural Net on {len(data)} samples")

#model = AIModel() # Error! Cannot instantiate abstract class

nn = NeuralNet()
nn.train([1, 2, 3])
nn.save_model()
# %%
class movemixin:
    def move(self):
        print(f"{self.__class__.__name__} is moving")
        
class animal:
    def eat(self):
        print("eat")
class cat(animal, movemixin):
    pass
class dog(animal,movemixin):
    pass
class car(movemixin):
    pass

dog1=dog();
dog1.move()

cat1 = cat()
cat1.move()

car1 = car()
car1.move()
# %%
class LoggerMixin:
    def log_activity(self):
        print("Activity recorded successfully")


class Student(LoggerMixin):
    def display(self):
        print("Student details")


class Teacher(LoggerMixin):
    def display(self):
        print("Teacher details")


s1 = Student()
t1 = Teacher()

s1.display()
s1.log_activity()

t1.display()
t1.log_activity()
# %%

class LoggerMixin:
    def log(self):
        print("Activity logged")

class PrintMixin:
    def print_data(self):
        print("Data sent to printer")

class SaveMixin:
    def save(self):
        print("Data saved successfully")

class Student(LoggerMixin, PrintMixin, SaveMixin):
    def __init__(self, name):
        self.name = name


s1 = Student("Ali")

s1.log()
s1.print_data()
s1.save()

# %%

#include <iostream>
# using namespace std;

# class LoggerMixin {
# public:
#     void log() {
#         cout << "Activity logged" << endl;
#     }
# };

# class Student : public LoggerMixin {
# };

# int main() {
#     Student s1;
#     s1.log();

#     return 0;
# }
# %%
#__setattr__ as magic function
class Patient:
    def __setattr__(self, name, value):
        print("Attribute:", name)
        print("Value:", value)
        super().__setattr__(name, value)

    def __init__(self, name, age, disease):
        self.name = name
        self.age = age
        self.disease = disease

p1 = Patient("Ali", 30, "Diabetes")
print("in main\n",p1.name, p1.age)


#print(dir(object)) #list function
#print(dir(p1))
#print(help(object))#list details
# %%
class ValidationMixin:
    def __setattr__(self, name, value):
        if name == "age" and value < 0:
            print("Invalid Age! Age cannot be negative.")
        super().__setattr__(name, value)

class PatientProfile(ValidationMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = PatientProfile("Ali", 30)
p2 = PatientProfile("Sara", -5)

print(p1.age)
print(p2.age)