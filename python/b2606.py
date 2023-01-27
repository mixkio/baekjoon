import sys
input = lambda : sys.stdin.readline().strip()
cnt = 0

def _union(a, b):
    fA = _find(a)
    fB = _find(b)

    par[fA] = fB


def _find(x):
    if (x == par[x]):
        return x
    else:
        par[x] = _find(par[x])
        return par[x]

N = int(input())
par = [i for i in range(N+1)]
M = int(input())

for i in range(M):
    a, b = map(int, input().split())
    _union(a, b)

for i in range(2, N+1):
    if(_find(1)==_find(i)):
        cnt+=1
print(cnt)