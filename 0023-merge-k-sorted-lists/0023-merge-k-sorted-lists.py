# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        

        def mergeTwoLists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

            dummy = ListNode()
            tail = dummy
            
            while l1 and l2:
                if l1.val < l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next
                
            # Attach whichever list still has remaining nodes
            tail.next = l1 if l1 else l2

            return dummy.next

        if lists:

            while len(lists) != 1:
                
                merged_lists = []

                for i in range(0,len(lists), 2):
                    if i+1 < len(lists):
                        merged_lists.append(mergeTwoLists(lists[i], lists[i+1]))
                    else:
                        merged_lists.append(lists[i])
                        
                lists = merged_lists

            return lists[0]

        else:
            return None