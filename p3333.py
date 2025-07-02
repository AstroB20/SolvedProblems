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
            runs.append(j - i)
            i = j
        
        num_runs = len(runs)
        dp = [0] * (n + 1)
        dp[0] = 1
        
        for run_len in runs:
            new_dp = [0] * (n + 1)
            for s in range(n + 1):
                if dp[s]:
                    for t in range(1, run_len + 1):
                        if s + t <= n:
                            new_dp[s + t] = (new_dp[s + t] + dp[s]) % MOD
            dp = new_dp
        return sum(dp[k:]) % MOD
