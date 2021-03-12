# 都是two pointers, 递归更好
# 固定一个点（最外层循环），然后转换成3sum
# 内层循环如果遇到index+1和index对应的值是一样的，考虑跳过
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        index1 = 0
        while index1 < (len(nums) - 3):
            while (index1 > 0) and (nums[index1] == nums[index1-1]) and ((index1+1) < len(nums)):
                index1 += 1
            num1 = nums[index1]
            index2 = index1 + 1
            while index2 < (len(nums) - 2):
                while (index2 - 1 > index1) and (nums[index2] == nums[index2-1]) and((index2+1) < len(nums)):
                    index2 += 1
                sub_target = target - num1
                num2 = nums[index2]
                lo = index2 + 1
                hi = len(nums) - 1
                while lo < hi:
                    sub_sum = num2 + nums[lo] + nums[hi]
                    if sub_target == sub_sum:
                        res.append([num1, num2, nums[lo], nums[hi]])
                        lo += 1
                        while (nums[lo] == nums[lo-1] and lo < hi):
                            lo += 1
                        hi -= 1
                        while (nums[hi] == nums[hi+1] and hi > lo):
                            hi -= 1
                    elif sub_target > sub_sum:
                        lo += 1
                        while (nums[lo] == nums[lo-1] and lo < hi):
                            lo += 1
                    else:
                        hi -= 1
                        while (nums[hi] == nums[hi+1] and hi > lo):
                            hi -= 1
                index2 += 1
            index1 +=1
                
        return res
                         
# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
#         def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
#             res = []
#             if len(nums) == 0 or nums[0] * k > target or target > nums[-1] * k:
#                 return res
#             if k == 2:
#                 return twoSum(nums, target)
#             for i in range(len(nums)):
#                 if i == 0 or nums[i - 1] != nums[i]:
#                     for _, set in enumerate(kSum(nums[i + 1:], target - nums[i], k - 1)):
#                         res.append([nums[i]] + set)
#             return res

#         def twoSum(nums: List[int], target: int) -> List[List[int]]:
#             res = []
#             lo, hi = 0, len(nums) - 1
#             while (lo < hi):
#                 sum = nums[lo] + nums[hi]
#                 if sum < target or (lo > 0 and nums[lo] == nums[lo - 1]):
#                     lo += 1
#                 elif sum > target or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
#                     hi -= 1
#                 else:
#                     res.append([nums[lo], nums[hi]])
#                     lo += 1
#                     hi -= 1
#             return res

#         nums.sort()
#         return kSum(nums, target, 4)