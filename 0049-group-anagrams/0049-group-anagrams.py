class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = {}
        
        for s in strs:
            key = "".join(sorted(s))
            groups.setdefault(key, []).append(s)
            
        return list(groups.values())
        