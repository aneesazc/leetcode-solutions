# O(2^n) -> O(n)
# Top Down
class Solution:
    def climbStairs(self, n: int) -> int:

        def helper(i, cache):
            if i > n:
                return 0
            if i == n:
                return 1
            if i in cache:
                return cache[i]

            cache[i] = helper(i + 1, cache) + helper(i + 2, cache)
            return cache[i]

        return helper(0, {})

# Bottom up
class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n - 1):
            tmp = one
            one = one + two
            two = tmp

        return one



class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        arr = [1, 1]
        i = n - 2

        while i >= 0:
            tmp = arr[0]
            arr[0] = arr[0] + arr[1]
            arr[1] = tmp
            i -= 1

        return arr[0]
      
