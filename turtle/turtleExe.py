#-*- coding:utf-8 -*-
import os
import sys
import io
import turtleDef as td

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'euc-kr')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'euc-kr')

#savePath="D:/Data/Investment/turtle/"
savePath="D:/Documents/Python/turtle/code/"

try:
    if not(os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("Failed to create directory!!!!!")
        raise


stockName=td.stockName()
#Limit=td.accountLimit(account,td.riskLimit)


i=1
#반복횟수
j=int(input("반복횟수: "))
while i <= j:
    account=td.entireaccount()
    print("%s회차"% i)
    enterP=td.firstPoint()
    N=float(input("N: "))

    with open(savePath+"%s.txt"% stockName, 'a') as f:
        now=td.date(input("오늘자 입력 1 or else :"))
        riskPer=float(input("리스크 비율 : "))
        f.write("입력일 : "+str(now)+"\n")
        f.write("%s회차"% i+"\n")
        f.write("진입포인트 : "+str(enterP)+"\n")
        f.write("ATR : "+str(N)+"\n")
        nextP=td.nextPoint(enterP,N,riskPer)
        f.write("정지포인트 : "+str(td.stopPoint(enterP,N,riskPer))+"\n") #정지포인트
        f.write("다음포인트 : "+str(nextP)+"\n")
        Limit=td.accountLimit(account,td.riskLimit) #한도
        #f.write("거래한도 : "+str(Limit)+"\n") 
        f.write("거래량 : "+str(td.contractAmount(Limit,N))+"\n") #거래량
        #f.write("계정금액 : "+str(td.changeAccount(account,N,i))+"\n") #계정금액
        f.write("\n")
    i+=1