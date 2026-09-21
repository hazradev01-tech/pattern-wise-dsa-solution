class Solution(object):

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]

        :rtype: int
        """
        if not nums:
            return 0

        my_set = set(nums)
        longest = 0

        for num in my_set:
            # Only start counting if 'num' is the beginning of a sequence
            if num - 1 not in my_set:
                x = num
                count = 1

                while x + 1 in my_set:
                    count += 1
                    x += 1

                longest = max(longest, count)

        return longest
        