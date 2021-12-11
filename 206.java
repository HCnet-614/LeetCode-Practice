class Solution {
   public ListNode reverseList(ListNode head) {
        ListNode pre = head;  //  request node
        ListNode cur = null;
        ListNode t;
        while(pre != null){
            t = pre.next;   // Record next node
            pre.next = cur;  // Refers to the previous node
            cur = pre;   // 两个节点都前进一位 / Both nodes move forward
            pre = t;
        }
        return cur;
    }
}
