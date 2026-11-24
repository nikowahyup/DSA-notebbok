
class Solution:

    def RemoveDuplicates(self, nums : list[int]) -> int:
        
        k = 1
        sebelum = 0

        for sekarang in range(1, len(nums)):

            if nums[sekarang] != nums[sebelum]:
                sebelum += 1
                nums[sebelum] = nums[sekarang]
                k += 1

        return k 