class Solution(object):
    def isPalindrome(self, x):
        xStr = str(x)
        xStrRev = xStr[::-1]

        if xStr == xStrRev:
            return 'true'
        else:
            return 'false'


soln = Solution()
ans = soln.isPalindrome(-121)
print(ans)
