import sys
from queue import deque
input = lambda:sys.stdin.readline().strip()

N = int(input())

field = [[] for _ in range(N)]
shark_eaten = 0
shark_size = 2

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

for i in range(N):
    field[i] = list(map(int,input().split()))
    for j in range(N):
        if field[i][j] == 9:
            shark_x = i
            shark_y = j

print(shark_x, shark_y)

queue = deque()
queue.append([shark_x, shark_y])

while queue.maxlen != 0:
    
    for i in range(4):
        print("test")