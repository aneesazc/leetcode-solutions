# Corrected definition of Interval for context
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Sort intervals by start time
        intervals.sort(key=lambda interval: interval.start)
        
        # Loop through intervals to check for overlaps
        for i in range(1, len(intervals)):
            # If the start time of the current interval is earlier than the end time of the previous one, there's an overlap
            if intervals[i].start < intervals[i - 1].end:
                return False
        
        # If no overlap is found, return True
        return True



class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Check if the list is empty
        if not intervals:
            return True  # If there are no meetings, there's no conflict

        # Sort intervals based on start time
        intervals.sort(key=lambda x: x.start)
        
        # Initialize the current interval
        cur = intervals[0]
        
        # Check for overlapping intervals
        for i in range(1, len(intervals)):
            if intervals[i].start < cur.end:
                # If there's an overlap, return False
                return False
            else:
                # Otherwise, update the current interval
                cur = intervals[i]
        
        # If no overlap is found, return True
        return True



class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)

        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]

            if i1.end > i2.start:
                return False
        return True


