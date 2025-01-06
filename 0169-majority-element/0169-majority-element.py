from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        count_dict = Counter(nums)
        for num in count_dict:
            if count_dict[num] > n // 2:
                return num
        return None
