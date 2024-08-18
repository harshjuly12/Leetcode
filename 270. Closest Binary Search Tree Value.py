class Solution:
  def closestValue(self, root: TreeNode | None, target: float) -> int:
    if target < root.val and root.left:
      left = self.closestValue(root.left, target)
      if abs(left - target) <= abs(root.val - target):
        return left

    if target > root.val and root.right:
      right = self.closestValue(root.right, target)
      if abs(right - target) < abs(root.val - target):
        return right

    return root.val