class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if str1 + str2 != str2 + str1:
            return ""
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        return str1[:gcd(len(str1), len(str2))]
# Example usage:
sol = Solution()
print(sol.gcdOfStrings("ABCABC", "ABC"))  # Output: "ABC"
print(sol.gcdOfStrings("ABABAB", "ABAB"))  # Output: "AB"
print(sol.gcdOfStrings("LEET", "CODE"))    # Output: "" (no common divisor)
