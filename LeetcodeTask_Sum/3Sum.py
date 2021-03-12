class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # result are initially made as a set
        res = set()
        # sort nums. By doing so, in the outer loop we can ignore any number > 0. 
        # same numbers are listed next to each other
        nums.sort()
        for index1 in range(len(nums)):
            num1 = nums[index1]
            # it is impossible to sum up 3 positive integers to get 0, so if the samllest start number is greater than 0, we stop
            if num1 > 0:
                break
            # for a given number x at index i, we will examine all possible combinations from the sublist starting at index i+1;
            # so if nums[i+1] is equal to nums[i], we can skip nums[i+1] because the result would be the same as what we get from num[x]
            if index1 == 0 or num1 != nums[index1 - 1]:
                target = 0 - num1
                self.twoSum(nums, index1, res)
        return res
    
    def twoSum(self, nums, index1, res):
        target = 0 - nums[index1]
        seen = set()
        for num2 in nums[index1+1:]:
            if target - num2 in seen:
                # Here we can see the reason why we made res a set. Even if there two triplets are the same(same items and same order), only one would be stored in the set
                res.add((nums[index1], num2, target-num2))
            seen.add(num2)
        