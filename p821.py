class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        n = len(s)
        result = [0] * n
        prev = -10000.0
        for i in range(n):
            if s[i] == c:
                prev = i
            result[i] = i - prev

        prev = 10000.0
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i
            result[i] = min(result[i], prev - i)

        return result