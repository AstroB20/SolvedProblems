class Solution(object):
    def minTime(self, skill, mana):
        """
        :type skill: List[int]
        :type mana: List[int]
        :rtype: int
        """
        n, m = len(skill), len(mana)
        
       
        dp = [[0]*m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                time = skill[i] * mana[j]
                
                if i == 0 and j == 0:
                    dp[i][j] = time
                elif i == 0:
                    dp[i][j] = dp[i][j-1] + time
                elif j == 0:
                    dp[i][j] = dp[i-1][j] + time
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + time
        
        return dp[-1][-1]