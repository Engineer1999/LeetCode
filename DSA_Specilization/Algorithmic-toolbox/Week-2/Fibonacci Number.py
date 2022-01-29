def FibNum(nums):
    ans = []
    ans.append(int(0))
    ans.append(int(1))
    for i in range(nums):
        ans.append(int(ans[i] + ans[i+1]))
    
    return ans[len(ans)-2]
        
    


if __name__ == '__main__':
    input_n = int(input())
    ans = FibNum(input_n)
    print(ans)