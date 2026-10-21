class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Anagram: words have the same exact letters in them just in different order
        - sort each word in the list alphabetically 
        '''
        hashA = {}
        for text in strs:
            # For each string in the array, sort them alphabetically
            sorted_text = "".join(sorted(text))
            # If the sorted anagram isn't in the hash yet, create an empty array for it and all the other   words that are apart of that
            if sorted_text not in hashA:
                # Create an empty list for it
                hashA[sorted_text] = []
            # The sorted text already exists as a key in the dictionary, so we can add the OG word onto there
            hashA[sorted_text].append(text)
    # Now we return the values of everything within a list BUT we have to specify that it's gonna come out as a list
        return list(hashA.values())