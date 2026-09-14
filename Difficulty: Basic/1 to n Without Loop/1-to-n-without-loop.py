class Solution:
    def printTillN(self, n):
        def helper(i):
            if i > n:
                return
            print(i, end=" ")
            helper(i + 1)

        helper(1)