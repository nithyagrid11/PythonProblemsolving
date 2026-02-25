# cook your dish here
n, x = map(int, input().split())
arr = list(map(int, input().split()))
found = False
for i in arr:
    if x == i:
        found = True
        break
if found:
    print("YES")
else:
    print("NO")
