class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        if "+" not in expression[1:] and "-" not in expression[1:]:
            return expression
        fractionList = []
        start = 0
        for i in range(1, len(expression)):
            if expression[i] == "+" or expression[i] == "-":
                u, d = expression[start:i].split("/")
                fractionList.append((int(u),int(d)))
                start = i
        u, d = expression[start:].split("/")
        fractionList.append((int(u),int(d)))
        ansd = 1
        for v in fractionList:
            ansd = self.lcm(ansd, v[1])
        ansu = 0
        for v in fractionList:
            ansu += v[0] * ansd / v[1]
        uzero = ansu == 0
        if not uzero:
            ansgcd = self.gcd(abs(ansu), ansd)
            return str(ansu/ansgcd) + "/" + str(ansd/ansgcd)
        else:
            return "0/1"
        
    def gcd(self, a, b):
        if a < b:
            a, b = b, a
        r = a % b
        while r != 0:
            a, b, r = b, r, b % r
        return b
    
    def lcm(self, a, b):
        return a * b / self.gcd(a, b)
