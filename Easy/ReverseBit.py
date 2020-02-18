class Solution:
    def reverseBits(self, n):
        ans = int("{:032b}".format(n)[::-1], 2)
        return ans
    

soln = Solution()
_input = 1234567891011
ans = soln.reverseBits(_input)
print(bin(_input))
print(bin(ans))