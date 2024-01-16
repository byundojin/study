import sys
N = int(sys.stdin.readline())
arr = [0] * 3000000
black = list(map(int, sys.stdin.readline().split()))
gray = list(map(int, sys.stdin.readline().split()))
white = list(map(int, sys.stdin.readline().split()))

for i in range(N):
    arr[black[i]] += 1
    arr[black[i] + gray[i]] += 3
    arr[black[i] + gray[i] + white[i]] += -5

arr[0] += N

c = 0
while arr[c]:
    c += 1
    if c > 3000000:
        break
    arr[c] += arr[c - 1]

print(arr[:10])
M = int(sys.stdin.readline())

shot = list(map(int, sys.stdin.readline().split()))
adrshot = sorted([[shot[i], i] for i in range(M)])
for i in range(M):
    shot[adrshot[i][1]] += adrshot[i][1] if adrshot[i][1] < i else i

for i in shot:
    sys.stdout.write(f"{arr[i - 1]}\n")