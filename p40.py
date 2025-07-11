class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtrack(start, path, target):
            if target == 0:
                result.append(path)
                return
            if target < 0:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                backtrack(i + 1, path + [candidates[i]], target - candidates[i])
        candidates.sort()
        result = []
        backtrack(0, [], target)
        return result
sol = Solution()
print(sol.combinationSum2([10,1,2,7,6,1,5], 8))
print(sol.combinationSum2([2,5,2,1,2], 5))  