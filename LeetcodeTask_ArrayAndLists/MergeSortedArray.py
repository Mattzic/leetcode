class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # print(id(nums1))
        # nums1 = nums1 + nums2
        # nums1.sort()
        # nums1 = [x for x in nums1 if x != 0]
        # print(nums1)
        # print(id(nums1))
        
        # 答案要输出原地址的列表对象,所以用index修改
        # index = m
        # while index < len(nums1):
        #     nums1[index] = nums2[index - m]
        #     index += 1
        # nums1.sort()
        
        index1 = 0
        index2 = 0
        indexcp = 0
        nums1_cp = nums1[:m]
        while index1 < (m + n):
            if (index2 >= n) or ((indexcp < m) and (nums1_cp[indexcp] <= nums2[index2])):
                nums1[index1] = nums1_cp[indexcp]
                index1 += 1
                indexcp += 1
            # elif (indexcp < m) and (nums1_cp[indexcp] <= nums2[index2]):
            #     nums1[index1] = nums1_cp[indexcp]
            #     index1 += 1
            #     indexcp += 1
            else:
                nums1[index1] = nums2[index2]
                index1 += 1
                index2 += 1