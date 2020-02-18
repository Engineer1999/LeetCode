class Solution(object):
    def reverse(self, x):
        if x>=2**31-1 or x<=-2**31:
            return 0
        else:
            intToStr = str(x)
            if x>=0:
                ans = intToStr[::-1]
            else:
                ans = "-" + intToStr[:0:-1]
                
            if int(ans)>=2**31-1 or int(ans)<=-2**31:
                return 0
            else:
                return int(ans)
            
            
soln = Solution()
ans = soln.reverse(12345)
print(ans)
