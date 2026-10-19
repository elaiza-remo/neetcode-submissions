class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ''' 
        2 strings are anagrams if they contain the same characters 

        - can we order strings in python? Yep
        Order the string, see if they match
    
        '''
        sortedS = ''.join(sorted(s))
        sortedT = ''.join(sorted(t))
        return sortedS == sortedT