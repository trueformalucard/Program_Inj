def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

f200 = list(fib(200))[-1]

for i, num in enumerate(fib(10), 1):
    print(f"{i:2}: {num}")

print("\n200:")
print(f200)