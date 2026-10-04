class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                # Minimum must be in the right unsorted portion
                left = mid + 1
            elif nums[mid] < nums[right]:
                # Minimum is at mid or in the left portion
                right = mid
            else:
                # nums[mid] == nums[right]: duplicates present, safely shrink right boundary
                right -= 1

        return nums[left]
        