n = int(input())
k = int(input())
while True:
    if n == k:
        break
    elif n % 2 == 1 or n // 2 < k:
        n -= 1
        print("-1")
    else:
        n //= 2
        print(":2")