### 참고
# 문제 힌트가 있고, 정답이 있다.
# 자료구조르 활용하면 쉽다.

from collections import deque

# 톱니바퀴 4개 정보 0 : N극, 1 : S극

def rotateGear(num, direction):
    # clock
    if direction == 1 : 
        tmp = gear[num].pop()
        gear[num].appendleft(tmp)
    # clock-wise : direction == -1 : 
    else :
        tmp = gear[num].popleft()
        gear[num].append(tmp)

def Solution(num, direction):
    visited[num] = True
    leftGear = num-1
    rightGear = num+1

    if leftGear > 0 and visited[leftGear] != True :
        if gear[leftGear][2] != gear[num][6] :
            Solution(leftGear, direction*-1)
            
    if rightGear < len(gear) and visited[rightGear] != True :
        if gear[rightGear][6] != gear[num][2] :
            Solution(rightGear, direction*-1)

    rotateGear(num,direction) # 현재 톱니바퀴 회전
    

def init():
    visited[:] = [False]*len(gear) # 방문 표시  


# 1. 문제 입력 부분 
# 시계방향 : 1, 반시계방향 : -1
gear = [deque(map(int,input())) for _ in range(4)]
gear.insert(0,[])
operateCnt = int(input()) # operate = deque(list(map(int,input().split())) for _ in range(int(input()))) # int(input())만큼 
operate = deque(list(map(int,input().split())) for _ in range(operateCnt)) 

# for dfs
visited = [False]*len(gear)

# 2. 시뮬레이션
for i in operate:
    init()
    Solution(i[0], i[1])
 
# 3. 카운트
res = 0
for i in range(1,5):
    if gear[i][0] == 1 :
        res += (1 << (i-1))

print(res)
