# -*- coding: utf-8 -*-
"""codingtest2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hqaQNYW_vDf72W0l5FuBxm-K4esvr9Po
"""

n=6
def generateMatrix( n:int):
  all=n*n
  row=0
  col=0
  repeat=n
  array=[[0 for c in range(n)] for r in range(n)]
  print(array)
  x=1 ##반복횟수
  while x<=all:
    for j in range(repeat):
      array[row][col]=x
      print(x)
      print(array)
      if j != repeat-1:
        col=col+1   ##마지막은 실행안해야되는데
      else:
        row=row+1
      x=x+1
    repeat=repeat-1
    if repeat==0:
      break
    
    for j in range(repeat):
      array[row][col]=x
      print(array)
      if j != repeat-1:
        row=row+1
      else:
        col=col-1
      x=x+1
    
    for j in range(repeat):
      array[row][col]=x
      print(array)
      if j!=repeat-1:
        col=col-1
      else:
        row=row-1
      x=x+1
    repeat=repeat-1
    if repeat==0:
      break
    for j in range(repeat):
      array[row][col]=x
      print(array)
      if j!=repeat-1:
        row=row-1
      else:
        col=col+1
      x=x+1

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        all=n*n
        row=0
        col=0
        repeat=n
        array=[[0 for c in range(n)] for r in range(n)]
        x=1
        while x<=all:
            for j in range(repeat):
                array[row][col]=x
                if j!=repeat-1:
                    col=col+1
                else:
                    row=row+1
                x=x+1
            repeat=repeat-1
            if repeat==0:
                break
            
            for j in range(repeat):
                array[row][col]=x
                print(array)
                if j!=repeat-1:
                    row=row+1
                else:
                    col=col-1
                x=x+1
            
            for j in range(repeat):
                array[row][col]=x
                if j!=repeat-1:
                    col=col-1
                else:
                    row=row-1
                x=x+1
            repeat=repeat-1
            if repeat==0:
                break
            for j in range(repeat):
                array[row][col]=x
                print(array)
                if j!=repeat-1:
                    row=row-1
                else:
                    col=col+1
                x=x+1
        return array

5*5

