// https://leetcode.com/problems/add-two-numbers

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* t1 = l1;
        ListNode* t2 = l2;
        ListNode* R = new ListNode(0);
        ListNode* R1 = R;
        int s1 = 0, s2 = 0, D = 0, C = 0;
        while (t1 != NULL || t2 != NULL || C > 0){
            s1 = t1 != NULL ? t1 -> val : 0;
            s2 = t2 != NULL ? t2 -> val : 0;
            int s = s1 + s2 + C;
            D = s % 10;
            C = s / 10 ;
            ListNode* v = new ListNode(D);
            R1 -> next = v;
            if(t1 != NULL)
                t1 = t1 -> next;
            if(t2 != NULL)
                t2 = t2 -> next;
            R1 = R1 -> next;
        }
        return R -> next;
    }
};