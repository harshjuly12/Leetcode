class Solution:
  @functools.lru_cache(None)
  def canWin(self, currentState: str) -> bool:
    return any(True
               for i, (a, b) in enumerate(zip(currentState, currentState[1:]))
               if a == '+' and b == '+' and
               not self.canWin(currentState[:i] + '-' + currentState[i + 2:]))