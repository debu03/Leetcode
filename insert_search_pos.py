class Solution:
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if nums[i]==target: 
                return i
            elif nums[i]>target:
                return i   
            else:
                j=len(nums)
        return j  