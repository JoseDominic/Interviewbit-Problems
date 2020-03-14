def GCD(A, B):  
    if A == 0 : 
        return B  
    return GCD(B%A, A) 
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self,A, B):  
        return GCD(A,B)
