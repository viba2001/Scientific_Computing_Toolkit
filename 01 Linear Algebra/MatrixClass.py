from VectorClass import Vector

class Matrix:
    def __init__(self, mat):
        """ Initializes the matrix class object with input matrix m which is a 2D array of numbers."""
        self.data = mat

    def __repr__(self):
        return f"Matrix ({self.data})"
    
    def __getitem__(self, index):
        return self.data[index]
    
    def shape(self):
        """Calculates and returns the shape of the matrix in [m,n]."""
        mat = self.data
        m = 0
        n = 0
        while 1:
            # Count number of columns
            try:
                temp = mat[0][n]
                if temp is None:
                    n = n
                    break
                else:
                    n += 1
            except:
                n = n
                break

        while 1:
            # Count number of rows
            try:
                temp = mat[m][0]
                if temp is None:
                    m = m
                    break
                else:
                    m += 1
            except:
                m = m
                break
        return (m,n)
    
    def rows(self):
        """ Returns the number of rows in the given matrix. Makes use of the shape() method written above."""
        rows = self.shape()[0]
        return rows
    
    def cols(self):
        """Returns the number of columns in the given matrix. Makes use of the shape() method written above."""
        cols = self.shape()[1]
        return cols

    def row(self, ind):
        """Returns 'ind' indexed row in the given matrix"""
        mat = self.data
        # Check if specified row is present in the matrix
        m = self.rows()
        if ind < m:
            # Indexed row exists
            result = mat[ind]
        else:
            raise IndexError("Row index out of bounds.")
        return Vector(result)
    
    def col(self, ind):
        """Returns 'ind' indexed column in the given matrix"""
        mat = self.data
        # Check if specified row is present in the matrix
        (m,n) = self.shape()
        result = []
        if ind < n:
            # Indexed column exists
            for i in range(m):
                temp = mat[i]
                result.append(temp[ind])
        else:
            raise IndexError("Column index out of bounds.")
        return Vector(result)
    
    def replace_row(self, ind, row):
        """Replaces "ind" indexed row of a given matrix with input "row". """
        mat = self.data
        # Check if specified row is present in the matrix
        m = self.rows()
        result = []
        if ind < m:
            # Indexed row exists
            for i in range(m):
                if i == ind:
                    result.append(row)
                else:
                    result.append(self.row(i).data)
        else:
            raise IndexError("Row index out of bounds.")
        return Matrix(result)
    
    def transpose(self):
        """Create the transpose of the existing matrix"""
        mat = self.data
        # Obtain shape of matrix
        (m,n) = self.shape()
        
        # Obtain each column as a separate Vector/list and create a matrix of these lists
        transpose = []
        for i in range(n):
            col = self.col(i)
            transpose.append(col.data)
        return Matrix(transpose)
    
    def multiply(self, mat):
        """Function to calculate matrix multiplication (m1 * m2) output"""
        mat1 = self
        mat2 = mat

        is_vector = False

        # Check compatibility of row/col size for matrix multiplication
        (m1,n1) = mat1.shape()
        if isinstance(mat2, Matrix):
            (m2,n2) = mat2.shape()
        elif isinstance(mat2, Vector):
            # Second matrix is rather a vector
            is_vector = True
            m2 = mat2.size()
            n2 = 1
        else:
            raise IndexError("Second matrix is of unknown type - neither a matrix nor a vector")

        if n1 != m2:
            raise IndexError("Matrices are not in compatible shape for multiplication.")
        else:
            # do matrix multiplication
            # Loop through each rows of first matrix, get each row, 
            # mutliply with elements of each column of second matrix
            result = []
            for i in range(m1):
                product = []
                row1 = mat1.row(i)
                for j in range(n2):
                    if is_vector == False:
                        col2 = mat2.col(j)
                    else:
                        col2 = mat2
                    product.append(row1.dot(col2))
                result.append(product)
            if is_vector == False:
                result = Matrix(result)
            else:
                # Vector multiplication should output a vector
                temp = [row[0] for row in result]
                result = Vector(temp)

        return result
                