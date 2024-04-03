// https://leetcode.com/problems/merge-two-sorted-lists

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        s = []
        if(not list1 and not list2):
            return None
        while list1 and list2:
            if(list1.val >= list2.val):
                s.append(list2.val)
                list2 = list2.next 
            else:
                s.append(list1.val)
                list1 = list1.next
        while list1:
            s.append(list1.val)
            list1 = list1.next
        while list2:
            s.append(list2.val)
            list2 = list2.next 
        head = ListNode(s.pop(0))
        sol = head
        while s:
            sol.next = ListNode(s.pop(0))
            sol = sol.next
        return head