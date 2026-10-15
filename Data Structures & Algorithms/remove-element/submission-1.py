class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''
        Remove all occurences of val in nums IN-PLACE
        
        RETURN number of elements in nums which are not VAL
        
        Don't actually have to REMOVE it, just need to get the first k parts of the array to be the elements that aren't k
        '''

        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                # Not a duplicate, then we move it to the first half of the array
                nums[k] = nums[i]
                # Increase k so that we don't replace a placed value
                k += 1
        return k
          
            