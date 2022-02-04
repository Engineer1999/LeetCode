from functools import cmp_to_key
 
@cmp_to_key
def custom_compare(a, b):
    value1 = str(a) + str(b)
    value2 = str(b) + str(a)
 
    if value1 < value2:
        return 1
    elif value1 > value2:
        return -1
    else:
        return 0
 
 
def findLargestNumber(numbers):
    # sort using a custom function object
    numbers.sort(key=custom_compare)
 
    # join and return
    return ''.join(map(str, numbers))
 
 
if __name__ == '__main__':
    numbers = [4, 46, 427, 465, 42]
 
    largestNumber = findLargestNumber(numbers)
    print('The largest number is', largestNumber)
'''
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
 '''