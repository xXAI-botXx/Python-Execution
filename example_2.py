import random


def calc_grade():
    grades = [1,2,3,4,5,6]
    return random.choice(grades)


print(f"Student have the Grade: {calc_grade()}")