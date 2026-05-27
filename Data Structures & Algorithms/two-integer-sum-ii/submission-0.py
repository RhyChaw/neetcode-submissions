class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        indices = []

        while left < right:
            summ = numbers[left] + numbers[right]
            if summ == target:
                indices.append(left + 1)
                indices.append(right + 1)
                return indices
            if summ > target:
                right -= 1
            else:
                left += 1
        return indices
        
        


