class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []

        for i in range(len(intervals)):
            start, end = intervals[i]

            # Case 1: current interval is completely before newInterval
            if end < newInterval[0]:
                res.append([start, end])

            # Case 2: newInterval is completely before current interval
            elif newInterval[1] < start:
                res.append(newInterval)

                # Everything after this is already sorted
                res.extend(intervals[i:])
                return res

            # Case 3: they overlap -> merge
            else:
                newInterval[0] = min(newInterval[0], start)
                newInterval[1] = max(newInterval[1], end)

        # If newInterval never got added, add it at the end
        res.append(newInterval)

        return res