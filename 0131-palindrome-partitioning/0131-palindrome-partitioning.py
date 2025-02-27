class Solution:
    @cache
    def partition(self, s: str) -> List[List[str]]:
        if not s:  # all suffixes have been processed
            return [[]]
        ans = []
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:  # prefix is palindrome
                for suf in self.partition(s[i:]):  # process suffixes
                    ans.append([s[:i]] + suf)  # list adding
        return ans