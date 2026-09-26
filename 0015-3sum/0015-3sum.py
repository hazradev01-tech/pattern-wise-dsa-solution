class Solution(object):

  def threeSum(self, nums):
    """:type nums: List[int]

    :rtype: List[List[int]]
    """
    ans = []
    n = len(nums)
    nums.sort()

    for i in range(n):
      # Skip duplicate values for the first element
      if i > 0 and nums[i] == nums[i - 1]:
        continue

      # Set up the two pointers
      j = i + 1
      k = n - 1

      # Move pointers towards each other
      while j < k:
        total_sum = nums[i] + nums[j] + nums[k]

        if total_sum < 0:
          j += 1  # Need a larger sum
        elif total_sum > 0:
          k -= 1  # Need a smaller sum
        else:
          # Found a valid triplet
          ans.append([nums[i], nums[j], nums[k]])

          j += 1
          k -= 1

          # Skip duplicate values for j and k
          while j < k and nums[j] == nums[j - 1]:
            j += 1
          while j < k and nums[k] == nums[k + 1]:
            k -= 1

    return ans