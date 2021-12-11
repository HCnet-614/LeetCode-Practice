class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0) # 0为任意值，不影响操作 / 0 is an arbitrary value and does not affect the operation
        dummy.next = head
        prev = dummy
        while(head != None):
            if(head.val == val):
                prev.next = head.next
                head = head.next
            else:
                prev = head
                head = head.next
        return dummy.next
