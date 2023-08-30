class Solution:
    def plusOne(self, digits):
        
        #converting list into integer
        num = 0 
        for i in digits:
            num = num*10 + i
        #storing listed number to temp
        temp=num+1
        #converting int to list
        mylist = [int(value) for index,value in enumerate(str(temp))]
        return mylist
