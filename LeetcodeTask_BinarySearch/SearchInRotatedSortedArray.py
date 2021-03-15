# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         res = -1
#         if target in nums:
#             res = nums.index(target)
#         return res

# find the rotated index, split the list into two sublists and search 
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = -1
        rotate_index = self.find_r(nums)
        if rotate_index == 0:
            res = self.BS(nums, 0, len(nums)-1, target)
        elif target < nums[0]:
            lo = rotate_index
            hi = len(nums) - 1
            res = self.BS(nums, lo, hi, target)
        elif target > nums[rotate_index]:
            hi = rotate_index - 1
            lo = 0
            res = self.BS(nums, lo, hi, target)
        else:
            res =  rotate_index
        return res
    
    # find rotation index
    # rotation index: the sublist before it(exclusive) is an ascending list, the sublist after it(inclusive) is an ascending list
    # if there is only one number, the rotation index is 0
    # if the list is in ascending order, the r-index is 0
    def find_r(self, nums):
        lo = 0
        hi = len(nums) - 1
        if nums[lo] <= nums[hi]:
            return 0
        while lo <= hi: 
            mid = lo + (hi - lo) // 2
            if nums[mid] > nums[mid + 1]:
                return mid + 1
            else:
                if nums[lo] <= nums[mid]:
                    lo = mid + 1
                else:
                    hi = mid - 1
    

    def BS(self, nums, lo, hi, target):
        res = -1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                res = mid
                break
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return res
    