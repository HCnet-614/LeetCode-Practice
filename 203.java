class Solution {
    public ListNode removeElements(ListNode head, int val) {
        ListNode dummy = new ListNode(0); // 0为任意值，不影响操作 / 0 is an arbitrary value and does not affect the operation
        dummy.next = head;
        ListNode prev = dummy;
        while(head != null){
            if (head.val == val){
                prev.next = head.next;
                head = head.next;
            }else{
                prev = head;
                head = head.next;
            }
        }
        return dummy.next;
    }
}
