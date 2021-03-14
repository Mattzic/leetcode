# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # bubble sort O(n**2) TLE
#     def sortList(self, head: ListNode) -> ListNode:
#         counts = 0
#         iter1 = head
        
#         while iter1:
#             iter1 = iter1.next
#             counts += 1
#         for i in range(counts - 1):
#             iter2 = head
#             for j in range(counts - i - 1):
#                 if iter2.val >= iter2.next.val:
#                     self.swap(iter2, iter2.next)
#                 iter2 = iter2.next
#         return head
    
#     def swap(self, iter1, iter2):
#         temp = iter1.val
#         iter1.val = iter2.val
#         iter2.val = temp


    # split and merge(divide and conquer)
    def sortList(self, head: ListNode) -> ListNode:
        
        # base case 
        # one test case with head == None
        if not head or not head.next:
            return head
        
        # split
        # iter2 has to be head.next
        # if iter2 = head, list with 2 elements can not be splitted. 
        # In this case, it will enter the while loop, iter1 will be the last element, l2 will be None
        iter1 = head
        iter2 = head.next
        while iter2 and iter2.next:
            iter1 = iter1.next
            iter2 = iter2.next.next            
        l2 = iter1.next
        iter1.next = None
        
        # recursive call for two sublists
        l1_sorted = self.sortList(head)
        l2_sorted = self.sortList(l2)
        
        # merge them
        return self.merge(l1_sorted, l2_sorted)
        
    # the same as Merge Two Sorted Lists
    def merge(self, l1, l2):
        head = ListNode()
        cur = head
        while l1 and l2:
            if l1.val >= l2.val:
                cur.next = l2
                l2 = l2.next
            else:
                cur.next = l1
                l1 = l1.next
            cur = cur.next
        cur.next = l1 or l2
        return head.next