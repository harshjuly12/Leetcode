class Solution:
  @functools.lru_cache(None)# type: ignore
  def allPossibleFBT(self, n: int) -> list[TreeNode | None]:# type: ignore
    if n % 2 == 0:
      return []
    if n == 1:
      return [TreeNode(0)]# type: ignore

    ans = []

    for leftCount in range(n):
      rightCount = n - 1 - leftCount
      for left in self.allPossibleFBT(leftCount):
        for right in self.allPossibleFBT(rightCount):
          ans.append(TreeNode(0))# type: ignore
          ans[-1].left = left
          ans[-1].right = right

    return ans