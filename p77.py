class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def backtrack(start,path):
            if len(path) == k:
                result.append(path[:])
                return
            for i in range(start,n + 1):
                path.append(i)
                backtrack(1 + i, path)
                path.pop()
        result = []
        backtrack(1,[])
        return result