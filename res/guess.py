from wypp import *
import unittest
import random

rand_n = random.randint(1, 100)
RUNNING = True

while RUNNING:
    guess = int(input("Rate eine Zahl: "))

    if guess == rand_n:
        RUNNING = False
        print(f"Super {rand_n} ist die gesuchte Zahl!")
    elif guess > rand_n:
        print("Deine Zahl ist noch zu hoch!\n")
    elif guess < rand_n:
        print("Deine Zahl ist noch zu klein!\n")