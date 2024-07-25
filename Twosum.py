class Solution(object):
  def twoSum(self, nums, target):
    # Step 1: Iterate over the numbers in the array.
    for i in range(len(nums)):
        # Step 2: For each number, iterate over the rest of the numbers in the array.
        for j in range(i+1, len(nums)):
            # Step 3: Check if the current two numbers add up to the target.
            if nums[i] + nums[j] == target:
                return [i, j]
    # Step 4: If no such pair is found, return an empty list.
    return []
        