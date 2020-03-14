class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        p=-1
        for i in range(0,len(A)):
            if(i==len(A)-1):
                if(A[i]==0):
                    p=1
            elif(A[i]==A[i+1]):
                continue
            else:
                if(len(A)-(i+1))==abs(A[i]):
                    p=1
                    break
        return p