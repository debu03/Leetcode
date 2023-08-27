class Solution:
    def romanToInt(self, s):
        roman_dict={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000} #creation of dictionary od key:value pair
        num=0 #iniliatizing num 
        for i in range(len(s)-1): #from digit 1 to end-1
            if roman_dict[s[i]] < roman_dict[s[(i+1)]]: #if digit 1 is less than next subtract from num
                num-=roman_dict[s[i]]
            else:
                num+=roman_dict[s[i]] #else add to num
        return num+roman_dict[s[-1]] # add num and last digit at end of loop to get final ans
