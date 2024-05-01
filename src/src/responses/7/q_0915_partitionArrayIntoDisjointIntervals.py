from typing import List

class Solution:
    
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        max_left = [0] * n
        min_right = [0] * n
        
        max_left[0] = nums[0]
        for i in range(1, n):
            max_left[i] = max(max_left[i-1], nums[i])
        
        min_right[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            min_right[i] = min(min_right[i+1], nums[i])
        
        for i in range(1, n):
            if max_left[i-1] <= min_right[i]:
                return i
