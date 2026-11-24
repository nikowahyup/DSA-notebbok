class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

class Solution:
    def ReverseList(self, head : ListNode) -> ListNode:

        sebelum = None
        sekarang = head

        while sekarang is not None:
            selanjutnya = sekarang.next
            sekarang.next = sebelum
            sebelum = sekarang
            sekarang = selanjutnya

        return sebelum