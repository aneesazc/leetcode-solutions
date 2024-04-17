class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        res = [intervals[0]]

        for start, end in intervals[1:]:
            if res[-1][1] >= start:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append([start, end])

        return res



class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        res = [intervals[0]]

        for start, end in intervals[1:]:
            if res[-1][1] >= start:
                res[-1] = [min(res[-1][0], start), max(res[-1][1], end)]
            else:
                res.append([start, end])

        return res
