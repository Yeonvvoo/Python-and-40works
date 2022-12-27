# 텍스트를 음성으로 변환

# 문자를 음성으로 변환해주는 라이브러리
from gtts import gTTS
from playsound import playsound
import os


# 1) 파일 만들기
text = "안녕하세요. 파이썬과 40개의 작품들 입니다."

tts = gTTS(text=text, lang='ko')
tts.save("./hi.mp3")

# 2) 파일 실행하기
# 경로를 스크립트 경로로 이동
os.chdir(os.path.dirname(os.path.abspath(__file__)))
playsound("hi.mp3")

