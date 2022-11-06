# Runtime 145 ms Beats 46.55%
# Memory 13.9 MB Beats 43.46%

# creat dummy



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        cur = dummy

        plus = 0

        while l1 or l2 or plus:
            cur.next = ListNode()
            
            if l1:
                v1 = l1.val
            else:
                v1 = 0

            if l2:
                v2 = l2.val
            else:
                v2 = 0

            val = v1 + v2 + plus

            plus = 0
            if val > 9:
                val = val - 10
                plus = 1

            cur.val = val
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            if l1 == None and l2 == None and plus == 0:
                cur.next = None
            cur = cur.next

        return dummy


