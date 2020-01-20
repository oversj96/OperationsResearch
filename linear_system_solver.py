"""linear_system_solver.py: A python script that will accept a number of
 unknown variables and a number of equations and solve the system."""

__author__    = "Justin Overstreet"
__copyright__ = "oversj96.github.io"

import numpy as np

# Used a global string for the header so that I wouldn't need 
# to keep passing this information around
header = "      Math 371\n"\
         "    Spring 2020\n" \
         "Linear System Solver\n" \
         " Justin Overstreet\n"


def get_system():
      """Obtains from the user the system they would like to solve"""
      am = []
      bm = []
      print("\nAfter the user inputs the values for the A and B matrices, "\
            "the program will determine")
      print("a solution to the system of two equations and two unknowns.")
      print("\nVariables to input are: a, b, c, d, r, and s and will" 
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
      """Solves the system by using numpy to transform data into matrices
      Matrix operations are programmed here and the solution is not obtained with
      np.solve(). Proof of concept."""
      # Check for parallel lines
      if is_multiple(a[0], a[2]) and is_multiple(a[1], a[3]):
            print("The system has no solutions: lines are parallel")
            return None        
      # Structure the coefficient data into a coefficient matrix
      a = np.matrix(a).reshape((2, 2))
      # Structure b data into the b matrix
      b_matrix = np.matrix(b).reshape((2, 1))
      # Simplest way of checking for unique solutions for the 
      # matrix turns out to be checking if it is singular or not
      try:
            inverse_matrix = np.linalg.inv(a)
      except np.linalg.LinAlgError:
            print("Matrix is singular and does not have a unique solution:" \
             " infinitely many solutions")
            return None
      # Obtain the solutions via matrix multiplication of the inversed
      # coefficient matrix.
      solutions = inverse_matrix * b_matrix
      # Display the solution data and calculate if the solutions generated truly do
      # achieve the same results as the data in the b matrix.
      print(f"x = {solutions[0,0]:.3f}, y = {solutions[1,0]:.3f}")
      print(f"{a[0,0]:.3f}*{solutions[0,0]:.3f} + {a[0,1]:.3f}*{solutions[1,0]:.3f} = "\
            f" {a[0,0]*solutions[0,0] + a[0,1]*solutions[1,0]:.3f}")
      print(f"{a[1,0]:.3f}*{solutions[0,0]:.3f} + {a[1,1]:.3f}*{solutions[1,0]:.3f} = "\
            f" {a[1,0]*solutions[0,0] + a[1,1]*solutions[1,0]:.3f}")          
      return solutions


def is_multiple(x, y):
      """Determine if the two values passed are multiples/divisors"""
      # There were many cases that had to be checked
      # If both x and y are 1, they are multiples, but if only 1 coefficient
      # is the value 1, then they are not truly multiples.
      if x == 1 and y == 1:
            return True
      if x == 1:
            return False
      if y == 1:
            return False
      # 0 cannot be a multiple of something and must be caught here, lest
      # we end up with a divide by zero error.
      if x == 0 or y == 0:
            return False
      # Test, by the modulo operator, if the values are even multiples.
      x, y = abs(x), abs(y)
      if x > y:
            return x % y == 0
      else:
            return y % x == 0


if __name__ == "__main__":   
      # Acts as the "main() {} insertion point equivalent for a c program."
      # When this file is referenced as a module, this portion will not
      # be accessed and ran; only the functions defined shall be.
      while True:
            print()
            print(header)
            answer = input("Do you wish to solve a new system? [Y]es/[N]o: ").lower()
            if answer.startswith('y'):
                  am, bm = get_system()
                  solve_with_matrices(am, bm)
            else:
                  break


