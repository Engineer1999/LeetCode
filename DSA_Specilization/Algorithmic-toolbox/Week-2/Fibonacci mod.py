def last_digit_of_the_sum_of_squares_of_fibonacci_numbers(n):
       

    if n <= 1: #Check if the input value is too small
        return n

    n = n%60 #If not, take the mod60 of the input


    pre = 0 #First value of the Fibonacci series
    curr = 1 #Second value of the Fibonacci series
    for i in range(2, n+2): #Iterate until n+2, since we are looking for F_N + F_{N+1}
        pre, curr = curr, (pre+curr) #Calculate the current Fibonacci value

    return (pre*curr)#return the mod10
        
    


if __name__ == '__main__':
    input_numbers = [int(x) for x in input().split()]
    ans = last_digit_of_the_sum_of_squares_of_fibonacci_numbers(input_numbers[0])%input_numbers[1]
    print(ans)