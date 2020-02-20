class Solution(object):
    def twoSum(self, nums, target):
        cnt = 0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    cnt = 1
                    return [i,j]
        if cnt == 0:
            return [0,0]

sol = Solution()                
sol.twoSum([2,7,11,15], 13)
