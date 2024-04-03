// https://leetcode.com/problems/rotate-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        i = head
        l = 1
        while i.next:
            i = i.next
            l += 1
        temp = head
        k = k % l
        if k == 0:
            return head
        for n in range(l - k - 1):
            temp = temp.next
        N = temp.next
        temp.next = None
        i.next = head
        return N
      