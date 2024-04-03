// https://leetcode.com/problems/swapping-nodes-in-a-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        first = None
        sec = None
        trec = head
        j = 0
        i = 1
        count = head
        while count:
            count = count.next
            j+=1
        while trec:
            if i == k:
                first = trec
            if i == (j-(k-1)):
                sec = trec
            i += 1
            trec = trec.next
        if first and sec:
            temp = first.val
            first.val = sec.val
            sec.val = temp
        return head
            