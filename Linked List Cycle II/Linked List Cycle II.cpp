// https://leetcode.com/problems/linked-list-cycle-ii

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
    ListNode *detectCycle(ListNode *head) {
        ListNode *f = head;
        ListNode *s = head;
        if(s == NULL)
            return NULL;
        if(s -> next == NULL)
            return NULL;
        s = s -> next;
        f = f -> next -> next;
        while(f != NULL && f -> next != NULL){
            if(f == s)
                break;
            f = f -> next -> next;
            s = s -> next;
        }
        if(f != s)
            return NULL;
        s = head;
        while(f != s){
            if(f == s)
                break;
            f = f -> next;
            s = s -> next;
        }
        return s;
    }
};