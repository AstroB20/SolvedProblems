class Solution(object):
    def maximumTotalDamage(self, power):
        """
        :type power: List[int]
        :rtype: int
        """
        if not power:
            return 0

        freq = {}
        for val in power:
            if val in freq:
                freq[val] += 1
            else:
                freq[val] = 1

        values = sorted(freq.keys())
        n = len(values)

        total = [v * freq[v] for v in values]
        dp = [0] * n

        for i in range(n):
            curr = total[i]

            j = i - 1
            while j >= 0 and values[i] - values[j] <= 2:
                j -= 1

            if j >= 0:
                curr += dp[j]

            dp[i] = max(dp[i - 1] if i > 0 else 0, curr)

        return dp[-1]