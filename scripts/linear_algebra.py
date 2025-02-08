import numpy as np

def multiply_matrices(matrix1, matrix2):
  try:
    result = np.dot(matrix1, matrix2)
    return result
  except ValueError:
    print("Error: Matrices cannot be multiplied due to incompatible dimensions.")
    return None

if __name__ == '__main__':
  matrix1 = np.array([[1, 2], [3, 4]])
  matrix2 = np.array([[5, 6], [7, 8]])

  product = multiply_matrices(matrix1, matrix2)

  if product is not None:
    print("Matrix 1:")
    print(matrix1)
    print("Matrix 2:")
    print(matrix2)
    print("Product:")
    print(product)
