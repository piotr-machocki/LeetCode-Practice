# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        
        if head:
            if head.next:
                dummy.next = head.next
            else:
                return head
        else:
            return None
        
        prev = dummy
        
        while head:

            if head.next:
                first = head
                second = head.next
                prev.next = second
                first.next = second.next
                second.next = first

                prev = prev.next.next
                head = head.next

            else:
                return dummy.next

        return dummy.next
