class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob1 and rob2 represent the maximum amounts robbed
        # up to two steps back and one step back, respectively.
        # Initially, no house has been robbed, so both are 0.
        rob1 = 0
        rob2 = 0
        # [rob1, rob2, n, n+1, ...]
        # Loop through each number in the list of house values.
        for n in nums:
            # For each house 'n', you have two choices:
            # 1. Rob the current house plus the amount from rob1 (i.e., the house two steps back),
            #    because adjacent houses cannot be robbed.
            # 2. Skip the current house and take the amount from rob2 (i.e., the previous house's maximum),
            #    which already considers the best decision up to that point.
            # The max of these two choices will be the new rob2 value,
            # representing the maximum amount that can be robbed up to the current house.
            curr = max(n + rob1, rob2)

            # Prepare for the next iteration:
            # rob1 is updated to rob2's value from the previous iteration,
            # and rob2 is updated to the current maximum amount.
            rob1 = rob2
            rob2 = curr

        # After going through all houses, rob2 contains the maximum amount
        # that can be robbed without triggering the alarm.
        return rob2
