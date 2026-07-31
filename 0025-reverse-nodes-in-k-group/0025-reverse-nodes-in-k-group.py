# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if k == 1 or not head:
            return head
        
        dummy = ListNode()
        L = dummy
        L_holder = None
        prev = None
        last = None
        start = ListNode(next=head)
        check = start.next
        first = True

        while check:

            for _ in range(k-1):
                if check.next:
                    check = check.next
                else:
                    L.next = start.next
                    return dummy.next
            
            check = check.next 
            
            prev = start.next
            last = prev.next
            L_holder = prev

            for i in range(k-1):

                another = last.next 

                if first:
                    prev.next = None
                    last.next = prev
                    first = False
                else:
                    last.next = prev
                
                prev = last
                P = prev
                last = another
                               
            L.next = P
            L = L_holder
            start.next = check
        
        L.next = None
        return dummy.next   



  