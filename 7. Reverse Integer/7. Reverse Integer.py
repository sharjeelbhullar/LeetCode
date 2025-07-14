class Solution:
    def reverse(self, x: int) -> int:
        if x > 2**31-1 or x < -2**31:
            return 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        reversed = 0
        while x > 0:
            lastDigit = x % 10
            reversed = reversed * 10 + lastDigit
            x = x//10
            if reversed > 2**31-1 or x < -2**31:
                return 0
        reversed = reversed * sign
        return reversed