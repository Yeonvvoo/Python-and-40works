import googletrans

### 간단한 번역
# translator = googletrans.Translator()
#
# str1 = "데이식스 노래 좋아"
# result1 = translator.translate(str1, dest='en', src='auto')
# print(f'{str1} => {result1.text}')
#
# str2 = "Beautiful Feeling"
# result2 = translator.translate(str2, dest='ko', src='en')
# print(f'{str2} => {result2.text}')

### 사용 가능한 언어 출력
# lang = googletrans.LANGUAGES
# print(lang)

### 파일 번역 프로그램
from os import linesep
import googletrans

translator = googletrans.Translator()

read_file_path = r"영어파일.txt"
write_file_path = r'한글파일.txt'

with open(read_file_path, 'r') as f:
    readLines = f.readlines()

for lines in readLines:
    result1 = translator.translate(lines, dest='ko')
    print(result1.text)
    with open(write_file_path, 'a', encoding='UTF8') as f:
        f.write(result1.text + '\n')