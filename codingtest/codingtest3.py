# -*- coding: utf-8 -*-
"""codingtest3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kfAt_06Qebq-80G_m1bRm-inYIzggF_o
"""

from collections import deque

from collections import deque
s1=input()
s2=input()
s3=input()
s4=input()

int(input)

s1=list(s1)
s2=list(s2)
s3=list(s3)
s4=list(s4)
s1 = list(map(int, s1))
s2 = list(map(int, s2))
s3 = list(map(int, s3))
s4 = list(map(int, s4))

queue1=deque(s1)
queue2=deque(s2)
queue3=deque(s3)
queue4=deque(s4)
print(queue1)



def confirm(queue1,queue2,queue3,queue4):##다르면 1, 같으면 0
  conlist=[0,0,0]
  if queue1[2]!=queue2[6]:
    conlist[0]=1
  if queue2[2]!=queue3[6]:
    conlist[1]=1
  if queue3[2]!=queue4[6]:
    conlist[2]=1
  return conlist

conlist=confirm(queue1,queue2,queue3,queue4)
conlist

######회전
def rotation(x,queue):
  if x ==-1:##반시계
    a=queue.popleft()
    queue.append(a)
  if x==1:##시계
    a=queue.pop()
    queue.appendleft(a)
  return queue

print(queue1)
queue1=rotation(-1,queue1)
print(queue1)



###1번2번3번4번톱니 회전 ??다중리턴
def gear1(dir,queue1,queue2,queue3,queue4):
  conlist=confirm(queue1,queue2,queue3,queue4)
  if conlist[0]==0:##1번 2번바퀴 같을때
    queue1=rotation(dir,queue1)
    return queue1,queue2,queue3,queue4
  if conlist[0]==1:
    queue1=rotation(dir,queue1)
    queue2=rotation(-dir,queue2)
    if conlist[1]==0:
      return queue1,queue2,queue3,queue4
    else:
      queue3=rotation(dir,queue3)
      if conlist[2]==0:
        return queue1,queue2,queue3,queue4
      else:
        queue4=rotation(-dir,queue4)
        return queue1,queue2,queue3,queue4

def gear2(dir,queue1,queue2,queue3,queue4):
  conlist=confirm(queue1,queue2,queue3,queue4)
  if conlist[0]==0:##1번 2번바퀴 같을때
    queue2=rotation(dir,queue2)
  else:
    queue2=rotation(dir,queue2)
    queue1=rotation(-dir,queue1)
  if conlist[1]==0:
    return queue1,queue2,queue3,queue4
  else:
    queue3=rotation(-dir,queue3)
    if conlist[2]==0:
      return queue1,queue2,queue3,queue4
    else: 
      queue4=rotation(dir,queue4)
      return queue1,queue2,queue3,queue4

def gear3(dir,queue1,queue2,queue3,queue4):
  conlist=confirm(queue1,queue2,queue3,queue4)
  if conlist[2]==0:#3번과 4번
    queue3=rotation(dir,queue3)
  else:
    queue3=rotation(dir,queue3)
    queue4=rotation(-dir,queue4)
  if conlist[1]==0:
    return queue1,queue2,queue3,queue4
  else:
    queue2=rotation(-dir,queue2)
    if conlist[0]==0:
      return queue1,queue2,queue3,queue4
    else:
      queue1=rotation(dir,queue1)
      return queue1,queue2,queue3,queue4

def gear4(dir,queue1,queue2,queue3,queue4):
  conlist=confirm(queue1,queue2,queue3,queue4)
  if conlist[2]==0: ## 3번 4번같다면
    queue4=rotation(dir,queue4)
    return queue1,queue2,queue3,queue4
  else:
    queue4=rotation(dir,queue4)
    queue3=rotation(-dir,queue3)
    if conlist[1]==0:
      return queue1,queue2,queue3,queue4
    else:
      queue2=rotation(dir,queue2)
      if conlist[0]==0:
        return queue1,queue2,queue3,queue4
      else:
        queue1=rotation(-dir,queue1)
        return queue1,queue2,queue3,queue4

repeat=int(input())
for i in range(repeat):
  num,dir=map(int,input().split())
  if num==1:
    queue1,queue2,queue3,queue4=gear1(dir,queue1,queue2,queue3,queue4)
  elif num==2:
    queue1,queue2,queue3,queue4=gear2(dir,queue1,queue2,queue3,queue4)
  elif num==3:
    queue1,queue2,queue3,queue4=gear3(dir,queue1,queue2,queue3,queue4)
  elif num==4:
    queue1,queue2,queue3,queue4=gear4(dir,queue1,queue2,queue3,queue4)

