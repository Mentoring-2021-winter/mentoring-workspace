# -*- coding: utf-8 -*-
"""codingtest1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PlK0cnSwjLwms1ZIw99ANJiqj1zzTc0m
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n=len(s)
        cols=0
        while n>0:
            n=n-numRows
            cols=cols+1
            if numRows>=3:
                for i in range(0,numRows-2):
                    if n>=1: 
                        n=n-1
                        cols=cols+1
            else:
                continue
        array=[[0 for col in range(cols)] for row in range(numRows)]
        R=0
        C=0
        K=0
        
        for i in range(len(s)):
            if numRows==1:
                array[R][C]=s[i]
                C=C+1
                continue
            if R==numRows-1:
                K=1
            elif R==0:
                K=0
            if K==0:
                array[R][C]=s[i]
                R=R+1    
            elif K==1:
                array[R][C]=s[i]
                R=R-1
                C=C+1
        result=""
        for i in array:
            for j in i:
                if j!=0:
                    result+=j
        return result











