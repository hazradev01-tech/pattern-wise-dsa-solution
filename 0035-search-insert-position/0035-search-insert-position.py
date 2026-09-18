class Solution(object):

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        right = len(nums) - 1

        while low <= right:
            mid = (low + right) // 2

            if nums[mid] == target:
                return mid  # Return the index, not the element value
            elif nums[mid] < target:
                low = mid + 1
            else:
                right = mid - 1

        return low  # If not found, low is the correct insertion index
        