import sys
import io
from datetime import datetime

#stopPoint={'base':2,'Fstop':0.5,'Sstop':2}

#price=float(input("Price: "))
riskLimit=0.02
#종목명지정
def stockName():
    stockName=input("종목명: ")
    return stockName
#계정시작금액
def entireaccount():
    #account=int(input("시작금액: "))
    account=300000
    return account
#계정한도
def accountLimit(account,riskLimit):
    accountLimit=account*riskLimit
    print("계정한도 금:", accountLimit)
    return accountLimit
#첫진입포인트
def firstPoint():
    enterPoint=float(input('첫진입포인트: '))
    return enterPoint
#다음거래포인트
def nextPoint(enterPoint,N):
    newEnterPoint=enterPoint+(2*N)
    print("다음거래포인트:",newEnterPoint)
    return newEnterPoint 
#거래량
def contractAmount(Limit,N):
    contract=Limit//(N*2)
    print("거래량:",contract)
    return contract
#거래정지포인트
def stopPoint(enterPoint,N):
    stopPoint=enterPoint-(2*N)
    print("거래정지포인트:",stopPoint)
    return stopPoint 
#계정변동
def changeAccount(account,N,i):
    account=account+(N*i)    
    print("계정금액:",account)
    return account 

def date(Y):
    if Y=='1':
        date=datetime.now()
        print("입력일 : ",date)
        return date
    else:
        date=input("날짜 입력 : ")
        return date
        
