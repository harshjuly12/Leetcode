class Solution:
  def kInversePairs(self, n: int, k: int) -> int:
    kMod = 1_000_000_007
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(n + 1):
      dp[i][0] = 1

    for i in range(1, n + 1):
      for j in range(1, k + 1):
        dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % kMod
        if j - i >= 0:
          dp[i][j] = (dp[i][j] - dp[i - 1][j - i] + kMod) % kMod

    return dp[n][k]