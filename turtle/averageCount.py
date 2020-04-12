#-*- coding: utf-8 -*-
import os
import sys
import io
import turtleDef as td

def position(enterP):
    highest = int(input("고점 : "))
    lowest = int(input("저점 : "))
    distance = highest - lowest
    mid = lowest+(distance*0.5)
    higher = (distance*0.62)+lowest
    lower = (distance*0.38)+lowest
    #enterP=td.firstPoint()
    print("진입 : ",enterP)
    print("고점 : ",highest)
    print("저점 : ",lowest)
    print("거리 : ",distance)
    print("중심 : ",mid)
    print("62% : ",higher)
    print("38% : ",lower)

    if enterP>mid:
        print("높음", enterP-mid)
    if enterP<mid:
        print("낮음", mid-enterP)
    if enterP==mid:
        print("중심")