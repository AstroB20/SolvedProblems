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
    public ListNode mergeNodes(ListNode head) {
        if (head == null || head.next == null) {
            return null;
        }
        ListNode dummy = new ListNode(0);
        ListNode current = dummy;
        int sum = 0;
        head = head.next;
        while (head != null) {
            if (head.val == 0) {
                if (sum > 0) {
                    current.next = new ListNode(sum);
                    current = current.next;
                    sum = 0; 
                }
            } else {
                sum += head.val; 
            }
            head = head.next; 
        }
        return dummy.next; 
    }
}