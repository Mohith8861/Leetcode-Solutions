// https://leetcode.com/problems/linked-list-cycle

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode *f = head;
        ListNode *s = head;
        if(s == NULL)
            return false;
        if(s -> next == NULL)
            return false;
        s = s -> next;
        f = f -> next -> next;
        while(f != NULL && f -> next != NULL){
            if(f == s)
                return true;
            f = f -> next -> next;
            s = s -> next;
        }
        return false;
    }
};