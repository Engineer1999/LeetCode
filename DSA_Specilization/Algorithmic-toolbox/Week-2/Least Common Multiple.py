def GCD(numbers):
    
    if numbers[0]>numbers[1]:
        a, b = numbers[0], numbers[1]
    else:
        a, b = numbers[1], numbers[0]

    
    while a*b!=0:
        b, a = a%b, b
    if a==0:
        return b
    else:
        return a
            
        
        
if __name__ == '__main__':
    input_numbers = [int(x) for x in input().split()]
    ans = int((input_numbers[0]*input_numbers[1])/GCD(input_numbers))
    print(ans)
    
        