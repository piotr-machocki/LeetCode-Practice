# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:

        def carry_helper(curr):
            while curr.val == 10:
                curr.val = 0
                if not curr.next:
                    last = ListNode(val = 1)
                    curr.next = last
                    return dummy.next
                curr = curr.next
                curr.val += 1
        
        dummy = ListNode()

        if l1:
            dummy.next = l1
        else:
            dummy.next = l2
            return dummy.next

        carry = 0

        while l1:
            if l2:
                sum = l1.val + l2.val + carry 
                if sum > 9:
                    carry = 1
                    l1.val = sum - 10
                else:
                    carry = 0
                    l1.val = sum
            else:
                if carry:
                    l1.val += 1
                carry_helper(l1)
                return dummy.next
            
            if not l1.next and l2.next:
                if carry:
                    l2.next.val += 1
                l1.next = l2.next
                l2 = l2.next
                carry_helper(l2)
                return dummy.next
            
            if not l1.next and not l2.next and carry:
                last = ListNode(val = 1)
                l1.next = last
                return dummy.next
                        
            l1 = l1.next
            l2 = l2.next
        
        return dummy.next



                
                
                
