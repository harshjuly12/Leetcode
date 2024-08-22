class Solution:
  def isReflected(self, points: list[list[int]]) -> bool:
    minX = math.inf
    maxX = -math.inf
    seen = set()

    for x, y in points:
      minX = min(minX, x)
      maxX = max(maxX, x)
      seen.add((x, y))

    summ = minX + maxX

    return all((summ - x, y) in seen for x, y in points)