class Solution:
    # @param A : integer
    # @return an integer
    def isPalindrome(self, A):
        if(A<0):
            return 0
        x = list(str(A))
        if(x==x[::-1]):
            return 1
        else:
            return 0
