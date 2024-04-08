from numpy import array, empty, abs

A = array([[2, 1, 4, 1],
           [3, 4, -1, -1],
           [1, -4, 1, 5],
           [2, -2, 1, 3]], float)

V = array([-4, 3, 9, 7], float)
N = len(V)

# Gaussian Elimination with partial pivoting
for m in range(N):
    # Find the pivot row with the largest absolute value in the current column
    pivot_row = m
    for i in range(m + 1, N):
        if abs(A[i, m]) > abs(A[pivot_row, m]):
            pivot_row = i

    # Swap rows if necessary
    if pivot_row != m:
        A[[m, pivot_row]] = A[[pivot_row, m]]
        V[[m, pivot_row]] = V[[pivot_row, m]]

    # Divide by the diagonal element
    div = A[m, m]
    A[m, :] /= div
    V[m] /= div

    # Now subtract from lower rows
    for i in range(m + 1, N):
        mult = A[i, m]
        A[i, :] -= mult * A[m, :]
        V[i] -= mult * V[m]

# Backsubstitution
x = empty(N, float)
for m in range(N - 1, -1, -1):
    x[m] = V[m]
    for i in range(m + 1, N):
        x[m] -= A[m, i] * x[i]

print("The x values are: (w,x,y,z) = ", x)