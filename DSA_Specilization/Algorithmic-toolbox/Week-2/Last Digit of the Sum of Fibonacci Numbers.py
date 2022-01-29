def fib(n, computed = {0: 0, 1: 1}):
     if n not in computed:
         computed[n] = fib(n-1, computed) + fib(n-2, computed)
     return computed[n]
 
if __name__ == '__main__':
    input_numbers = int(input())
    ans = fib(input_numbers)
    print(sum(ans))
 