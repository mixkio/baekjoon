import sys
input = lambda : sys.stdin.readline().strip()
N, M = map(int, input().split())
listarr = []
dictarr = {}
for i in range(N):
     temp = input()
     listarr.append(temp)
     dictarr[temp] = i+1
for i in range(M):
    keyword = input()
    if keyword.isdigit():
        print(listarr[int(keyword)-1])
    else:
        print(dictarr[keyword])