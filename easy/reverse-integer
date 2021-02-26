# https://leetcode.com/problems/reverse-integer/
# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

class Solution:
    def reverse(self, x: int) -> int:
        MIN_INT = -1*(2**31)
        MAX_INT = (2**31) -1
        s = str(x)
        is_negative = (s[0] == '-')
        if is_negative:
            s=s[1:]
        res = int(''.join(list(reversed(s)))) * (-1 if is_negative else 1)
        if MIN_INT<=res<=MAX_INT:
            return res
        return 0