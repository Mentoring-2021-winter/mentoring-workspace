#gear1 = list(map(int,input().split()))
#gear2 = list(map(int,input().split()))
#gear3 = list(map(int,input().split()))
#gear4 = list(map(int,input().split()))
#=>위처럼 쓰면 recursion을 못해줄 것 같아 다른거 찾아서 씀

def Shift(gearNumber,direction):
    global gear;
    if(direction==1):   #시계 방향 -> right shift
        temp = gear[gearNumber-1][7]
        for i in range(len(gear[gearNumber-1])-1,0,-1):
            gear[gearNumber-1][i]=gear[gearNumber-1][i-1]
        gear[gearNumber-1][0]=temp  #마지막에 있던게 제일 먼저오게됨

    if(direction==-1):  #반시계 방향 -> left shift
        temp = gear[gearNumber-1][0]
        for i in range(0, len(gear[gearNumber - 1])-1):
            gear[gearNumber - 1][i] = gear[gearNumber - 1][i + 1]
        gear[gearNumber - 1][7] = temp  # 제일 처음에 있던게 마지막에 가게됨


def TurnGear(gearNumber,direction,option=None):
    global gear;

    if gearNumber==0 or gearNumber==5 : #recursion 탈출문
        return;
    else:
        if option==None:    #처음 지정한 톱니바퀴번호에 대해 한차례 방향으로 회전진행
            Shift(gearNumber,direction)    
        if option=='right': #
            if gearNumber >= 1 and gearNumber <= 3: #오른쪽바퀴가 존재해서 움직일 수 있는지 조사해야함
                if (gear[gearNumber - 1][2]!=gear[gearNumber][6]):  #오른쪽바퀴와 S,N극이 다르다면
                    Shift(gearNumber+1, -(direction))   #오른쪽바퀴 회전시킴
                    TurnGear(gearNumber+1,-(direction),option)  #오른쪽바퀴에 대해 다시 recursion으로 조사하게함
        if option=='left':
            if gearNumber>=2 and gearNumber<=4:     #왼쪽바퀴가 존재해서 움직일 수 있는지 조사해야함
                if(gear[gearNumber-1][6]!=gear[gearNumber-2][2]):   #왼쪽바퀴와 S,N극이 다르다면
                    Shift(gearNumber-1,-(direction))
                    TurnGear(gearNumber-1,-(direction),option)  #왼쪽바퀴에 대해 다시 recursion으로 조사하게 함

gear = [list(map(int, input())) for _ in range(4)]  #톱니바퀴 배열생성 [[********] [********] [********] [********] ]
rotate = int(input())                            #몇번 시행할지

for i in range(0, rotate):
    gearNumber, direction = map(int, input().split())
    TurnGear(gearNumber,direction)          #처음에대해서는 회전을 한차례 진행하겠다 option=>None
    TurnGear(gearNumber,direction,'left')   #진행한 회전 이후 left쪽으로 recursion하겠다
    TurnGear(gearNumber,direction,'right')  #진행한 회전 이후 right쪽으로 recursion하겠다


score = 0
for i in range(0,4):
    if(gear[i][0]==1):
        if i==0:
            score+=1
        elif i==1:
            score+=2
        elif i==2:
            score+=4
        elif i==3:
            score+=8

print(score)