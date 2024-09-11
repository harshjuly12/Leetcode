class Solution:
  def minSteps(self, n: int) -> int:
    if n <= 1:
      return 0

    dp = [i for i in range(n + 1)]

    for i in range(2, n + 1):
      for j in range(i // 2, 2, -1):
        if i % j == 0:
          dp[i] = dp[j] + i // j  
          break

    return dp[n]