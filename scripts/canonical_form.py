import numpy as np

# Define the symmetric matrix A
A = np.array([[2, 1],
              [1, 2]])

# Step 2: Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

# Eigenvalues should be real for symmetric matrices
print("Eigenvalues:", eigenvalues)

# Step 3: Form the matrix P from normalized eigenvectors
P = eigenvectors

# Since eigenvectors might not be normalized, let's normalize them
P = P / np.linalg.norm(P, axis=0)

# Step 4: Transform to canonical form
D = np.diag(eigenvalues)  # Diagonal matrix with eigenvalues
canonical_form = P.T @ A @ P  # This should be close to D due to numerical precision

print("Canonical Form (D):")
print(canonical_form)

# To express the quadratic form in terms of new variables y
# Suppose x = [x1, x2], then y = P.T @ x
x = np.array([1, 2])  # Example vector x
y = P.T @ x  # Transform x to y

# Original quadratic form Q(x) = x.T @ A @ x
Q_original = x.T @ A @ x
print("Original Quadratic Form Q(x):", Q_original)

# Canonical form Q(y) = y.T @ D @ y
Q_canonical = y.T @ D @ y
print("Canonical Quadratic Form Q(y):", Q_canonical)