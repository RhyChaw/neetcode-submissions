class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)        # {1:1, 2:2, 3:3} in one line
        return [x for x, _ in count.most_common(k)]