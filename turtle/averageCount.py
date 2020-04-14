#-*- coding: utf-8 -*-
import os
import sys
import io
import turtleDef as td

savePath="D:/Documents/Python/turtle/code/"
#savePath="C:/Users/animo/OneDrive/문서/python/turtle/code/"

try:
    if not(os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("Failed to create directory!!!!!")
        raise

def position(stockName):
    with open(savePath + "%s.txt" % stockName, 'a', encoding="utf-8") as f:
        highest = int(input("고점 : "))
        lowest = int(input("저점 : "))
        distance = highest - lowest
        mid = lowest+(distance*0.5)
        higher = (distance*0.62)+lowest
        lower = (distance*0.38)+lowest
        #enterP=td.firstPoint()
        #print("진입 : ",enterP)
        print("고점 : ",highest)
        print("저점 : ",lowest)
        print("거리 : ",distance)
        print("중심 : ",mid)
        print("38% : ",higher)
        print("62% : ",lower)
        f.write("고점 : "+ str(highest)+"\n")
        f.write("저점 : "+ str(lowest)+"\n")
        f.write("거리 : "+ str(distance)+"\n")
        f.write("중심 : "+ str(mid)+"\n")
        f.write("38% : "+ str(higher)+"\n")
        f.write("62% : "+ str(lower)+"\n")

        # if enterP>mid:
        #     print("높음", enterP-mid)
        # if enterP<mid:
        #     print("낮음", mid-enterP)
        # if enterP==mid:
        #     print("중심")

#position(int(input("진입 : ")))
position(input("종목 : "))