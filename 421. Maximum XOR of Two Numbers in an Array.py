class Solution:
  def findMaximumXOR(self, nums: list[int]) -> int:
    maxNum = max(nums)
    if maxNum == 0:
      return 0
    maxBit = int(math.log2(maxNum))
    ans = 0
    prefixMask = 0 
    prefixMask |= 1 << i
    prefixes = set([num & prefixMask for num in nums])
    candidate = ans | 1 << i
    for prefix in prefixes:
        if prefix ^ candidate in prefixes:
          ans = candidate
          break

    return ans