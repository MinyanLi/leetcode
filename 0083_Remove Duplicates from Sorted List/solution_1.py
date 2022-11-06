# Runtime 76 ms Beats 67.51%
# Memory 14 MB Beats 29.99%

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        # by changing the pointer in cur will also change the pointer in head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            cur = cur.next   # move forward to next element
        return head  # because cur had been moving forward, at the end of the while loop, cur will be None, so should not return cur
