//Python 
n = int(input())
t = int(input())
l=[int(x) for x in input().split()]
findlen = 0
for i in range(0, n):
    for j in range(i, n):
        s = []
        count = 0
        s = l[i:j + 1]
        for k in range(0, len(s)):
            count = count + max(s) - s[k]
        if count <= t and len(s) > findlen:
            findlen = len(s)
print(findlen)
