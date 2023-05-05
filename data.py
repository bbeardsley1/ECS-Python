"""displays user data and allows entry"""
from main import AGE
from main import NAME

print(
    """
Welcome to the data section
Please enter / view your data below
"""
)
if AGE == int(0):
    AGE = int(input("Age : "))
else:
    print(f"Age : {AGE}")
if NAME == str(""):
    NAME = input("Name : ")
else:
    print(f"Name : {NAME}")
