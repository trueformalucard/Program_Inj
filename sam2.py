def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

with open("fib.txt", "w", encoding="utf-8") as файл:
    for число in fib(200):
        файл.write(str(число) + "\n")

print("200:", list(fib(200))[-1])