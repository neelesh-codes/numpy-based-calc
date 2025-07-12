from math import *
import numpy as np


details = np.load("D:\\AI Enginerring cource\\numpy based calc\\user Data\\activation.npy")
class Calculator:
    def basic_clalc(self):
        print("You want to do basic calculation that's ok.")
        print("Let' start now ")

        user_old_new = input("Have you ever used this calculator before: y/n")
        if user_old_new == 'y':
            expr = int(input("enter the expression  here (no alphabetic symbol): "))
            result = eval(expr)
            print(f"The result is here MR. {details[0]}")
            

if __name__ == "__main__":
    print("Welcome to the app: let's start now!")
    print("Type of calculation: (in this app)")
    print("1: on simple numbers. (b)")
    print("2: on matrices. (m)")
    print("3: on vector. (v)")
    type_of_calc = input("Which type of calcutlation you want to do: b/m/v")
    print("So you want to do this: ", type_of_calc)

    if type_of_calc == 'b':
        pass
