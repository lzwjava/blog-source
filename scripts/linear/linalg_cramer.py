import numpy as np

# Define the system of linear equations
A = np.array([[2, 1, -1], [-3, -1, 2], [-2, 1, 2]])

b = np.array([8, -11, -3])

# Calculate the determinant of A
det_A = np.linalg.det(A)

# Calculate the determinants of the matrices formed by replacing each column of A with b
det_Ax = np.linalg.det(np.column_stack((b, A[:, 1], A[:, 2])))
det_Ay = np.linalg.det(np.column_stack((A[:, 0], b, A[:, 2])))
det_Az = np.linalg.det(np.column_stack((A[:, 0], A[:, 1], b)))

# Calculate the solutions using Cramer's Rule
x = det_Ax / det_A
y = det_Ay / det_A
z = det_Az / det_A

print("Solution using Cramer's Rule:")
print(f"x = {x}")
print(f"y = {y}")
print(f"z = {z}")

# Verify the solution by solving the system using numpy's linear algebra solver
solution = np.linalg.solve(A, b)
print("\nSolution using numpy's solver:")
print(f"x = {solution[0]}")
print(f"y = {solution[1]}")
print(f"z = {solution[2]}")
