# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue
class Solution: 
# ==============================================================================================       
    # method 1
    # merge every sublist one by one
#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#         length = len(lists)
#         if length == 0:
#             return None
#         i = 1
#         res = lists[0]
#         if res == None and length == 1:
#             return None
        
#         # print(res)
#         # print(lists)
#         while i < length:
#             res = self.merge(res, lists[i])
#             i += 1
#         return res
        
    
#     def merge(self, l1, l2):
#         head = ListNode()
#         cur = head
#         while l1 and l2:
#             if l1.val <= l2.val:
#                 cur.next = l1
#                 l1 = l1.next
#             else:
#                 cur.next = l2
#                 l2 = l2.next
#             cur = cur.next            
#         cur.next = l1 or l2
#         return head.next
# ============================================================================================== 
    # method 2
    # 取出所有数值放入一个list，并排序
    # 根据这个list重新创建linked list
#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#         vals = []
#         for sub_l in lists:
#             while sub_l:
#                 vals.append(sub_l.val)
#                 sub_l = sub_l.next
#         vals.sort()
#         head = cur = ListNode()
#         for v in vals:
#             cur.next = ListNode(v)
#             cur = cur.next
#         return head.next
# ==============================================================================================         
    # method 3
    # divided and conquer and merge
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        length = len(lists)
        if length == 0:
            return None
        i = 1
        res = lists[0]
        if res == None and length == 1:
            return None
        
        step = 1
        # divide and conquer，先由最小的子列两两合并，再合并他们的合并
        # 例: 第一次循环：l[0] = (l[0],l[0+1]), l[0+2*1] = (l[0+2*1],l[0+2*1+1]).....
        #     第二次循环: l[0] = (l[0], l[2]).....
        # 直到 0+ step > length
        while step < length:
            # 必须是length - step，因为合并的两个列表下标是i和i+step 
            for i in range(0, length - step, step * 2):
                lists[i] = self.merge(lists[i], lists[i+step])
            step *= 2
        return lists[0]
    
    def merge(self, l1, l2):
        head = ListNode()
        cur = head
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next            
        cur.next = l1 or l2
        return head.next
