class Solution:
  def toHex(self, num: int) -> str:
    if num == 0:
      return '0'

    hex = '0123456789abcdef'
    ans = []
    if num < 0:
      num += 2**32

    while num > 0:
      ans.append(hex[num & 0xF])
      num >>= 4

    return ''.join(reversed(ans))