class Solution:
  def minAbbreviation(self, target: str, dictionary: list[str]) -> str:
    m = len(target)

    def getMask(word: str) -> int:
      mask = 0
      for i, c in enumerate(word):
        if c != target[i]:
          mask |= 1 << m - 1 - i
      return mask

    masks = [getMask(word) for word in dictionary if len(word) == m]
    if not masks:
      return str(m)

    abbrs = []

    def getAbbr(cand: int) -> str:
      abbr = []
      replacedCount = 0
      for i, c in enumerate(target):
        if cand >> m - 1 - i & 1:
          if replacedCount:
            abbr += str(replacedCount)
          abbr.append(c)
          replacedCount = 0
        else:
          replacedCount += 1
      if replacedCount:
        abbr.append(str(replacedCount))
      return ''.join(abbr)

    for cand in range(2**m):
      if all(cand & mask for mask in masks):
        abbr = getAbbr(cand)
        abbrs.append(abbr)

    def getAbbrLen(abbr: str) -> int:
      abbrLen = 0
      i = 0
      j = 0
      while i < len(abbr):
        if abbr[j].isalpha():
          j += 1
        else:
          while j < len(abbr) and abbr[j].isdigit():
            j += 1
        abbrLen += 1
        i = j
      return abbrLen

    return min(abbrs, key=lambda x: getAbbrLen(x))