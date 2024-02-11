# Question 2: Fibonacci Sequence
# Write a program to generate the Fibonacci sequence up to 100.
def fibonacci(limit):
    fib_seq = [0, 1]
    while fib_seq[-1] + fib_seq[-2] <= limit:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq
fibonacci_seq = fibonacci(100)
print("Fibonacci sequence up to 100:")
print(fibonacci_seq)
