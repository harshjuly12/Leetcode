class Solution:
  def reorderedPowerOf2(self, n: int) -> bool:
    count = collections.Counter(str(n)) # type: ignore
    return any(Counter(str(1 << i)) == count for i in range(30)) # type: ignore