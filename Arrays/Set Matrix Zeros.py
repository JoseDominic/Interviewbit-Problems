class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        r = len(A)
        c = len(A[0])
        R , C = [],[]
        for i in range(r):
            if 0 in A[i]:
                R.append(i)
        for j in range(c):
            for i in range(r):
                if A[i][j] ==0:
                    C.append(j)
                    break
        for i in R:
            A[i] = [0]*c
        for i in C:
            for j in range(r):
                A[j][i]=0
        return A
