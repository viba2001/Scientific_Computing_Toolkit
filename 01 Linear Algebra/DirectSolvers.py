from VectorClass import Vector
from MatrixClass import Matrix

def gaussian_elimination(A,b):
    """
    Gaussian elimination or Row reduction method is used to solve
    A x = b
    by reducing the matrix A to row echolon form.

    Inputs: 
    A - Matrix object
    b - Vector object

    Outputs:
    U - Modified A Matrix
    c - Modified b Vector
    """
    Nrow = A.rows()
    Ncol = A.cols()
    Mat  = A.data

    # Step 1: Reduce the matrix to an upper matrix form 
    for i in range(Nrow):
        # Select the pivot = [i,i] element
        row_i = A.row(i)
        pivot = row_i.data[i]
        if pivot == 0:
            raise ValueError("Zero pivot encountered.")
        
        for j in range(i+1,Nrow):
            row_j   = A.row(j)
            factor  = (row_j[i] / pivot)
            row_new = row_j.subtract(row_i.scale(factor))
            A       = A.replace_row(j, row_new)
            b[j]    = b[j]- b[i]*(factor)
    
    # Rename the original matrix and vector since they are modified
    U = A
    c = b

    return U, c

def backward_substitution(U,c):
    """Function to solve the linear system U x = c where U & c have undergone Gaussian Elimination."""

    Nvar  = c.size()
    x     = [0] * Nvar
    for i in range(Nvar-1, -1, -1):
        s = 0
        for j in range(i+1, Nvar):
            s +=  x[j] * U.data[i][j]
        if U.data[i][i] == 0:
            raise ValueError("Matrix is singular. Cannot perform back substitution.")
        x[i] = (c.data[i] - s) / U.data[i][i]

    return Vector(x)       

def forward_substitution(L, c):
    """Function to solve the linear system L x = c where L is an lower triangular matrix."""

    Nvar  = c.size()
    x     = [0] * Nvar
    for i in range(Nvar):
        s = 0
        for j in range(i):
            s += L[i][j] * x[j]
        if L.data[i][i] == 0:
            raise ValueError("Matrix is singular. Cannot perform forward substitution.")
        x[i] = (c[i]-s)/L[i][i]

    return Vector(x) 

    #Gaussian Elimination with Partial Pivoting
    #LU Decomposition (Doolittle)
    #Solve using LU
    #Cholesky Decomposition