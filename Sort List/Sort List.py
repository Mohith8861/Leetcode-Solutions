// https://leetcode.com/problems/sort-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        sept = head
        l = []
        while head:
            l.append(head.val)
            head = head.next
        l.sort()
        while l:
            sept.val = l.pop(0)
            sept = sept.next
        return temp

        

        