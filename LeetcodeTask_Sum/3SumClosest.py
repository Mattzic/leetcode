class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # 参考了答案的思路 two pointers，自己打的，没有直接copy
        diff = float('inf')
        nums.sort()
        for i in range(len(nums)):
            lo = i + 1
            hi = len(nums) - 1
            while (lo < hi):
                sum = nums[i] + nums[lo] + nums[hi]
                if abs(diff) > abs(target - sum):
                    diff = target - sum
                if target > sum:
                    lo += 1
                elif target < sum:
                    hi -= 1
                else:
                    break
            if diff == 0:
                break
        return target - diff

# class Solution:
#     def threeSumClosest(self, nums: List[int], target: int) -> int:
#         diff = float('inf')
#         nums.sort()
#         for i in range(len(nums)):
#             lo, hi = i + 1, len(nums) - 1
#             while (lo < hi):
#                 sum = nums[i] + nums[lo] + nums[hi]
#                 if abs(target - sum) < abs(diff):
#                     diff = target - sum
#                 if sum < target:
#                     lo += 1
#                 else:
#                     hi -= 1
#             if diff == 0:
#                 break
#         return target - diff