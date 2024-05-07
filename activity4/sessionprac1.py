from numpy import array, empty, copy
from pylab import plot, show, xlabel, ylabel, linspace

def gaussian_Elim(A, v):
    N = len(v)

    # Gaussian elimination
    for m in range(N):
        largest = abs(A[m, m])
        largest_row = m
        for i in range(m + 1, N):
            if abs(A[i, m]) > largest:
                largest = abs(A[i, m])
                largest_row = i

    if largest_row != m:
        current_row = copy(A[i,m])
        A[m, :] = A[largest_row, :]
        A[largest_row, :] = current_row
        v[m], v[largest_row] = v[largest_row], v[m]

    for i in range(m + 1, N):
        factor = A[i, m]/A[m, m]
        for j in range(m, N):
            A[i, j] -= A[m, j]*factor
        v[i] -= v[m]*factor

    # Backsubstitution
    x = empty(N, float)
    for m in range(N - 1, -1, -1):
        x[m] = v[m]
        for i in range(m + 1, N):
            x[m] -= A[m, i]*x[i]
        x[m] /= A[m, m]
    return x

# Constants
N = 3
A = array([[2.0, 1.0, 4.0], [3.0, 4.0, -1.0], [1.0, 3.0, 5.0]])
v = array([1.0, -2.0, 3.0])

# Solve
x = gaussian_Elim(A, v)
print(x)

plot(linspace(0, 1, 3), x)
xlabel("x")
ylabel("y")
show()