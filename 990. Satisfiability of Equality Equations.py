class UnionFind:
  def __init__(self, n: int):
    self.id = list(range(n))

  def union(self, u: int, v: int) -> None:
    self.id[self.find(u)] = self.find(v)

  def find(self, u: int) -> int:
    if self.id[u] != u:
      self.id[u] = self.find(self.id[u])
    return self.id[u]


class Solution:
  def equationsPossible(self, equations: list[str]) -> bool:
    uf = UnionFind(26)

    for x, op, _, y in equations:
      if op == '=':
        uf.union(string.ascii_lowercase.index(x), # type: ignore
                 string.ascii_lowercase.index(y)) # type: ignore

    return all(
        uf.find(string.ascii_lowercase.index(x)) != # type: ignore
        uf.find(string.ascii_lowercase.index(y)) # type: ignore
        for x, op, _, y in equations
        if op == '!')