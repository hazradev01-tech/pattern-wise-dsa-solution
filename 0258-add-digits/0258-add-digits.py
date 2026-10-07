class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            current_sum = 0
            while num > 0:
                current_sum += num % 10  # ADDING LAST ELEMENT
                num //= 10  # REMOVING LAST DIGIT
            num = current_sum
        return num