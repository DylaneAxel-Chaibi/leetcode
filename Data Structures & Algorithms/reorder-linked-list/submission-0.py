# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []
        curr = head
        while curr :
            stack.append(curr)
            curr = curr.next
        for i in range(len(stack)) :
            if i % 2 == 0 :
                stack[i//2].next = stack[-1 - i//2]
            else :
                stack[-1 - i//2].next = stack[i//2 + 1]
        stack[len(stack)//2].next = None