import re


### 이메일 형식 찾기
# test_string = """
# aaa@bbb.com
# 123@abc.co.kr
# test@hello.kr
# ok@ok.co.kr
# ok@ok.co.kr
# ok@ok.co.kr
# no.co.kr
# no.kr
# """
#
# results = re.findall(r'[\w\.-]+@[\w\.-]+', test_string)
# # 중복제거
# results = list(set(results))
# print(results)

#### 사이트에서 이메일 수집
import requests

url = "https://v.daum.net/v/20221224152906491"

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36',
    'Content-Type' : 'text/html; charset=utf-8'
}

response = requests.get(url, headers=headers)
results = re.findall(r'[\w\.-]+@[\w\.-]+', response.text)
results = list(set(results))
print(results)