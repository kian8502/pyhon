import sys
import io
from datetime import datetime


#price=float(input("Price: "))
#종목명지정
def stockName():
    stockName=input("종목명: ")
    return stockName
#계정시작금액
def entireaccount():
    #account=int(input("시작금액: "))
    account=int(input("계정보유금 : "))
    return account
#손실한도
def accountLimit(account,riskPer):
    accountLimit=account*riskPer
    print("손실한정 금:", accountLimit)
    return accountLimit
#첫진입포인트
def firstPoint():
    enterPoint=int(input('첫진입포인트: '))
    return enterPoint
#다음거래포인트
def nextPoint(enterPoint,N):
    newEnterPoint=enterPoint+N
    print("다음거래포인트:",newEnterPoint)
    return newEnterPoint 
#거래량
def contractAmount(Limit,N):
    contract=Limit//N
    print("거래량:",contract)
    return contract
#거래정지포인트
def stopPoint(enterPoint,N):
    stopPoint=enterPoint-N
    print("거래정지포인트:",stopPoint)
    return stopPoint 
#계정변동
def changeAccount(account,N,i):
    account=account+(N*i)    
    print("계정금액:",account)
    return account 

def date(today):
    if today=='1':
        date=datetime.now()
        print("입력일 : ",date)
        return date
    else:
        date=input("날짜 입력 : ")
        return date
        
def price(enterPoint,amount):
    price=enterPoint*amount
    print("구매가격 : ",price)
    return price
