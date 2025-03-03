class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def getNext(number):
            return sum(int(digit) ** 2 for digit in str(number))
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = getNext(n)
        return n == 1