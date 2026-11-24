class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

class Solution:

    def AddTwoNum(self, l1 : ListNode, l2 : ListNode) -> ListNode:

        node_dummy = ListNode(0)
        current = node_dummy
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            val_1 = l1.val if l1 is not None else 0
            val_2 = l2.val if l2 is not None else 0


            total = val_1 + val_2 + carry
            carry = total // 10
            digit = total % 10


            node = ListNode(digit)
            current.next = node
            current = current.next

            if l1 is not None:
                l1 = l1.next

            if l2 is not None:
                l2 = l2.next

        return node_dummy.next

    