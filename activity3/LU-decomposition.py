import numpy as np

def lu_decomposition(A):
    """
    Performs LU decomposition of a matrix A.

    Args:
        A: A square matrix.

    Returns:
        A tuple containing the lower triangular matrix (L) and the upper triangular matrix (U).
    """
    N = len(A)
    L = np.eye(N, dtype=float)  # Initialize L as the identity matrix
    U = A.copy()  # Create a copy of A for U

    # Gaussian Elimination
    for m in range(N):
        # Partial pivoting (not implemented here for simplicity)
        div = U[m, m]
        U[m, :] /= div
        L[m+1:, m] = U[m+1:, m] / div

        for i in range(m+1, N):
            mult = L[i, m]
            L[i, :] -= mult * U[m, :]
            U[i, :] -= mult * U[m, :]

    return L, U

# Example usage
A = np.array([[2, 1, 4, 1],
              [3, 4, -1, -1],
              [1, -4, 1, 5],
              [2, -2, 1, 3]], float)

L, U = lu_decomposition(A)

print("Lower triangular matrix (L):")
print(L)
print("\nUpper triangular matrix (U):")
print(U)