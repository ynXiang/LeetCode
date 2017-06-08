class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ans = 0
        d = []
        for i in range(len(points)):
            d.append({})
        for i in range(len(points)-1):
            for j in range(i+1, len(points)):
                dist = self.squaredist(points[i],points[j])
                if dist not in d[i]:
                    d[i][dist] = 1
                else:
                    d[i][dist] += 1
                if dist not in d[j]:
                    d[j][dist] = 1
                else:
                    d[j][dist] += 1
        for i in d:
            for v in i.values():
                ans += v*(v-1)
        return ans
        
    def squaredist(self, a, b):
        return (a[0]-b[0])**2+(a[1]-b[1])**2
