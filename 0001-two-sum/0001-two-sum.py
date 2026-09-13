class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map={}
        for i in range(0,len(nums)):
            remain=target-nums[i]
            if remain in hash_map:
                return[hash_map[remain],i]
            hash_map[nums[i]]=i