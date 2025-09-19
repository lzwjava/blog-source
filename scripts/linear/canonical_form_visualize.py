import numpy as np
import matplotlib.pyplot as plt

# Define the matrix A
A = np.array([[2, 1], [1, 2]])

# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

# Normalize the eigenvectors
eigenvectors_normalized = eigenvectors / np.linalg.norm(eigenvectors, axis=0)

# Create a figure and axis for plotting
plt.figure(figsize=(12, 6))

# Plot eigenvectors as arrows
plt.subplot(1, 2, 1)
plt.title("Eigenvectors")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)

# Plot each eigenvector
for ev in eigenvectors_normalized.T:
    plt.arrow(0, 0, ev[0], ev[1], width=0.05, head_width=0.1, color="r")
    plt.text(ev[0] + 0.1, ev[1] + 0.1, f"({ev[0]:.2f}, {ev[1]:.2f})", color="r")

# Create a grid for quadratic form visualization
x_values = np.linspace(-3, 3, 40)
y_values = np.linspace(-3, 3, 40)
X, Y = np.meshgrid(x_values, y_values)

# Compute Q_original
Q_original = 2 * X**2 + 2 * Y**2 + 2 * X * Y

# Compute Q_canonical
D = np.diag(eigenvalues)
P = eigenvectors
Q_canonical = np.zeros_like(Q_original)
for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        v = np.array([X[i, j], Y[i, j]])
        Q_canonical[i, j] = v @ P @ D @ P.T @ v

# Plot quadratic forms
plt.subplot(1, 2, 2)
plt.title("Quadratic Form Contours")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)

# Plot contours for Q_original and Q_canonical
levels = np.array([0.5, 1, 2, 4, 8])
cs_original = plt.contour(X, Y, Q_original, levels=levels, label="Original Q(x)")
cs_canonical = plt.contour(X, Y, Q_canonical, levels=levels, label="Canonical Q(y)")

# Add labels and legend
plt.clabel(cs_original, inline=True, fontsize=8)
plt.clabel(cs_canonical, inline=True, fontsize=8)
plt.legend()

# Show the plots
plt.tight_layout()
plt.show()
