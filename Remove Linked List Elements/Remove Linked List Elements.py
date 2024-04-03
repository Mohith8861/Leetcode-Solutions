// https://leetcode.com/problems/remove-linked-list-elements

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        d = ListNode(None)
        d.next = head
        node = d

        while node.next:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next

        return d.next