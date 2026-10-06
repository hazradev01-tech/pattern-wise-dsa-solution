class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        low=0
        high=n-1
        minimum=float("inf")

        while low<=high:
            mid=(low+high)//2
            #if left has sorted
            if nums[low]<=nums[mid]:
                minimum=min(minimum,nums[low]) #update minimum
                low=mid+1                      #search in the right half
            else:                              #right half is sorted
                minimum=min(minimum,nums[mid]) #update minimum
                high=mid-1                     #search in the left half
        return minimum                         #return the smallest one
        