class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtrack(start, path, target):
            if target == 0:
                res.append(path[:])
                return
            if target < 0:
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, target - candidates[i])
                path.pop()
        res = []
        candidates.sort()
        backtrack(0, [], target)
        return res