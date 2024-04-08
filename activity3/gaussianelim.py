from numpy import array,empty

A = array([[2,1,4,1],
           [3,4,-1,-1],
           [1,-4,1,5],
           [2,-2,1,3]],float)

V = array([-4,3,9,7],float)
N = len(V)

#Gaussian Elimination
for m in range(N):

    #Divide by the diagonal element
    div = A[m,m]
    A[m,:] /= div
    V[m] /= div

    #Now subtract from lower rows
    for i in range(m+1,N):
        mult = A[i,m]
        A[i,:] -= mult*A[m,:]
        V[i] -= mult*V[m]

#Backsubstitution
x = empty(N,float)
for m in range(N-1,-1,-1):
    x[m] =V[m]
    for i in range(m+1,N):
        x[m] -= A[m,i]*x[i]

print("The x values are: (w,x,y,z) = ",x)