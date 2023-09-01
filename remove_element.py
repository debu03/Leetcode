class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Initialize a variable to keep track of non-val elements
        
        for i in range(len(nums)):
            if nums[i] != val: #when non-val
                nums[k] = nums[i]  # Move the non-val element to the beginning
                k += 1 #increment
        
        return k
