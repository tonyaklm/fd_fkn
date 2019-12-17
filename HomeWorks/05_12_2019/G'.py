x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
flag = abs(x1 - x2) == 1 and (y1 - y2) == -1
print("YES" if flag else "NO")