class Solution(object):
    def kthCharacter(self, k):
        """
        :type k: int
        :rtype: str
        """
        word = "a"
        while len(word)<k:
            for alpha in word:
                word+=chr(ord(alpha)+1)
            print(word)
        return word[k-1] if k <= len(word) else "a"
# Example usage:
sol = Solution()
print(sol.kthCharacter(5))  # Output: 'e'
# print(sol.kthCharacter(10)) # Output: 'j'
# print(sol.kthCharacter(15)) # Output: 'o'