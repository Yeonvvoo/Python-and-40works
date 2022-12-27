# 내/외부 IP 확인
import socket
import requests
import re

#-- 내부 IP 확인

# 소켓 연결
in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# https의 기본 접속 포트 = 443
in_addr.connect(("www.google.co.kr", 443))
# 연결된 소켓 이름 출력
print(f'내부 IP: {in_addr.getsockname()[0]}')


#-- 외부 IP 확인

# 사이트 접속
req = requests.get("http://ipconfig.kr")
# re: 정규식 표현을 사용하여 ip주소를 가져와 바인딩
""" 정규식 표현식(Regular expressions) 참고 """
""" https://nachwon.github.io/regular-expressions/ """
# re.search: 문자열 전체에서 검색하여 처음으로 매치되는 문자열을 찾는다.
# \d: 숫자[0-9]와 같다.
# {m,n} 반복 횟수 지정 : {m, n} 앞에 있는 문자가 m번에서 n번까지 반복될 때 매치된다.
out_addr = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]
print(f'외부 IP: {out_addr}')






