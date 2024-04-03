// https://leetcode.com/problems/reverse-nodes-in-k-group

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        le = head
        l = 0
        while le:
            l += 1
            le = le.next
        f,s = head,head
        for i in range(0,l,k):
            if(i + k > l):
                break
            st = []
            for j in range(k):
                st.append(f.val)
                f = f.next
            while st:
                s.val = st.pop()
                s = s.next
        return head     