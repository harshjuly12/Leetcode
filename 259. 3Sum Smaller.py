class Solution:
  def threeSumSmaller(self, nums: list[int], target: int) -> int:
    if len(nums) < 3:
      return 0

    ans = 0

    nums.sort()

    for i in range(len(nums) - 2):
      l = i + 1
      r = len(nums) - 1
      while l < r:
        if nums[i] + nums[l] + nums[r] < target:
          ans += r - l
          l += 1
        else:
          r -= 1

    return ans