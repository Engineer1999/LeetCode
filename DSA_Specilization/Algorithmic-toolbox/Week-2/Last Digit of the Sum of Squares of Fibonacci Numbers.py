def FibNum(n):
    if n <= 1:
        return n
    sum_ans = 1
    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum_ans += current*current

    return sum_ans%10
 
if __name__ == '__main__':
    input_numbers = int(input())
    ans = FibNum(input_numbers)
    print(ans)
 