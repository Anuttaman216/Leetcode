class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        count = 0

        for i in range(len(points)-1):
            cur = points[i][:]
            tar = points[i+1]

            while cur != tar:

                if cur[0] < tar[0]:
                    cur[0] += 1
                elif cur[0] > tar[0]:
                    cur[0] -= 1

                if cur[1] < tar[1]:
                    cur[1] += 1
                elif cur[1] > tar[1]:
                    cur[1] -= 1

                count += 1

        return count