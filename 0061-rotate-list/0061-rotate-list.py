# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def sizeOfList(head) :
            curr = head
            l = 0
            while curr :
                l += 1
                curr = curr.next
            return l
        if not head :
            return None
        k %= sizeOfList(head)
        if k == 0 :
            return head
        prev = curr = P = head
        for _ in range(k-1) :
            P = P.next
        while P.next :
            P = P.next
            prev = curr
            curr = curr.next
        P.next = head
        prev.next = None
        return curr