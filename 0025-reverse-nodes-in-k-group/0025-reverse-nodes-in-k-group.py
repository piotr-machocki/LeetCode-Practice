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

        def revK():
            nonlocal L, L_holder, prev, start, check, first

            for _ in range(k-1):
                if check.next:
                    check = check.next
                else:
                    L.next = start.next
                    return

            check = check.next

            st = start.next
            prev = st
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
            
            first = True

            if not check:
                L.next = P 
                return
            else:
                L.next = P
                L = L_holder
                start.next = another
                revK()
                return
        
        revK()
        return dummy.next    