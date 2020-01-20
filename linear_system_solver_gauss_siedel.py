"""linear_system_solver_gauss_siedel.py: A python script that will accept a number of unknown variables and a number of equations and 
solve the system."""

__author__    = "Justin Overstreet"
__copyright__ = "oversj96.github.io"

# Used a global string for the header so that I wouldn't need to keep passing this information around
header = "      Math 371\n"\
         "    Spring 2020\n" \
         "Linear System Solver\n" \
         " Justin Overstreet\n"


def gauss_siedel_iteration(tol, max_iters, a, b, separation=1):
    """Employs the Gauss-Siedel method of iteration to find solutions
    to linear systems."""
    # swaps equations 1 and 2 if matrix a is not diagonally dominant
    if a[1][0] > a[0][0]:
        a.reverse()
        b.reverse()
    n = len(b)
    iteration = 0
    p = [0 for j in range(0, n)]
    old_p = [0 for j in range(0, n)]
    while (iteration < max_iters) and (separation > tol):
        for r in range(0, n):
            temp = b[r]
            for c in range(0, n):
                if c != r:
                    temp -= a[r][c]*p[c]
            p[r] = temp / a[r][r]
        separation = 0
        for j in range(0, n):
            separation += abs(p[j] - old_p[j])
        for j in range(0, n):
            old_p[j] = p[j]
        iteration += 1 
    for j in range(0, n):
        print(f"x{j}: = {p[j]:.3f}")



if __name__ == "__main__":
    print(header)
    #while input("Do you wish to solve a two-unknown, two-equation system? Yes or No").lower() is 'yes':
    a = [[2, 3], [5, -4]]
    b = [8, 9]
    gauss_siedel_iteration(1e-2, 99, a, b)



