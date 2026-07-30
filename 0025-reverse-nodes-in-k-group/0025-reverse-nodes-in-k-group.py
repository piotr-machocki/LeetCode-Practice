# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if k == 1:
            return head

        dummy = ListNode()
        L = dummy
        start = ListNode(next=head)
        prev = None
        last = None
        P = None
        next_start = ListNode()

        def revGroup(iter):

            nonlocal L, start, prev, last, P, next_start

            if iter == 1:
                L.next = P
                L = prev

                if next_start.next:
                    start = ListNode(next=next_start.next)   
                    revGroup(k)
                return

            st = start.next

            for _ in range(iter-1):

                if st and st.next:
                    prev = st
                    last = prev.next
                else:
                    L.next = start.next
                    return

                st = st.next
            
            ln = last.next

            prev.next = None
            last.next = prev

            if iter == k:

                P = last

                if ln:
                    next_start.next = ln
                else:
                    L.next = last
                    next_start.next = None
            
            revGroup(iter-1)

        revGroup(k)

        return dummy.next