class Solution:
  def alienOrder(self, words: list[str]) -> str:
    graph = {}
    inDegrees = [0] * 26

    self._buildGraph(graph, words, inDegrees)
    return self._topology(graph, inDegrees)

  def _buildGraph(
      self,
      graph: dict[str, set[str]],
      words: list[str],
      inDegrees: list[int],
  ) -> None:
    for word in words:
      for c in word:
        if c not in graph:
          graph[c] = set()

    for first, second in zip(words, words[1:]):
      length = min(len(first), len(second))
      for j in range(length):
        u = first[j]
        v = second[j]
        if u != v:
          if v not in graph[u]:
            graph[u].add(v)
            inDegrees[ord(v) - ord('a')] += 1
          break  
        if j == length - 1 and len(first) > len(second):
          graph.clear()
          return

  def _topology(self, graph: dict[str, set[str]], inDegrees: list[int]) -> str:
    s = ''
    q = collections.deque()

    for c in graph:
      if inDegrees[ord(c) - ord('a')] == 0:
        q.append(c)

    while q:
      u = q.pop()
      s += u
      for v in graph[u]:
        inDegrees[ord(v) - ord('a')] -= 1
        if inDegrees[ord(v) - ord('a')] == 0:
          q.append(v)

    return s if len(s) == len(graph) else ''