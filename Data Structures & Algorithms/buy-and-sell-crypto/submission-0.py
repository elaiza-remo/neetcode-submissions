class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # BUY on lowest number in prices
        # SELL on the highest number in prices AFTER index of buying
        
        # RETURN the maximum profit you can achieve, 0 if you're at a loss

        # If we use sliding window for this, we gotta keep track of left and right
        left = 0
        right = 0
        maxProfit = 0
        '''
        Left index is the initial/default "lowest" buy price 
        If right index is LOWER than the left index, then increase left index so that the lowest value      changes to the actual lowest value SO FAR 
        Increase the right index, if its lower THEN repeat above
        If the right index is greater then --> we have PROFIT! set maxProfit to prices[rightIndex] - prices[leftIndex]
        Keep increasing the right index to see if there's a lower BUY price
        do a maxProfit = max(maxProfit, right - left)
        '''
        while right < len(prices):
            # Going through the whole list
            # Increasing the index
            # If the right index is a better buying price, then move the left index to where the right index is and then increase the right index by 1
            if prices[right] <= prices[left]:
                left = right
            # If the right index is NOT a better buying price, left is still the lowest, and this means that there will be profit from this, so store the profit
            else:
                maxProfit = max(maxProfit, prices[right] - prices[left])
                # No need to move left here cause left is still the most optimal buying price (lowest one in the list so far)
            right += 1 
        return maxProfit

            