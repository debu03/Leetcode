class Solution:
    def removeDuplicates(self, nums):
        replace=1 #keeping replace varieable at pos 1 as 0th position is always unique
        for i in range(1,len(nums)): #llly start i from 1
            if nums[i-1]!=nums[i]: 
                nums[replace]=nums[i] 
                replace+=1 #increment pos of replace (shift forward)
        return replace #return replace count for getting total unique elements