#!/usr/bin/env python
# coding: utf-8

# # Write a Python class named Point3D defined by x, y, and z. Define a method that returns (x, y ,z). This tells Python to represent this object in the following format: (x, y, z). Then create a variable named my_point containing a new instance of Point3D with x=1, y=2, and z=3 and print it.

# In[2]:


class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def coordinates(self):
        return (self.x, self.y, self.z)

# Create an instance of Point3D
my_point = Point3D(x=1, y=2, z=3)

# Print the coordinates of my_point
print(my_point.coordinates())


# # Write a Python class named Rectangle constructed by a length and width. Define two methods, area and perimeter, which will compute the area and the perimeter of the rectangle. Then create a variable named my_rectangle containing a new instance of Rectangle with width=3 and length = 4 and compute both area and perimeter ( the area is expected to be 3*4=12 and perimeter 2*(3+4)=14).

# In[3]:


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Create an instance of Rectangle
my_rectangle = Rectangle(length=4, width=3)

# Compute and print the area and perimeter
print("Area:", my_rectangle.area())
print("Perimeter:", my_rectangle.perimeter())


# # Write a Python  class named Circle constructed by its center O and radius r. Define two methods, area and perimeter, which will compute the area and the perimeter of the circle, and is Inside() method which allows you to test whether a point A(x, y) belongs to the circle C(O, r) or not.
# 

# In[4]:


import math

class Circle:
    def __init__(self, center_x, center_y, radius):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def is_inside(self, point_x, point_y):
        distance = math.sqrt((point_x - self.center_x)**2 + (point_y - self.center_y)**2)
        return distance <= self.radius

# Create an instance of Circle
my_circle = Circle(center_x=0, center_y=0, radius=5)

# Compute and print the area and perimeter
print("Area:", my_circle.area())
print("Perimeter:", my_circle.perimeter())

# Test if a point is inside the circle
point_to_test = (3, 4)
if my_circle.is_inside(*point_to_test):
    print(f"The point {point_to_test} is inside the circle.")
else:
    print(f"The point {point_to_test} is outside the circle.")


# # Suppose we want to model a bank account with support for deposit and withdraw operations. Let’s create a Python class named Bank defined by its balance. Define two methods, deposit and withdraw, to compute the new amount of each operation.

# In[5]:


class Bank:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposit successful. New balance: {self.balance}"
        else:
            return "Invalid deposit amount. Please deposit a positive amount."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrawal successful. New balance: {self.balance}"
        elif amount > self.balance:
            return "Insufficient funds. Withdrawal canceled."
        else:
            return "Invalid withdrawal amount. Please withdraw a positive amount."

# Create an instance of Bank with an initial balance
my_bank_account = Bank(balance=1000)

# Deposit and print the new balance
print(my_bank_account.deposit(500))

# Withdraw and print the new balance
print(my_bank_account.withdraw(200))

# Attempt to withdraw more than the balance
print(my_bank_account.withdraw(1500))

# Attempt to deposit a negative amount
print(my_bank_account.deposit(-100))


# In[ ]:




