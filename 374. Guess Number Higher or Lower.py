
class Solution:
  def guessNumber(self, n: int) -> int:
    l = 1
    r = n

    while l < r:
      m = (l + r) // 2
      if guess(m) <= 0:  
        r = m
      else:
        l = m + 1

    return l