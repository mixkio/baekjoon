T = int(input())

def dfs(cur, length):
    global cnt
    global arr
    global n
    if(cur == length):
        sum = 0
        for i in range(cur):
            sum += arr[i]
        if(sum == n):
            cnt += 1
        return
    for i in range(1, 4):
        arr[cur] = i
        dfs(cur + 1, length)




for i in range(T):
    cnt = 0
    n = int(input())
    arr = [0 for _ in range(n)]
    for j in range(1, n + 1):
        dfs(0, j)
    print(cnt)
