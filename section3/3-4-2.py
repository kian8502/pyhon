import sys
import io
import requests
from bs4 import BeautifulSoup
import urllib.parse as rep
import urllib.request as req
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#login????
loginInfo = {
    'name': 's170501',
    'password': 'evil9578',
    'autologin': '1',
    'enter': rep.quote_plus('로그인')
}

#Session ????, with ????????? ????
with requests.Session() as s:
    login_req = s.post("http://192.168.10.250/index.php", data=loginInfo)
    #HTML ??? ???
    #print('login_req',login_req.text)
    #print('headers',login_req.headers)
    
    if login_req.status_code == 200 and login_req.ok:
        post_one = s.get('http://192.168.10.250/screens.php?elementid=38')
        post_one.raise_for_status()
        soup = BeautifulSoup(post_one.text, 'html.parser')
        #print(soup.prettify())
        graph = soup.select('div.flickerfreescreen > a')
        #graph_397_25
        print(graph)
        for i,z in enumerate(graph,1):
            #chart = z['src']
            #fullFileName = os.path.join('D:/img/',str(i)+'.jpg')
            #req.urlretrieve('http://192.168.10.250/'+chart,fullFileName)
            print(z)
            
