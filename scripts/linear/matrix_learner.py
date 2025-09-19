import numpy as np


def main():
    print("Running Systems of Equations examples...")
    learn_systems_of_equations()
    print("\nRunning Matrices and Operations examples...")
    learn_matrices_and_operations()
    print("\nProgram completed.")


def learn_systems_of_equations():
    # Example 1: Unique Solution
    A = np.array([[2, 3], [4, 5]])
    b = np.array([8, 14])
    try:
        x = np.linalg.solve(A, b)
        print("Unique Solution Example: x =", x)
    except np.linalg.LinAlgError:
        print("Unique Solution Example: No unique solution")

    # Example 2: Infinite Solutions
    A_inf = np.array([[2, 3], [4, 6]])
    b_inf = np.array([6, 12])
    try:
        np.linalg.solve(A_inf, b_inf)
        print("Infinite Solutions Example: Solution exists")
    except np.linalg.LinAlgError:
        print("Infinite Solutions Example: No unique solution (infinite solutions)")

    # Example 3: No Solution
    A_no = np.array([[2, 3], [4, 6]])
    b_no = np.array([6, 13])
    try:
        np.linalg.solve(A_no, b_no)
        print("No Solution Example: Solution exists")
    except np.linalg.LinAlgError:
        print("No Solution Example: No solution")


def learn_matrices_and_operations():
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])

    addition = A + B
    subtraction = A - B
    scalar_mult = 2 * A
    matrix_mult = A @ B
    transpose = A.T

    print("Matrix Addition (A + B):")
    print(addition)
    print("Matrix Subtraction (A - B):")
    print(subtraction)
    print("Scalar Multiplication (2 * A):")
    print(scalar_mult)
    print("Matrix Multiplication (A @ B):")
    print(matrix_mult)
    print("Transpose of A:")
    print(transpose)

    try:
        A_inv = np.linalg.inv(A)
        check = A @ A_inv
        print("Inverse of A:")
        print(A_inv)
        print("Check (A @ A_inv):")
        print(check)
    except np.linalg.LinAlgError:
        print("Inverse of A: Does not exist")


if __name__ == "__main__":
    main()
