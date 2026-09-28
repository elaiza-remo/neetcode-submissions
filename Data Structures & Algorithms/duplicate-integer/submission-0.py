class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Return true if any value appears more than once in the array
        unique_values = []
        for value in nums:
            if value not in unique_values:
                # if the number is not in the unique values yet then add it onto there
                unique_values.append(value)
            elif value in unique_values:
                # the number exists in the unique_values list already
                return True
        return False

        