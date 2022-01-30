def FibNum(n):
    if n <= 1:
        return n
    
    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current
        
    


if __name__ == '__main__':
    input_numbers = [int(x) for x in input().split()]
    ans = FibNum(input_numbers[0])%input_numbers[1]
    print(ans)