class Solution(object):
    def topKFrequent(self, nums, k):
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
            
        
        sorted_items = sorted(freq.items(), key=lambda item: item[1], reverse=True)
        
        
        return [item[0] for item in sorted_items[:k]]

         
        