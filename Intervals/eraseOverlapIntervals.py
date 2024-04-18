# Time- O(nlogn)
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prevEnd = intervals[0][1]
        output = 0

        for start, end in intervals[1:]:
            if start < prevEnd:
                output += 1
                prevEnd = min(prevEnd, end)
            elif start >= prevEnd:
                prevEnd = end

        return output
