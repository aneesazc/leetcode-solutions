# Time, Space- O(n), O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        # left ptr starts at dummy because we need the reference of the
        # value previous to the one we want to delete
        left = dummy 
        right = head

        # update right pointer n steps
        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next

        return dummy.next
