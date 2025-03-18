#include <iostream>
#include <stdlib.h>

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};


class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        if (!head)
        {
            return head;
        }
        else if (!head->next)
        {
            return head;
        }

        ListNode* dummy = new ListNode();
        ListNode* ptr1 = head;
        ListNode* ptr2 = head->next;
        ListNode* tracker = dummy;

        while(ptr1 && ptr2 && ptr1->next && ptr2->next)
        {
            ListNode* ptr2_next = ptr2->next->next;
            ListNode* ptr1_next = ptr1->next->next;
            ptr1->next = nullptr;
            ptr2->next = nullptr;
            tracker->next = ptr2;
            tracker->next->next = ptr1;
            tracker = tracker->next->next;

            ptr1 = ptr1_next;
            ptr2 = ptr2_next;
        }

        if(ptr2)
        {
            tracker->next = ptr2;
            ptr2->next = nullptr;
            tracker = tracker->next;
        }

        if(ptr1)
        {
            tracker->next = ptr1;
            ptr1->next = nullptr;
            tracker = tracker->next;
        }
        
        ListNode* new_head = dummy->next;
        delete dummy;
        return new_head;
    }
};


int main()
{
    Solution* s = new Solution();
    ListNode* _1 = new ListNode(1);
    ListNode* _2 = new ListNode(2);
    ListNode* _3 = new ListNode(3);
    ListNode* _4 = new ListNode(4);
    
    _1->next = _2;
    _2->next = _3;
    _3->next = _4;

    ListNode* result = s->swapPairs(_1);

    while(result)
    {
        std::cout << result->val << std::endl;
        result = result->next;
    }
}