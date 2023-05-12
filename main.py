"""Imports current time"""
from datetime import datetime

def inputcheck(question):
    while True:
        try:
            x = input(f"{question} : ")
        except any:
            print("An Error Occured, please try again")
        else:
            return x
    

def run_program(filename):
    """Runs program and informs user of operation"""
    print(
        """
        Running Program..."""
    )
    open(filename, "r", encoding="utf8")


def get_message():
    """sends output based on time of day"""
    now = datetime.now()
    current_time = int(now.strftime("%H")) - 5
    if 0 > current_time:
        current_time += 24
    if current_time < 12:
        return "Good Morning"
    elif current_time < 18:
        return "Good Afternoon"
    return "Good Night"


END = False
while END is False:
    print(
        """Hello, please choose an option from the following list
ID     Script

CI1  - Check In 1
CI2  - Check In 2
CI3  - Check In 3
CI4  - Check In 4

EX1  - Exercise 1
EX2  - Exercise 2
EX3  - Exercise 3
EX4  - Exercise 4
EX5A - Exercise 5 A
EX5B - Exercise 5 B
EX5C - Exercise 5 C
EX6  - Exercise 6

REV1 - Review 1
REV2 - Review 2

DATA - view/change data

QUIT - Quit probram
"""
    )
    script = input("Please enter a script ID : ")
    if script == "CI1":
        run_program("check_in_1.py")
    elif script == "CI2":
        run_program("check_in_2.py")
    elif script == "CI3":
        run_program("check_in_3.py")
    elif script == "CI4":
        run_program("check_in_4.py")
    elif script == "EX1":
        run_program("exercize_1.py")
    elif script == "EX2":
        run_program("exercize_2.py")
    elif script == "EX3":
        run_program("exercize_3.py")
    elif script == "EX4":
        run_program("exercize_4.py")
    elif script == "EX5A":
        run_program("exercize_5_a.py")
    elif script == "EX5B":
        run_program("exercize_5_b.py")
    elif script == "EX5C":
        run_program("exercize_5_c.py")
    elif script == "EX6":
        run_program("exercize_6.py")
    elif script == "REV1":
        run_program("review_1.py")
    elif script == "REV2":
        run_program("review_2.py")
    elif script == "DATA":
        run_program("data.py")
    elif script == "QUIT":
        END = True
print(
    """
      Script Ended"""
)
