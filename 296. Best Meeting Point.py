class Solution:
  def minTotalDistance(self, grid: list[list[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    I = [i for i in range(m) for j in range(n) if grid[i][j]]
    J = [j for j in range(n) for i in range(m) if grid[i][j]]

    def minTotalDistance(grid: list[int]) -> int:
      summ = 0
      i = 0
      j = len(grid) - 1
      while i < j:
        summ += grid[j] - grid[i]
        i += 1
        j -= 1
      return summ

    return minTotalDistance(I) + minTotalDistance(J)