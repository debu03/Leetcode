class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # Initialize a dictionary to store the count of each number

        num_count = {}
        
        # Count the occurrences of each number in the list
        for num in nums:
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1
        
        # Find the number that occurs only once
        for num, count in num_count.items():
            if count == 1:
                return num