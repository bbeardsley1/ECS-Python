"""Imports current time"""
from datetime import datetime


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


AGE = int(0)
NAME = str("")
END = False
while END is False:
    print(
        """Hello, please choose an option from the following list
ID     Script

CI1  - Check In 1
CI2  - Check In 2
CI3  - Check In 3
CI4  - Check In 4

DP1  - Day 1 Practice
DP2  - Day 2 Practice
DP3  - Day 3 Practice
DP4  - Day 4 Practice
DP5A - Day 5 Practice A
DP5B - Day 5 Practice B
DP5C - Day 5 Practice C
DP6  - Day 6 Practice
DP7  - Day 7 Practice

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
    elif script == "DP1":
        run_program("day_1_practice.py")
    elif script == "DP2":
        run_program("day_2_practice.py")
    elif script == "DP3":
        run_program("day_3_practice.py")
    elif script == "DP4":
        run_program("day_4_practice.py")
    elif script == "DP5A":
        run_program("day_5_practice_a.py")
    elif script == "DP5B":
        run_program("day_5_practice_b.py")
    elif script == "DP5C":
        run_program("day_5_practice_c.py")
    elif script == "DP6":
        run_program("day_6_practice.py")
    elif script == "DP7":
        run_program("day_7_practice.py")
    elif script == "DATA":
        run_program("data.py")
    elif script == "QUIT":
        END = True
print(
    """
      Script Ended"""
)
