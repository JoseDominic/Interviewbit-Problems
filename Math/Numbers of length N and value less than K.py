class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        c = str(C)
        c = list(c)
        count=0
        if(B==1):
            for i in A:
                if i<C:
                    count+=1
            return count
        if(B>len(c)):
            return 0
        if(B<len(c)):
            if 0 in A:
                return (len(A)-1)*(len(A)**(B-1))
            else:
                return len(A)**B
        total=0
        count=0
        i=0
        less=0
        while(1):
            less=0
            count=0
            if i>=B:
                break
            for j in range(len(A)):
                if i==0:
                    if A[j]<int(c[i]) and A[j]!=0:
                        less+=1
                else:
                    if A[j]<int(c[i]):
                        less+=1
            count+=less*(len(A)**(B-i-1))
            total+=count
            if int(c[i]) in A:
                i+=1
            else:
                break
        return total
                   
            
