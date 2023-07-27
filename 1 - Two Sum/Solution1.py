class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Traverse all elements in the array except for the last one since it cannot make a pair
        for index in range(len(nums) - 1):
            # Traverse all remaining elements in the array
            for secondIndex in range(index + 1, len(nums)):
                # Check for the two sum solution for the current pair
                if nums[index] + nums[secondIndex] == target:
                    return [index, secondIndex]

        # Exactly one solution is guaranteed to exist. Raise an exception since no solution has been found
        raise Exception("No solution found")

# Complexity Analysis
# n - the number of elements in the array nums
# Time Complexity - O(n²)
# Space Complexity - O(1)