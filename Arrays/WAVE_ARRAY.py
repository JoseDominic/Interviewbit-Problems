#return array such that a1 >= a2 <= a3 >= a4...
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        A = sorted(A)
        L = [0]*len(A)
        first=0
        count=0
        second=1
        while(1):
            if(count>=len(A)):
                break
            if(second>=len(A)):
                second-=1
            L[first] = A[second]
            #print(second)
            if(second<len(A)):
                L[second] = A[first]
            first+=2
            second+=2
            count+=2
            #print(count)
        return L