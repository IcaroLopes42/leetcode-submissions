class Solution:
    def fib(self, n: int) -> int:
        cache = {}
        res = 0
        def dfs(n):
            if n in cache:
                return cache[n]
            if n == 1 or n == 0:
                return n
            res = dfs(n-1) + dfs(n-2)
            cache[n] = res
            return res

        return dfs(n)