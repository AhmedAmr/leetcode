class Solution:
    def reverseBits(self, n: int) -> int:
        s = 32
        binary_val = (bin(n)[2:]).rjust(s, '0')
        return int(''.join(list(reversed(binary_val))), base=2)
        