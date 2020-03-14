import math
class Solution:
    # @param A : integer
    # @return an integer
    def isPower(self, A):
        if(A==1):
            return 1
        flag=0
        for i in range(2,int(math.ceil(A**0.5))+1):
            sq = i*i
            count=1
            while(sq<=A):
                if(sq==A):
                    return 1
                    break
                sq = sq*i
        return flag