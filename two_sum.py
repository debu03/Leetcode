class Solution:
    def twoSum(self, nums, target): #create a list to search from and traget sum
        
        hashMap= {} #create a dictionary called hashMap to map key and value
        for index, num in enumerate(nums): #iterate over enumerate-->get index of num in list
            diff = target - num #if diff is present in list means sum is posible
            if diff in hashMap: 
                return [hashMap[diff], index] #return index of hashmap
            hashMap[num] = index #add index to hashmap
