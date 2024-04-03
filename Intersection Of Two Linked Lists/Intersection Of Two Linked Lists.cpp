// https://leetcode.com/problems/intersection-of-two-linked-lists

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
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        int l1 = 0,l2 = 0;
        ListNode* temp1 = headA;
        ListNode* temp2 = headB;
        while(temp1 != NULL){
            l1 += 1;
            temp1 = temp1 -> next;
        }
        while(temp2 != NULL){
            l2 += 1;
            temp2 = temp2 -> next;
        }
        int o = 0;
        ListNode* temp3 = headA;
        ListNode* temp4 = headB;
        if(l1 > l2){
            o = l1 - l2;
            while(o > 0)
            {
                temp3 = temp3 -> next;
                o--;
            }
        }
        else{
            o = l2 - l1;
            while(o > 0)
            {
                temp4 = temp4 -> next;
                o--;
            }
        }
        while(temp3 != NULL && temp4 != NULL){
            if(temp3 == temp4)
                return temp4;
            temp3 = temp3 -> next;
            temp4 = temp4 -> next;
        }
        return NULL;
    }
};