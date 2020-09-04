class Solution:
    def longestCommonPrefix(self, strs) -> str:
        ans = ''
        temp=''
        if strs==[]:
            return ""

        for i in range(len(strs[0])):
            temp = temp + strs[0][i]
            cnt=0
            for ele in strs:
                #print(ele[0:i+1])
                #print(temp)
                #print('------------')
                if ele[0:i+1] == temp:
                    cnt+=1
            if cnt == len(strs):
                ans = ans + strs[0][i]
                
        return ans

Lists =  ["c","acc","ccc"]

sol = Solution()
print(sol.longestCommonPrefix(Lists))