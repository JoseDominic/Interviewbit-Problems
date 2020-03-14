#Kadane's algorithm

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        max_ending_here=0
        max_so_far =0
        for i in A:
            max_ending_here =max_ending_here + i
            if(max_ending_here<0):
                max_ending_here = 0
            if(max_ending_here>max_so_far):
                max_so_far = max_ending_here
        if(max_so_far==0):
            A = sorted(A)
            max_so_far=A[len(A)-1] 
        return max_so_far
