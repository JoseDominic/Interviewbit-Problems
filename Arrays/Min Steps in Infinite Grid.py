class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        distance = 0
        for i in range(len(A)-1):
            x1,x2,y1,y2 =A[i],A[i+1],B[i],B[i+1]
            distance+=max(abs(x2-x1),abs(y2-y1))
        return distance    
            