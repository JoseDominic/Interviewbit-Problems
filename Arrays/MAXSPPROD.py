#EFFICIENT METHOD USING STACK
class Solution:
    # @param A : list of integers
    # @return an integer
    def maxSpecialProduct(self, A):
        left = [0]*len(A)
        right = [0]*len(A)
        #print(left,right)
        stack = []
        stack.append(0)
        top=0
        #for finding left special value
        for i in range(1,len(A)-1):
            while(A[stack[top]]<=A[i]):
                stack.pop()
                #print(top)
                top-=1
                if(top==-1):
                    break
            if(len(stack)!=0):
                left[i]=stack[top]
            top+=1    
            stack.append(i)    
        stack = []
        # for finding right special value            
        stack.append(len(A)-1)
        top = 0
        for i in range(len(A)-2,0,-1):
            while(A[stack[top]]<=A[i]):
                stack.pop()
                top-=1
                if(top==-1):
                    break
            if(len(stack)!=0):
                right[i]=stack[top]
            top+=1    
            stack.append(i)    
        product = [0]*len(A)
        for i in range(0,len(A)):
            product[i]=left[i]*right[i]
        #print(left,right)
        ans = max(product)%((10**9)+7)
        return ans