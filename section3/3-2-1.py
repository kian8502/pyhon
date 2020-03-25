import sys
import io
import requests

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

s = requests.Session()
#r = s.get('https://www.naver.com') #put(fetch), delete, get, post

#print('1',r.text)
#r = s.get('http://httpbin.org/cookies',cookies={'from':'hi'})
'''
url = 'http://httpbin.org/get'
headers = {'user-agent':'myPythonApp_1.0.0'}

r = s.get(url,headers=headers)
print(r.text)
'''
s.close()

with requests.Session() as s:
    r = s.get('https://www.naver.com')
    print(r.text)