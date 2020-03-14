class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, A):
        num_rows = A
        T = [[1]]
        if(num_rows==1):
            return T
        if(num_rows==0):
            return []
        for i in range(1,num_rows):
            r0 = T[i-1]
            r1 = []
            x=i+1
            for j in range(x):
                temp = 0
                if (j-1)>=0:
                    temp+=r0[j-1]
                if(j<len(r0)):
                    temp+=r0[j]
                r1.append(temp)
            T.append(r1)
        return T

