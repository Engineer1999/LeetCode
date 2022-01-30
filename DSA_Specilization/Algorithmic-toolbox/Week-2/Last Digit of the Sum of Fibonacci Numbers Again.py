def FibNum(m, n):
    if n <= 1:
        return n
    sum_ans = 0
    previous = 0
    current  = 1

    for ii in range(n - 1):
        previous, current = current, previous + current
        if ii+2>=m:
            #print(ii+2, m, current)
            sum_ans += current
        
    return sum_ans%10
 
if __name__ == '__main__':
    input_numbers = [int(x) for x in input().split()]
    ans = FibNum(input_numbers[0], input_numbers[1])
    print(ans)
 