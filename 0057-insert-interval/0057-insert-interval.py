class Solution:
      def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []
        insert = False

        intervals.sort()

        for i in range(len(intervals)):
            # Case 1: current interval is completely before newInterval
            if intervals[i][1] < newInterval[0]:
                res.append(intervals[i])

            # Case 2: current interval is completely after newInterval
            elif intervals[i][0] > newInterval[1]:
                if insert == False:
                    res.append(newInterval)
                    insert = True
                res.append(intervals[i])

            # Case 3: overlapping interval → MERGE (overlap reduce here)
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])

        # if newInterval was never inserted
        if insert == False:
            res.append(newInterval)

        return res
     

        


        
        