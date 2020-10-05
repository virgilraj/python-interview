
def fibonacci_rec(n):
    if n==0:
        return 0
    if n == 1 or n == 2:
        return 1
    
    result = fibonacci_rec(n-1) + fibonacci_rec(n-2)
    return result

def fibonacci(n):
    if n==0:
        return 0
    if n == 1 or n == 2:
        return 1

    prev1 = 1
    prev2 = 1
    result = 0
    for i in range(3, n+1):
        
        result = prev1 + prev2
        prev2 = prev1
        prev1 = result
    print("fibonacci of ", n ," is ", result)

if __name__ == "__main__":
    #fibonacci(100020)
    print("fibnacii" , fibonacci_rec(100))