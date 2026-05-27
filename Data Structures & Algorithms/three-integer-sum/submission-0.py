class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i, j, k = 0, 0, 0
        result= []
        length = len(nums)
        summ = nums[i] + nums[j] + nums[k]
        # # worst case O(n3) to brute force all of them
        # # gets better with dp in O(n2)

        # for i in range(length):
        #     if i == 0:
        #         j = i + 1
        #         k = length
        
        #         if summ == 0:
        #             result.append([nums[i], nums[j], nums[k]])
        #         if summ > 0:
        #             k -= 1
        #         if summ < 0:
        #             j += 1
        #     if i != 0 and length:
        #         j = 0
        #         k = length
        #         # logic for skipping ith here
        #         if summ == 0:
        #             result.append([nums[i], nums[j], nums[k]])
        #         if summ > 0:
        #             k -= 1
        #         if summ < 0:
        #             j += 1

        #     if i == length:
        #         j = 0
        #         k = length - 1
        #         # logic for skipping ith here
        #         if summ == 0:
        #             result.append([nums[i], nums[j], nums[k]])
        #         if summ > 0:
        #             k -= 1
        #         if summ < 0:
        #             j += 1
        #     return result


        nums.sort()
        for i in range(length):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = length - 1
            while j < k:
                summ = nums[i] + nums[j] + nums[k]
                if summ == 0:
                    result.append([nums[i], nums[j], nums[k]])

                    j += 1
                    k -= 1

                    while j < k and nums[j] == nums[j-1]:
                        j += 1

                elif summ > 0:

                    k -= 1
                else:

                    j += 1
        return result