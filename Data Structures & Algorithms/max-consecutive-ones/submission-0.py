class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # GOAL: find consecutive ones
        # so the nums variable is the array of items 
        # have to go through the array
        max = 0
        current = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                current += 1
            else: 
                current = 0 
            if current > max:
                max = current
        return max