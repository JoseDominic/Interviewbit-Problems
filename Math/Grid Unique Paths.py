import math
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        #(A+B-2)C(min(A-1,B-1))
        n = A+B-2
        r = min(A-1,B-1)
        ans = math.factorial(n)/(math.factorial(r)*math.factorial(n-r))
        return int(ans)
        
