import numpy as np


def multiply_matrices(matrix1, matrix2):
    try:
        result = np.dot(matrix1, matrix2)
        return result
    except ValueError:
        print("Error: Matrices cannot be multiplied due to incompatible dimensions.")
        return None


def add_matrices(matrix1, matrix2):
    try:
        result = np.add(matrix1, matrix2)
        return result
    except ValueError:
        print("Error: Matrices cannot be added due to incompatible dimensions.")
        return None


def subtract_matrices(matrix1, matrix2):
    try:
        result = np.subtract(matrix1, matrix2)
        return result
    except ValueError:
        print("Error: Matrices cannot be subtracted due to incompatible dimensions.")
        return None


def transpose_matrix(matrix):
    return np.transpose(matrix)


def inverse_matrix(matrix):
    try:
        result = np.linalg.inv(matrix)
        return result
    except np.linalg.LinAlgError:
        print("Error: Matrix is not invertible.")
        return None


def qr_decomposition(matrix):
    try:
        q, r = np.linalg.qr(matrix)
        return q, r
    except np.linalg.LinAlgError:
        print("Error: QR decomposition failed.")
        return None, None


if __name__ == "__main__":
    matrix1 = np.array([[1, 2], [3, 4]])
    matrix2 = np.array([[5, 6], [7, 8]])

    print("Matrix 1:")
    print(matrix1)

    print("\nMatrix 2:")
    print(matrix2)

    print("\nMatrix Multiplication:")
    product = multiply_matrices(matrix1, matrix2)
    if product is not None:
        print(product)

    print("\nMatrix Addition:")
    sum_matrix = add_matrices(matrix1, matrix2)
    if sum_matrix is not None:
        print(sum_matrix)

    print("\nMatrix Subtraction:")
    diff = subtract_matrices(matrix1, matrix2)
    if diff is not None:
        print(diff)

    print("\nTranspose of Matrix 1:")
    print(transpose_matrix(matrix1))

    print("\nInverse of Matrix 1:")
    inv = inverse_matrix(matrix1)
    if inv is not None:
        print(inv)

    # Example of Eigenvalues and Eigenvectors
    print("\n\nExample of Eigenvalues and Eigenvectors Calculation:")

    matrix3 = np.array([[9, 10], [11, 12]])
    print("\nMatrix 3:")
    print(matrix3)

    eigenvalues, eigenvectors = np.linalg.eig(matrix3)
    print("\nEigenvalues:")
    print(eigenvalues)

    print("\nEigenvectors:")
    print(eigenvectors)

    reconstructed_matrix = (
        eigenvectors @ np.diag(eigenvalues) @ np.linalg.inv(eigenvectors)
    )
    print("\nReconstructed Matrix:")
    print(reconstructed_matrix)

    # Example of QR Decomposition
    print("\n\nExample of QR Decomposition:")
    matrix4 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("\nMatrix 4:")
    print(matrix4)

    Q, R = qr_decomposition(matrix4)
    if Q is not None and R is not None:
        print("\nQ (Orthogonal Matrix):")
        print(Q)
        print("\nR (Upper Triangular Matrix):")
        print(R)
