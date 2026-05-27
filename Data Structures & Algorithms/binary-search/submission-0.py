class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = 0

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (right + left) // 2

            if nums[mid] == target:
                index = mid
                return index
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1