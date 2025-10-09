class Solution(object):
    def minTime(self, skill, mana):
        """
        :type skill: List[int]
        :type mana: List[int]
        :rtype: int
        """
        n, m = len(skill), len(mana)
        prev = [0] * m
        curr = [0] * m

        # Wizard 0 (base case)
        prev[0] = skill[0] * mana[0]
        for j in range(1, m):
            prev[j] = prev[j-1] + skill[0] * mana[j]

        # Remaining wizards
        for i in range(1, n):
            curr[0] = prev[0] + skill[i] * mana[0]
            for j in range(1, m):
                curr[j] = max(prev[j], curr[j-1]) + skill[i] * mana[j]
            prev, curr = curr, prev  # swap

        return prev[m-1]
            