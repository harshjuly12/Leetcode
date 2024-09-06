class Solution:
  def findLonelyPixel(self, picture: list[list[str]]) -> int:
    m = len(picture)
    n = len(picture[0])
    ans = 0
    rows = [0] * m  
    cols = [0] * n  

    for i in range(m):
      for j in range(n):
        if picture[i][j] == 'B':
          rows[i] += 1
          cols[j] += 1

    for i in range(m):
      if rows[i] == 1:  
        for j in range(n):
          if picture[i][j] == 'B':
            if cols[j] == 1:
              ans += 1
            break

    return ans