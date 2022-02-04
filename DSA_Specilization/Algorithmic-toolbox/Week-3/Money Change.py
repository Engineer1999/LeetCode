def findChange(nums):
    total_coin = 0
    tens = int(nums/10)
    fives = int((nums-tens*10)/5)
    ones = nums - tens*10-fives*5
    
    return tens+fives+ones
    

if __name__ == '__main__':
    input_n = int(input())
    ans = findChange(input_n)
    print(ans)