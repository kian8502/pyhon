import sys
import io
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'euc-kr')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'euc-kr')

# 요청 URL
URL = 'https://www.wishket.com/accounts/login/'

#Fake User-Agent 생성
ua = UserAgent()
'''print(ua.ie)
print(ua.chrome)
print(ua.random)
'''
with requests.Session() as s:
    #URL 연결
    s.get(URL)
    #Login 정보 Payload
    login_Info = {
        'identification': 'kian85',
        'password': 'qh!s!77JbX@6czH',
        'csrfmiddlewaretoken': s.cookies['csrftoken']
    }
    #Header값 확인
    #print('header',s.headers)
    #print('token',s.cookies['csrftoken'])

    #요청
    response = s.post(URL, data=login_Info,headers={'User-Agent':str(ua.chrome), 'Referer':'https://www.wishket.com/accounts/login/'})
    #HTML 결과 확인
    #print('response', response.text)

    if response.status_code == 200 and response.ok:
        soup = BeautifulSoup(response.text,'html.parser')
        projectList = soup.select('table.table-responsive > tbody > tr')
        for i in projectList:
            #print(i)
            print(i.find('th').string, i.find('td').text)

