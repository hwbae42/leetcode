from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        threshold = len(nums) // 2
        for num, count in Counter(nums).items():
            if count > threshold:
                return num
