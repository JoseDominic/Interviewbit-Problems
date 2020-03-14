class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        r0 = [1]
        k = A
        if(k==0):
            return r0
        r1 = []
        for i in range(0,k):
            r1 = [0]*(len(r0)+1)
            for j in range(len(r1)):
                r1[j] = 0
                if(j-1>=0):
                    r1[j]+=r0[j-1]
                if(j<len(r0)):
                    r1[j]+=r0[j]
            r0 = r1.copy()
        return r1