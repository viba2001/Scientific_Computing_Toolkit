class Vector:
    def __init__(self, v):
        """ Initializes the vector class object with input vector v which is list of numbers."""
        self.data = v

    def __repr__(self):
        return f"Vector({self.data})"
    
    def size(self):
        """Calculates and returns the size of the vector."""
        v = self.data
        n = 0
        while 1:
            try:
                temp = v[n]
                if temp is None:
                    n = n
                    break
                else:
                    n += 1
            except:
                n = n
                break
        return n
    
    def add(self, vector2):
        """ Calculates and returns the sum of given two vectors v1 and v2."""
        v1 = self.data
        v2 = vector2.data
        # Check that the two vectors are of same size. 
        n1 = self.size()
        n2 = vector2.size()
        
        if n2 != n1:
            raise ValueError("Error in computing vector addition as both vectors are not of same size.")

        result = []
        for i in range(n1):
            a = v1[i]
            b = v2[i]
            result.append(a+b)
        
        return Vector(result)
    
    def dot(self, vector2):
        """ Calculates and returns the dot product of given two vectors v1 and v2."""
        # Check that the two vectors are of same size. 
        v1 = self.data
        v2 = vector2.data
        n1 = self.size()
        n2 = vector2.size()

        if n2 != n1:
            raise ValueError("Error in computing dot product as both vectors are not of same size.")

        dot = 0
        for i in range(n1):
            dot += v1[i] * v2[i]
        
        return dot
    
    def norm(self):
        """ Computes the magnitude of the vector. """
        v = self.data
        n = self.size()
        result = 0
        for i in range(n):
            result += v[i]**2
        result = result**(0.5)

        return result
    
    def scale(self, lamda):
        """Scale given vector by a constant Lamda."""
        v = self.data
        n = self.size()
        lamda_v = []
        for i in range(n):
            lamda_v.append(v[i]*lamda)

        return Vector(lamda_v)
    
    def normalize(self):
        """Convert given vector to a unit vector."""
        v = self.data
        n = self.size()
        norm_v = self.norm()
        if norm_v == 0:
            raise ValueError("Cannot normalize the zero vector.")
        normalized_vector = []
        for i in range(n):
            normalized_vector.append(v[i]/norm_v)
        
        return Vector(normalized_vector)   

    def probability_normalize(self):
        """Probability Normalize a given vector so the sum of elements is one."""
        v = self.data
        n = self.size()
        factor = 0
        for i in range(n):
            factor += v[i]

        normalized_vector = []
        for i in range(n):
            normalized_vector.append(v[i]/factor)
        
        return Vector(normalized_vector)                

    def distance(self, vector2):
        """Calculate distance between any given 2 vectors"""
        v1 = self.data
        v2 = vector2.data
        
        n1 = self.size()
        n2 = vector2.size()
        if n2 != n1:
            raise ValueError("Error in computing dot product as both vectors are not of same size.")
        
        result = 0
        for i in range(n1):
            result += (v1[i] - v2[i])**2
        result = result**(0.5)

        return result

    # def projection():

    # def angle():

    # def cross():