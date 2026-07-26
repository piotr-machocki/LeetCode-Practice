# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        dummy = ListNode()
        curr = dummy

        import heapq
        
        pq = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(pq, (lists[i].val, i, lists[i]))

        while pq:
            x = heapq.heappop(pq)

            if x[2].next:
                heapq.heappush(pq, (x[2].next.val ,x[1], x[2].next))

            curr.next = x[2]
            curr = curr.next

        return dummy.next






