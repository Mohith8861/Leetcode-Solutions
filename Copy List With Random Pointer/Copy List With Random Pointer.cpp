// https://leetcode.com/problems/copy-list-with-random-pointer

/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        Node* Result = new Node(0);
        Node* copy = Result;
        Node* temp = head;
        unordered_map <Node*,Node*> M;
        while (temp != NULL){
            Node* c = new Node(temp -> val);
            copy -> next = c;
            M[temp] = copy -> next;
            copy = copy -> next;
            temp = temp -> next;
        }       
        Node* temp1 = head;
        copy = Result -> next;
        while (copy != NULL){
            if(temp1 -> random == NULL)
                copy -> random = NULL;
            else
                copy -> random = M[temp1 -> random];
            copy = copy -> next;
            temp1 = temp1 -> next;
        }
        return Result -> next;
    }
};