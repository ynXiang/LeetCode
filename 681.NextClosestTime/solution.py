class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        nums = list(set([time[0],time[1],time[3],time[4]]))
        nums.sort(reverse=True)
        minTime, maxTime = '00:00', '23:59'
        times = []
        for n1 in nums:
            for n2 in nums:
                for n3 in nums:
                    for n4 in nums:
                        if n1+n2 < '24' and n3+n4 < '60':
                            curTime = n1+n2+':'+n3+n4
                            if curTime == time and times:
                                return times[-1]
                            else:
                                times.append(curTime)
        return times[-1]
