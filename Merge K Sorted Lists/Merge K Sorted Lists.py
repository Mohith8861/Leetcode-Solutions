// https://leetcode.com/problems/merge-k-sorted-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l = []
        for c in lists:
            while c:
                l.append(c.val)
                c = c.next
        l.sort()
        if not l:
            return None
        temp = ListNode(l[0])
        sol = temp
        for v in l[1:]:
            temp.next = ListNode(v)
            temp = temp.next
        return sol
