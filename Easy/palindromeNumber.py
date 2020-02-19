class Solution(object):
    def isPalindrome(self, x):
        rev = 0
        holdX = x
        while(x>0):
            rev = rev*10 + (x%10)
            x=int(x/10)
        return holdX==rev


soln = Solution()
ans = soln.isPalindrome(-121)
print(ans)
