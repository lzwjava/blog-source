import numpy as np

A = np.array([[2, 1], [1, 2]])

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors: ", eigenvectors)
print("Eigenvector Norms:", np.linalg.norm(eigenvectors, axis=0))

# Check if the eigenvalues are correct by verifying the characteristic equation
characteristic_polynomial = np.poly(A)
computed_characteristic_polynomial = np.poly(eigenvalues)

print("Characteristic Polynomial of A:", characteristic_polynomial)
print(
    "Computed Characteristic Polynomial from Eigenvalues:",
    computed_characteristic_polynomial,
)


# Compare the coefficients of the characteristic polynomials
if np.allclose(characteristic_polynomial, computed_characteristic_polynomial):
    print("Eigenvalues are correct: The characteristic polynomial matches.")
else:
    print(
        "Eigenvalues might be incorrect: The characteristic polynomial does not match."
    )


P = eigenvectors / np.linalg.norm(eigenvectors, axis=0)

print("Normalized Eigenvectors (P):")
print(P)

D = np.diag(eigenvalues)
canonical_form = P.T @ A @ P

print("Canonical Form (D):")
print(canonical_form)

x = np.array([1, 2])

print("Original Vector x:")
print(x)

y = P.T @ x

print("Transformed Vector y:")
print(y)

Q_original = x.T @ A @ x
print("Original Quadratic Form Q(x):", Q_original)

Q_canonical = y.T @ D @ y
print("Canonical Quadratic Form Q(y):", Q_canonical)

print(
    "Difference between Q_original and Q_canonical:", np.abs(Q_original - Q_canonical)
)
