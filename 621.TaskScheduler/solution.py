class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        import collections
        taskCounts = collections.Counter(tasks)
        maximum = 0
        maxCnt = 0
        totalCnt = 0
        for ocur in taskCounts.values():
            totalCnt += ocur
            if ocur > maximum:
                maximum = ocur
                maxCnt = 1
            elif ocur == maximum:
                maxCnt += 1
        numOfDiffTasks = len(taskCounts)
        return len(tasks) if (totalCnt - maxCnt) >= (maximum - 1) * (n + 1) else max(0, (maximum - 1) * (n + 1) + maxCnt)
