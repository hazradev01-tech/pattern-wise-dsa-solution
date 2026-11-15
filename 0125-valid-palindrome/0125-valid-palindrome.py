class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Keep only alphanumeric characters and make them lowercase
        p = [ch.lower() for ch in s if ch.isalnum()]
        
        # Check if the list of characters is a palindrome and return a boolean
        return p == p[::-1]
        