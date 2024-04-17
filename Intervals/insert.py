class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                # If the end of newInterval is less than the start of the current interval,
                # then newInterval does not overlap with any subsequent intervals.
                # We can add newInterval to the result and return it along with all remaining intervals.
                res.append(newInterval)
                return res + intervals[i:]

            elif newInterval[0] > intervals[i][1]:
                # If the start of newInterval is greater than the end of the current interval,
                # then newInterval cannot overlap with the current interval.
                # Add the current interval to the result.
                res.append(intervals[i])

            else:
                # If newInterval overlaps with the current interval, merge them into newInterval.
                # This does not add the interval to 'res' yet, it updates newInterval
                # to be the merged interval.
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        # After checking all intervals, add the final version of newInterval to the result.
        # This handles the case where newInterval extends past all existing intervals
        # or is non-overlapping and should be added at the end.
        res.append(newInterval)
        return res
