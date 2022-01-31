def FibNum(m, n):
    m = int(m%60)
    n = int(n%60)
    
    if n<m:
        n+=60
    
    sum_ans = 0
    current = 0
    next  = 1

    for ii in range(n+1):
        if ii>=m:
            sum_ans += current
    
        next, current = next+current, next
    return int(sum_ans%10)
 
if __name__ == '__main__':
    input_numbers = [int(x) for x in input().split()]
    ans = FibNum(input_numbers[0], input_numbers[1])
    print(ans)
 