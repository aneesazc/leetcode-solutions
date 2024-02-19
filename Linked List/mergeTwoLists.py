class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a dummy node to simplify edge cases and maintain the head of the merged list.
        dummy = ListNode()  
        # This 'current' pointer is used to build the new list.
        current = dummy  

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next  # Move current to the next node.

        # Attach the remaining elements of list1 or list2.
        current.next = list1 or list2

        # Return the merged list, starting from the next element of the dummy since dummy is an empty node.
        return dummy.next
