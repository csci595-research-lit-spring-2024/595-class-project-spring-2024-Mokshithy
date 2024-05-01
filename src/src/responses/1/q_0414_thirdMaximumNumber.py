class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unique_nums = list(set(nums))
        if len(unique_nums) < 3:
            return max(unique_nums)
        unique_nums.sort()
        return unique_nums[-3]