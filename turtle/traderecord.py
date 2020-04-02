import os
import sys
import io
from datetime import datetime

# sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'euc-kr')
# sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'euc-kr')

""" 
investType={1:"Buy",2:"Sell"}
trTime=input("Trading Date : ")
stockCode=input("Stock Code : ")
stockName=input("Stock Name : ")

trType={1:"시장가",2:"지정가",3:"역지정가"}
amount=int(input("Trading Amount : "))
price=int(input("Trading Price : "))
agreePrice=int(input("Contract Price : "))
slippage=int(input("Slippage : "))
atr=int(input("ATR : "))
unit=float(input("Unit : "))
trTax=int(input("Trading Tax : "))
reason=input("Reason : ")
note=input("Note : ")



def typeRecord():
    buyingType=input("Trading Type : ")
    if buyingType == "1":
        trType="시장가"
        return trType
    if buyingType == "2":
        trType="지정가"
        return trType
    if buyingType == "3":
        trType="역지정가"
        return trType

def buying(stockInfo):
    buyNum=stockInfo[0]+1
    trType=typeRecord()
    buyAmount=int(input("Trading Amount : "))
    price=int(input("Trading Price : "))
    agreePrice=int(input("Contract Price : "))
    slippage=int(input("Slippage : "))
    atr=int(input("ATR : "))
    unit=float(input("Unit : "))
    trTax=int(input("Trading Tax : "))
    reason=input("Reason : ")
    note=input("Note : ")

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
 """
savePath="D:/Documents/Python/turtle/code/"
def record(stockName):
    stockInfo=[]
    with open(savePath+"%s.txt"% stockName, "r", encoding="utf-8") as f:
        lines=f.readlines()
        for stockInfo in lines:
            print(stockInfo)
        

    # buyorsell = input("1 = buy, 2 = sell")

    # if buyorsell == "1":
    #     buyInfo=buying()
    # if buyorsell == "2":
    #     sellInfo=selling(buyInfo)


record("test")

#winandloss=0

# if profitandLoss>0:
#     profitCost=profitandLoss

# else :
#     lossCost=profitandLoss