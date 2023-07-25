class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Hash map to track all of the numbers already seen while traversing the array
        seen = {}

        # Traverse all elements in the array
        for index, num in enumerate(nums):
            difference = target - num
            # Check if the two sum pair has been found in a previous part of the array
            if difference in seen:
                return [index, seen[difference]]
            seen[num] = index
        
        # Exactly one solution is guaranteed to exist. Raise an exception since no solution has been found
        raise Exception("No solution found")

# Complexity Analysis
# n - the number of elements in the array nums
# Time Complexity - O(n)
# Space Complexity - O(n)