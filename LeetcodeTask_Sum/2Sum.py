class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:        
        for index1 in range(len(nums)):
            num1 = nums[index1]
            num2 = target - num1
            if num2 in nums[index1+1:]:
                return [index1, nums[index1+1:].index(num2)+index1+1]