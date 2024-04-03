// https://leetcode.com/problems/reverse-linked-list-ii

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if(left == right):
            return head
        l1,l = head,head
        k = right - left + 1
        while left -1 > 0:
            l = l.next
            l1 = l1.next
            left -= 1
        s = []
        while(k > 0):
            s.append(l.val)
            k -= 1
            l = l.next
        while s:
            l1.val = s.pop()
            l1 = l1.next
        return head
