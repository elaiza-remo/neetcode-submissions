class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        '''
        Replace every element in that array with the greatest element among the elements to its right
    
    Sliding Window - window gets smaller and smaller as we go on
    # Initially the window is arr[index:] where index = 1
    # Then the window becomes smaller by increasing the index by 1
    # Find the max of the window by replacing the currentIndex by max(window)
    '''
        for i in range(len(arr)):
            # Find max in window
            window = arr[i+1:]
            maxW = max(window, default=-1)
            arr[i] = maxW
        return arr 