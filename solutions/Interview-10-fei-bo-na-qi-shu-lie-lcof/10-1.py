class Solution:
    def fib(self, n: int) -> int:
        dp_0, dp_1 = 0, 1
        for _ in range(n):
            dp_0, dp_1 = dp_1, dp_0 + dp_1
        return dp_0 % 1000000007
        
        # # 超时
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return 1
        # return (self.fib(n - 1) + self.fib(n - 2)) % 1000000007