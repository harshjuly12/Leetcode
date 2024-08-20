from dataclasses import dataclass


@dataclass(frozen=True)
class T:
  mn: int  
  mx: int 
  size: int  


class Solution:
  def largestBSTSubtree(self, root: TreeNode | None) -> int:
    def dfs(root: TreeNode | None) -> T:
      if not root:
        return T(math.inf, -math.inf, 0)

      l = dfs(root.left)
      r = dfs(root.right)

      if l.mx < root.val < r.mn:
        return T(min(l.mn, root.val), max(r.mx, root.val), 1 + l.size + r.size)

      return T(-math.inf, math.inf, max(l.size, r.size))

    return dfs(root).size