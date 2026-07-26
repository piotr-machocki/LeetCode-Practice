# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        dummy = ListNode()
        curr = dummy

        # Filter out those sneaky empty linked lists (None's)
        
        lists = [node for node in lists if node]

        while True:

            smallest_idx = -1
            
            for i in range(len(lists)):
                if lists[i] is not None:
                    if smallest_idx == -1 or lists[i].val < lists[smallest_idx].val:
                        smallest_idx = i
                        
            if smallest_idx == -1:
                break
            else:
                curr.next = lists[smallest_idx]
                curr = curr.next
                lists[smallest_idx] = lists[smallest_idx].next
        
        return dummy.next