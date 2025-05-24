class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = [0] * 128
        for c in s:
            count[ord(c)] += 1
        result = 0
        for c in count:
            result += c // 2 * 2
            if result % 2 == 0 and c % 2 == 1:
                result += 1
        return result