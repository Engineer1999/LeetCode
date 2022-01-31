def FibNum(n):
    if n <= 1:
        return n
    
    limit = int(n%60)
    sum_ans = -1
    previous = 0
    current  = 1

    for _ in range(n+1):
        previous, current = current, (previous + current)%10
    
    if current!=0:
        sum_ans = current-1
    else:
        sum_ans = 9
    
    return sum_ans
 
if __name__ == '__main__':
    input_numbers = int(input())
    ans = FibNum(input_numbers)
    print(ans)
 