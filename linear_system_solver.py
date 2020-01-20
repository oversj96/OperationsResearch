"""linear_system_solver.py: A python script that will accept a number of
 unknown variables and a number of equations and solve the system."""

__author__    = "Justin Overstreet"
__copyright__ = "oversj96.github.io"

from sympy import symbols, sympify, Eq, solve
x, y = symbols("x y")

import numpy as np

# Used a global string for the header so that I wouldn't need 
# to keep passing this information around
header = "      Math 371\n"\
         "    Spring 2020\n" \
         "Linear System Solver\n" \
         " Justin Overstreet\n"


def get_system():
    am = []
    bm = []
    print("After the user inputs the values for the A and B matrices, "\
          "the program will determine")
    print("a solution to the system of two equations and two unknowns.")
    print("Variables to input are: a, b, c, d, r, and s and will" 
          " take the form below.")
    print("ax + by = r")
    print("cx + dy = s")
    am.append(input("Please input 'a': "))
    am.append(input("Please input 'b': "))
    bm.append(input("Please input 'r': "))
    am.append(input("Please input 'c': "))
    am.append(input("Please input 'd': "))  
    bm.append(input("Please input 's': "))
    am = list(map(int, am))
    bm = list(map(int, bm))
    return am, bm


def solve_with_matrices(a, b):
      if is_multiple(a[0], a[2]) and is_multiple(a[1], a[3]):
            print("The system has no solutions: lines are parallel")
            return None        
      a = np.matrix(a).reshape((2, 2))
      b_matrix = np.matrix(b).reshape((2, 1))
      try:
            inverse_matrix = np.linalg.inv(a)
      except np.linalg.LinAlgError:
            print("Matrix is singular and does not have a unique solution:" \
             " infinitely many solutions")
            return None
      solutions = inverse_matrix * b_matrix
      print(f"x = {solutions[0,0]:.3f}, y = {solutions[1,0]:.3f}")
      print(f"{a[0,0]:.3f}*{solutions[0,0]:.3f} + {a[0,1]:.3f}*{solutions[1,0]:.3f} = "\
            f" {a[0,0]*solutions[0,0] + a[0,1]*solutions[1,0]:.3f}")
      print(f"{a[1,0]:.3f}*{solutions[0,0]:.3f} + {a[1,1]:.3f}*{solutions[1,0]:.3f} = "\
            f" {a[1,0]*solutions[0,0] + a[1,1]*solutions[1,0]:.3f}")          
      return solutions


def is_multiple(x, y):
      if x == 0 or y == 0:
            return False
      x, y = abs(x), abs(y)
      if x > y:
            return x % y == 0
      else:
            return y % x == 0


if __name__ == "__main__":   
    while True:
      print()
      print(header)
      answer = input("Do you wish to solve a new system? [Y]es/[N]o: ").lower()
      if answer.startswith('y'):
            am, bm = get_system()
            solve_with_matrices(am, bm)
      else:
            break


