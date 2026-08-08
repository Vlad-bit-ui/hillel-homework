n = int(input())
sign = -1 if n < 0 else 1
n = abs(n)
result = 0
while n > 0:
    result = result * 10 + n % 10
    n //= 10
print(sign * result)