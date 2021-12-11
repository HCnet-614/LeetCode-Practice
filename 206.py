class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = head       # 申请节点 / Request node
        cur = None
        while(pre != None):
            t = pre.next   # 记录下一个节点 / Record next node
            pre.next = cur  # 指到前一个节点 / Refers to the previous node
            cur = pre   # 两个节点都前进一位 / Both nodes move forward
            pre = t
        return cur
