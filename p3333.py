class Solution(object):
    def possibleStringCount(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        runs = []
        n = len(word)
        i = 0
        while i < n:
            j = i
            while j < n and word[j] == word[i]:
                j += 1
            runs.append((word[i], j - i))
            i = j
        
        num_runs = len(runs)
        max_length = len(word)
        
        dp = [ [0] * (max_length + 1) for _ in range(num_runs + 1) ]
        dp[0][0] = 1
        
        for i in range(1, num_runs + 1):
            char, run_length = runs[i-1]
            for l in range(max_length + 1):
                for t in range(1, run_length + 1):
                    if l - t >= 0:
                        dp[i][l] = (dp[i][l] + dp[i-1][l - t]) % MOD
        result = 0
        for l in range(k, max_length + 1):
            result = (result + dp[num_runs][l]) % MOD
        
        return result
        