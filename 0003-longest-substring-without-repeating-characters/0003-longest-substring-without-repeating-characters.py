class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max = 0
        
        for i in range(len(s)):
            length = self.longest_substrings(s[i:])
            if length > max:
                max = length
        return max

    def longest_substrings(self, s: str) -> int:
            """
            cycle through given string,
            counting longest substring with unique letters
            how to count unique letters
            set, dict, list
            """
            seen = list()
            length = 0
            for letter in s:
                if letter in seen:
                    return length
                else:
                    seen.append(letter)
                    length += 1
            return length