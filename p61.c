/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *rotateRight(struct ListNode *head, int k)
{
    if (!head || !head->next || k == 0)
        return head;

    struct ListNode *tail = head;
    int length = 1;
    while (tail->next)
    {
        tail = tail->next;
        length++;
    }
    tail->next = head;
    k = k % length;
    if (k == 0)
    {
        tail->next = NULL;
        return head;
    }
    struct ListNode *newTail = head;
    for (int i = 0; i < length - k - 1; i++)
    {
        newTail = newTail->next;
    }
    struct ListNode *newHead = newTail->next;
    newTail->next = NULL;

    return newHead;
}