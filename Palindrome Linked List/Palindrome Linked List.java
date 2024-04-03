// https://leetcode.com/problems/palindrome-linked-list

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    private ListNode reverse(ListNode head){
        ListNode curr = head;
        ListNode next = null;
        ListNode prev = null;
        while(curr != null){
            next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }
    public boolean isPalindrome(ListNode head) 
    {
        ListNode s = head;
        ListNode f = head;
        if(head == null)
            return true;
        while(f != null && f.next != null){
            s = s.next;
            f = f.next.next;
        }
        ListNode f1 = reverse(s);
        ListNode s1 = head;
        while(f1 != null){
            if(s1.val != f1.val)
                return false;
            s1 = s1.next;
            f1 = f1.next;
        }
        return true;
    }    
}
