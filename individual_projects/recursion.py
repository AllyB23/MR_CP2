for num in range(1,11):
    if num % 2 == 0:
        print(num)

even = []

num = 5
sum = 1

for x in range(5):
    sum *= x
print(f"Loop: {sum}")

def factorial(n):
    if n == 1: return 1
    return n * factorial(n-1)

print(f"recursion: {factorial(num)}")

fib = [1, 1]

for i in range(1,11):
    #fib.append([i-1] + fib[i])

    print(f"Loop: {fib}")

numbers = []
def fibonacci(n):
    #numbers.append(n)
    if n == 1:
        return 1
    else:
        return n + fibonacci(n-1) + fibonacci(n-2)


fibonacci(10)
print(f"Recursion: {fibonacci(10)}")