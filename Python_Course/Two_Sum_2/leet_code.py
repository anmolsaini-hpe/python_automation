class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        while left < right :
            sum = nums[left] + nums[right]
            if sum == target:
                return [left,right]
            elif sum > target :
                right -= 1
            else:
                left += 1