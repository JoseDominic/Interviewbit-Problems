class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        B = list(str(A))
        B = B[::-1]
        if(A<0):
            x = B.pop()
            B.insert(0,'-')
        B = ''.join
        B = int(B)
        if (len(bin(B)) -2)>32:
            return 0
        return B