class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        x = list(A)
        # num = (len(x)-1)*26
        # num+=abs( ord(x[len(x)-1])-ord('A') + 1 )
        num=0
        exp = 0
        for i in range(len(x)-1,-1,-1):
            num+= (26**exp) +abs(ord(x[i])-ord('A'))*(26**exp)
            exp+=1
        return num
        
