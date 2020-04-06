#-*- coding:utf-8 -*-
import os
import sys
import io
import turtleDef as td
#import traderecord as tr

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'euc-kr')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'euc-kr')


savePath="D:/Documents/Python/turtle/code/"
#savePath="C:/Users/animo/OneDrive/문서/python/turtle/code/"

try:
    if not(os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("Failed to create directory!!!!!")
        raise

stockName=td.stockName()
#Limit=td.accountLimit(account,td.riskLimit)
#account=td.entireaccount() #보유계정금
account=1000000
enterP=td.firstPoint() #첫진입 포인트
N=float(input("N: "))
riskPer=0.01
now=td.date(input("오늘자 입력 1 or else :"))
#기초정보
def info(stockName):
    with open(savePath+"%s.txt"% stockName, 'a', encoding="utf-8") as f:
        pramiding=float(input("피라미딩 포인트 0.5 or 1 : "))
        f.write("입력일 : "+str(now)+"\n")
        #f.write("%s회차"% i+"\n")
        f.write("진입포인트 : "+str(enterP)+"\n")
        f.write("ATR : "+str(N)+"\n")
        f.write("\n")
        Limit=td.accountLimit(account,riskPer) #한도
        f.write("손실한도 : "+str(Limit)+"\n")
        amount=(td.contractAmount(Limit,N)) #거래량
        f.write("거래량 : "+str(amount)+"\n") 
        f.write("구매금액 : "+str(td.price(enterP,amount))+"\n")
        f.write("Pramiding포인트 : "+str(td.nextPoint(enterP,N,pramiding))+"\n") #추가포인트
        f.write("Drop포인트 : "+str(td.stopPoint(enterP,N))+"\n") #정지포인트
        f.write("\n")
#포인트 추적
def tradePoint(stockName):
    with open(savePath+"%s.txt"% stockName, 'a', encoding="utf-8") as f:
        lastP=float(input("직전 Drop포인트 : "))
        trail=td.trailPoint(lastP,N)
        f.write("Trail포인트 : "+str(trail)+"\n") #트레일포인트        
        f.write("\n")

#turtle(stockName)
call = input("1 = all, 2 = trail ")
if call == "1":
    info(stockName)
if call == "2":
    tradePoint(stockName)

""" call = input("1 = turtle, 2 = record : ")

if call == "1":
    turtle(stockName)
if call == "2":
    record(stockName)
 """