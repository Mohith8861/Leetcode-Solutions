// https://leetcode.com/problems/reverse-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = []
        temp = head
        while(temp):
            s.append(temp.val)
            temp = temp.next
        R = head
        while s:
            R.val = s.pop()
            R = R.next
        return head
