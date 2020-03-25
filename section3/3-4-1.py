import sys
import io
import requests
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'euc-kr')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'euc-kr')

#login정보
loginInfo = {
    'type': 'naver',
    ',code': '4g7wFE691LxANTVNTU'
}

#Session 생성, with 구문안에서 유지
with requests.Session() as s:
    login_req = s.post("ttps://user.ruliweb.com/member/social_login_proc?type=naver&code=4g7wFE691LxANTVNTU&state=EYIT8Zk6CE", data=loginInfo)
    #HTML 소스 확인
    print('login_req',login_req.text)
    #print('headers',login_req.headers)
    '''
    if login_req.status_code == 200 and login_req.ok:
        post_one = s.get('http://www.coolenjoy.net/bbs/mart2/880894')
        post_one.raise_for_status()
        soup = BeautifulSoup(post_one.text, 'html.parser')
        #print(soup.prettify())
        article = soup.select('#bo_v_con')
        print(article)
        #bo_v_con
'''