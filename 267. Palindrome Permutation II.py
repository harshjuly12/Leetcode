class Solution:
  def generatePalindromes(self, s: str) -> list[str]:
    count = collections.Counter(s)

    odd = sum(value & 1 for value in count.values())

    if odd > 1:
      return []

    ans = []
    candidates = []
    mid = ''

    for key, value in count.items():
      if value % 2 == 1:
        mid += key
      for _ in range(value // 2):
        candidates.append(key)

    def dfs(used: list[bool], path: list[str]) -> None:
      """Generates all the unique palindromes from the candidates."""
      if len(path) == len(candidates):
        ans.append(''.join(path) + mid + ''.join(reversed(path)))
        return

      for i, candidate in enumerate(candidates):
        if used[i]:
          continue
        if i > 0 and candidate == candidates[i - 1] and not used[i - 1]:
          continue
        used[i] = True
        path.append(candidate)
        dfs(used, path)
        path.pop()
        used[i] = False

    dfs([False] * len(candidates), [])
    return ans