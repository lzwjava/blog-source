import numpy as np

A = np.array([[2, 1],
              [1, 2]])

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors: ", eigenvectors)

P = eigenvectors / np.linalg.norm(eigenvectors, axis=0)

D = np.diag(eigenvalues)
canonical_form = P.T @ A @ P

print("Canonical Form (D):")
print(canonical_form)

x = np.array([1, 2])

y = P.T @ x

Q_original = x.T @ A @ x
print("Original Quadratic Form Q(x):", Q_original)

Q_canonical = y.T @ D @ y
print("Canonical Quadratic Form Q(y):", Q_canonical)