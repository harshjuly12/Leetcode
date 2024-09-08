class Solution:
  def outerTrees(self, trees: list[list[int]]) -> list[list[int]]:
    hull = []

    trees.sort(key=lambda x: (x[0], x[1]))

    def cross(p: list[int], q: list[int], r: list[int]) -> int:
      return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

    for tree in trees:
      while len(hull) > 1 and cross(hull[-1], hull[-2], tree) > 0:
        hull.pop()
      hull.append(tuple(tree))
    hull.pop()

    for tree in reversed(trees):
      while len(hull) > 1 and cross(hull[-1], hull[-2], tree) > 0:
        hull.pop()
      hull.append(tuple(tree))

    return list(set(hull))