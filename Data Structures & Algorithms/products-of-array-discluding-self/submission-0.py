class Solution:
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     result = []
    #     product = 1

    #     for i in nums:
    #         customNums = nums
    #         customNums[i] = 1
    #         result[i] = product(customNums)
        
    #     return result

    # def product(self, nums: List[int]) -> int:
    #     prod = 1
    #     for num in nums:
    #         prod *= num

    #     return prod
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        
        for i in range(len(nums)):        # use index, not value
            customNums = nums.copy()       # copy so you don't modify original
            customNums[i] = 1             # set current index to 1
            result.append(self.product(customNums))  # append, not index
        
        return result

    def product(self, nums: List[int]) -> int:
        prod = 1
        for num in nums:
            prod *= num
        return prod