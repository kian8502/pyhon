import os
import sys
import io
from datetime import datetime
import turtleDef as td

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

savePath="D:/Documents/Python/turtle/code/"
#investType={1:"Buy",2:"Sell"}

def typeRecord():
    buyingType=input("Trading Type 시장가=1, 지정가=2, 역지정가=3 : ")
    if buyingType == "1":
        trType="시장가"
        return trType
    if buyingType == "2":
        trType="지정가"
        return trType
    if buyingType == "3":
        trType="역지정가"
        return trType

def selling(stockInfo):
    sellNum=stockInfo[0]+1
    trType=typeRecord()
    sellAmount=int(input("Trading Amount : "))
    amount=stockInfo[2]-sellAmount #잔여 수량
    price=int(input("Trading Price : "))
    agreePrice=int(input("Contract Price : "))
    slippage=int(input("Slippage : "))
    priceRange=stockInfo[4]-agreePrice #매수가 - 매도가
    profitandLoss=priceRange*amount #priceRage * 매도수량
    trTax=int(input("Trading Tax : "))
    pnlwithTax=profitandLoss-trTax
    atr=int(input("ATR : "))
    unit=float(input("Unit : "))
    trTax=int(input("Trading Tax : "))
    reason=input("Reason : ")
    note=input("Note : ")

def agreedate(today):
    if today=='1':
        date=datetime.now()
        print("입력일 : ",date.strftime('%H:%M'))
        today=date.strftime('%Y-%m-%d')
        return today
    else:
        return today


def view(stockName):
    with open(savePath+"%s.txt"% stockName, "r", encoding="utf-8") as f:
        stockInfo=[]
        lines=f.readlines()
        for line in lines:
            stockInfo.append(line.strip().split('\t'))               
    print(stockInfo)
    search=input("search code : ") # code 분류로 검색 하여 저장
    i = 0
    with open(savePath+"%s.txt"% search, "w", encoding="utf-8") as f:            
        for line in stockInfo:
            print(line[i])
            i = i + 1
            #if line[1] == search:
                #f.write(str(line)+"\n")

       
def buyRecord(stockCode):
    stockInfo=[]
    stockInfo.append(td.date(input("오늘자 입력 1 or else : ")))
    stockInfo.append(stockCode)
    stockInfo.append(input("Stock Name : "))
    stockInfo.append(typeRecord())
    stockInfo.append(int(input("Trading Amount : ")))
    stockInfo.append(int(input("Trading Price : ")))
    stockInfo.append(agreedate(input("오늘자 입력 1 or else : ")))
    stockInfo.append(int(input("Contract Price : ")))
    stockInfo.append(stockInfo[4]*stockInfo[7])
    stockInfo.append(int(input("Slippage : ")))
    stockInfo.append(int(input("ATR : ")))
    stockInfo.append(float(input("Unit : ")))
    stockInfo.append(input("Reason : "))
    stockInfo.append(input("Note : "))
    
    with open(savePath+"buy.txt", "a", encoding="utf-8") as f:        
        f.write(str(stockInfo))
        f.write("\n")
        print(stockInfo)
            

    # buyorsell = input("1 = buy, 2 = sell")

    # if buyorsell == "1":
    #     buyInfo=buying()
    # if buyorsell == "2":
    #     sellInfo=selling(buyInfo)
#buyRecord(input("Stock Code : "))
view("buy")
