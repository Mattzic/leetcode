# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 比较简单, merge sort简化版
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        cur_head = head
        while l1 and l2:
            if l1.val <= l2.val:
                cur_head.next = l1
                l1 = l1.next
            else:
                cur_head.next = l2
                l2 = l2.next
            cur_head = cur_head.next
        cur_head.next = l1 or l2
        return head.next