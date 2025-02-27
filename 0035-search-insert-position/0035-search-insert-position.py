class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2
        end = len(nums) - 1
        while left <= right:
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                if mid == end:  # edge case
                    return end + 1
                if nums[mid + 1] > target:  # target belongs inbetween
                    return mid + 1
                left = mid + 1
                mid = (left + right) // 2  # keep searching
            elif nums[mid] > target:
                if mid == 0:  # edge case
                    return 0
                if nums[mid - 1] < target:  # target belongs inbetween
                    return mid
                right = mid - 1
                mid = (left + right) // 2  # keep searching
