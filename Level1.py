# Problem 1: Contains duplicate 1. (LC-217)

class Solution:
    def containsDuplicate(self, nums: List[int])-> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        else:
            return False

# Time Complexity: O(N), Space Complexity: constant O(N)
# Explanation of code: Iterate through each element in the list (nums). For each element it checks if element already exsists in the set. If it does, duplicate encountered, if not element is added to the set. If no duplicates found, return False.
# Why Hashset?: Optimizing for time complexity without modifying the array, O(1) cost for lookup operation & insertion. Better than nested for loops. O(N^2), also avoids sorting the array which would've costed O(N Log N).

# To optimize for Space Complexity & if modifying the array is allowed:
class Solution:
    def containsDuplicate(self, nums:List[int])-> bool:
    nums.sort()
    for i in range(1,len(nums)):
        
        if nums[i]==nums[i-1]:
            return True
    else:
        return False

# Problem 2: Contains duplicate 2







# Problem 3: Contains duplicate 3

