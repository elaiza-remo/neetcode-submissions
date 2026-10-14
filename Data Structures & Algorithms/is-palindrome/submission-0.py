class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        Using 2 pointers so one pointer at the beginning and another pointer at the end
        STOP when: 
        1) the pointers overlap
        2) the pointers don't equal each other

        First:
        - remove the spaces and non-alpha characters
        Second: 
        - create the pointers
        '''
        s = "".join(char for char in s if char.isalnum()).lower()
        
        # 2. Correctly initialize the pointers
        left = 0
        right = len(s) - 1
        
        # 3. Loop until pointers meet or cross
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
            
        return True


