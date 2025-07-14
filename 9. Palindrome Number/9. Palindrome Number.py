class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reverse = 0
        dup = x
        while x > 0:
            lastDigit = x % 10
            reverse = reverse * 10 + lastDigit
            x = x // 10
        
        if reverse == dup:
            return True
        return False