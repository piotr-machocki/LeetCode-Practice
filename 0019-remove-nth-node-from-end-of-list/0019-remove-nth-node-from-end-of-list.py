# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # Create a dummy node to handle L = n case
        dummy = ListNode(0, head)

        # First pass: Walk through the list to count the total length L. 

        L = 0
        curr = head

        while curr:
            L += 1
            curr = curr.next

        # Second pass: Walk to index L - n to remove the node.
        
        curr = dummy

        for i in range(L - n):
            curr = curr.next


        # Deleting the node L - n: Node L - n - 1 needs to point to L - n + 1 

        curr.next = curr.next.next

        # Return head of the list

        return dummy.next

