class Solution:
    # @param A : integer
    # @return a list of strings
    def fizzBuzz(self, A):
        l = [i for i in range(1,A+1)]
        for i in range(A):
            if(l[i]%3==0 and l[i]%5==0):
                l[i]="FizzBuzz"
            elif(l[i]%3==0):
                l[i]="Fizz"
            elif(l[i]%5==0):
                l[i]="Buzz"
        return l
