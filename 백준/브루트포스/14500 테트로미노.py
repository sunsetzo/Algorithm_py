import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

tetris=[[(0,0),(0,1),(0,2),(0,3)],
        [(0,0),(1,0),(2,0),(3,0)],
        [(0,0),(1,0),(0,1),(1,1)],
        [(0,0),(1,0),(2,0),(2,1)],
        [(0,1),(1,1),(2,1),(2,0)],
        [(0,0),(0,1),(1,1),(2,1)],
        [(0,0),(0,1),(1,0),(2,0)],
        [(0,0),(1,0),(1,1),(1,2)],
        [(0,2),(1,1),(1,2),(1,0)],
        [(0,0),(0,1),(0,2),(1,2)],
        [(0,0),(1,0),(0,1),(0,2)],
        [(0,0),(1,0),(1,1),(2,1)],
        [(0,1),(1,1),(1,0),(2,0)],
        [(1,0),(1,1),(0,1),(0,2)],
        [(0,0),(0,1),(1,1),(1,2)],
        [(0,1),(1,0),(1,1),(1,2)],
        [(0,0),(0,1),(0,2),(1,1)],
        [(0,0),(1,0),(1,1),(2,0)],
        [(0,1),(1,1),(1,0),(2,1)]]

_max = 0

for i in range(n):
    for j in range(m):
        for x in range(19):
            temp = 0
            cnt = 0
            for y in range(4):
                (di, dj) = tetris[x][y]
                ni, nj = i+di, j+dj
                if 0<=ni<n and 0<=nj<m:
                    temp += arr[ni][nj]
                    cnt += 1

                if cnt == 4:
                    if temp > _max:
                        _max = temp

print(_max)