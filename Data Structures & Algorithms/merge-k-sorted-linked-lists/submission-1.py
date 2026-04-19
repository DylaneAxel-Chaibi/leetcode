# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0 :
            return None
        if len(lists) == 1 :
            return lists[0]
        return self.merge2Lists(self.mergeKLists(lists[:len(lists)//2]), self.mergeKLists(lists[len(lists)//2:]))

    def merge2Lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        l1 = list1
        l2 = list2
        while l1 and l2 :
            if l1.val <= l2.val :
                dummy.next = l1
                dummy = dummy.next
                l1 = l1.next
            else :
                dummy.next = l2
                dummy = dummy.next
                l2 = l2.next
        if not l1 :
            dummy.next = l2
        if not l2 :
            dummy.next = l1
        if list1.val <= list2.val :
            return list1
        return list2
        