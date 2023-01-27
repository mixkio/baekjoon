import sys
input = lambda:sys.stdin.readline().strip()

N, r, c = map(int, input().split())
cnt = 0

def find(N, r, c):
    global cnt
    if N == 0:
        # print(cnt)
        return cnt
    if r < 2**(N-1) and c < 2**(N-1):
        # print(0)
        find(N-1, r, c)
    elif r < 2**(N-1) and c >= 2**(N-1):
        # print((2**(N-1)*2**(N-1)))
        cnt+=(2**(N-1)*2**(N-1))
        find(N-1, r, c-(2**(N-1)))
    elif r >= 2**(N-1) and c < 2**(N-1):
        # print((2**(N-1)*2**(N-1))*2)
        cnt+=(2**(N-1)*2**(N-1))*2
        find(N-1, r-(2**(N-1)), c)
    else:
        # print((2**(N-1)*2**(N-1))*3)
        cnt+=(2**(N-1)*2**(N-1))*3
        find(N-1, r-(2**(N-1)), c-(2**(N-1)))


find(N, r, c)
print(cnt)