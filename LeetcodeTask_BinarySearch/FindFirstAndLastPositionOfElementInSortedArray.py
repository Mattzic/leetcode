# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         if target not in nums:
#             return [-1, -1]
#         res = []
#         index1 = nums.index(target)
#         index2 = len(nums) - 1 - nums[::-1].index(target)
#         res.append(index1)
#         res.append(index2)
#         return res
#==============================================================================================================================================================================
# my version of bs
# still slow
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        
        res[0] = self.searchLeftest(nums, target)
        res[1] = self.searchRightest(nums, target)
        
        return res
    
    # binary search to find the leftest index
    # the difference between normal binary search and this one is that in order to find the leftest, 
    # when mid = target, we remember mid and keep searching the left sub-list 
    def searchLeftest(self, nums, target):
        res = -1
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                res = mid
                hi = mid - 1
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        
        return res
    
    # binary search to find the rightest index
    # similar idea
    def searchRightest(self, nums, target):
        res = -1
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                res = mid
                lo = mid + 1
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return res
#==============================================================================================================================================================================