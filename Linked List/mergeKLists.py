# Time, Space- O(nlogK), O(1) 
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeLists(l1, l2))
            lists = mergedLists
        return lists[0]

        
    def mergeLists(self, l1, l2):
        dummy = ListNode()
        curr = dummy

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        curr.next = l1 or l2

        return dummy.next

'''
The total no. of levels is log K (which is basically the no. of while loop iterations) 
and we do n operations at each level, so we get O(logk * n) or O(nlogK)
'''
# Since in each level of merging, you are processing O(n) nodes (across all merges at that level), 
# and there are logK levels (since you're halving the number of lists to be merged each time), the overall time complexity is O(nlogK).

# This logarithmic factor comes from the number of times you can 
# divide K by 2 until you get to 1 (which is what logK represents), 
# and n represents the total work done at each level.

        
