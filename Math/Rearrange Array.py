class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference. 
    # You do not need to return anything in this case. 
    def arrange(self, A):
        b = A[:]
        for i in range(len(A)):
            A[i]= b[A[i]]