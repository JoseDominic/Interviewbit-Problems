def no_of_ones(x):
    count=0
    for i in bin(x):
        if i=='1':
            count+=1
    return count
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def hammingDistance(self, A):
        l =[]
        for i in A:
            l.append('{:032b}'.format(i))
        c=0
        
        l=list(zip(*l))
        for i in l:
            a=i.count('0')
            b=i.count('1')
            c+=(2*a*b)
        return (c%1000000007)