result=0
if queue1[0]==1:
  result=result+1
if queue2[0]==1:
  result=result+2
if queue3[0]==1:
  result=result+4
if queue4[0]==1:
  result=result+8

queue1

result=0
if queue1[0]==1:
  result=result+1
if queue2[0]==1:
  result=result+2
if queue3[0]==1:
  result=result+4
if queue4[0]==1:
  result=result+8
print(result)

queue1[0]

from collections import deque

def confirm(queue1,queue2,queue3,queue4):##다르면 1, 같으면 0
  conlist=[0,0,0]
  if queue1[2]!=queue2[6]:
    conlist[0]=1
  if queue2[2]!=queue3[6]:
    conlist[1]=1
  if queue3[2]!=queue4[6]:
    conlist[2]=1
  return conlist

######회전
def rotation(x,queue):
  if x ==-1:##반시계
    a=queue.popleft()
    queue.append(a)
  if x==1:##시계
    a=queue.pop()
    queue.appendleft(a)
  return queue

###1번2번3번4번톱니 회전 ??다중리턴
def gear1(dir,queue1,queue2,queue3,queue4):
  conlist=confirm(queue1,queue2,queue3,queue4)
  if conlist[0]==0:##1번 2번바퀴 같을때
    queue1=rotation(dir,queue1)
    return queue1,queue2,queue3,queue4
  if conlist[0]==1:
    queue1=rotation(dir,queue1)
    queue2=rotation(-dir,queue2)
    if conlist[1]==0:
      return queue1,queue2,queue3,queue4
    else:
      queue3=rotation(dir,queue3)
      if conlist[2]==0:
        return queue1,queue2,queue3,queue4
      else:
        queue4=rotation(-dir,queue4)
        return queue1,queue2,queue3,queue4

def gear2(dir,queue1,queue2,queue3,queue4):
  conlist=confirm(queue1,queue2,queue3,queue4)
  if conlist[0]==0:##1번 2번바퀴 같을때
    queue2=rotation(dir,queue2)
  else:
    queue2=rotation(dir,queue2)
    queue1=rotation(-dir,queue1)
  if conlist[1]==0:
    return queue1,queue2,queue3,queue4
  else:
    queue3=rotation(-dir,queue3)
    if conlist[2]==0:
      return queue1,queue2,queue3,queue4
    else: 
      queue4=rotation(dir,queue4)
      return queue1,queue2,queue3,queue4

def gear3(dir,queue1,queue2,queue3,queue4):
  conlist=confirm(queue1,queue2,queue3,queue4)
  if conlist[2]==0:#3번과 4번
    queue3=rotation(dir,queue3)
  else:
    queue3=rotation(dir,queue3)
    queue4=rotation(-dir,queue4)
  if conlist[1]==0:
    return queue1,queue2,queue3,queue4
  else:
    queue2=rotation(-dir,queue2)
    if conlist[0]==0:
      return queue1,queue2,queue3,queue4
    else:
      queue1=rotation(dir,queue1)
      return queue1,queue2,queue3,queue4

s1=input()
s2=input()
s3=input()
s4=input()
s1=list(s1)
s2=list(s2)
s3=list(s3)
s4=list(s4)
s1 = list(map(int, s1))
s2 = list(map(int, s2))
s3 = list(map(int, s3))
s4 = list(map(int, s4))
queue1=deque(s1)
queue2=deque(s2)
queue3=deque(s3)
queue4=deque(s4)
repeat=int(input())
for i in range(repeat):
  num,dir=map(int,input().split())
  if num==1:
    queue1,queue2,queue3,queue4=gear1(dir,queue1,queue2,queue3,queue4)
  elif num==2:
    queue1,queue2,queue3,queue4=gear2(dir,queue1,queue2,queue3,queue4)
  elif num==3:
    queue1,queue2,queue3,queue4=gear3(dir,queue1,queue2,queue3,queue4)
  elif num==4:
    queue1,queue2,queue3,queue4=gear4(dir,queue1,queue2,queue3,queue4)

result=0
if queue1[0]==1:
  result=result+1
if queue2[0]==1:
  result=result+2
if queue3[0]==1:
  result=result+4
if queue4[0]==1:
  result=result+8
print(result)
