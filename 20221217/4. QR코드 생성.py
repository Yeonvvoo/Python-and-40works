# QR CODE 생성

import qrcode

# 주소 뿐만 아니라 문자 or 숫자로도 가능
qr_data = 'www.naver.com'
qr_img = qrcode.make(qr_data)

save_path =f"./{qr_data}.png"
qr_img.save(save_path)

# 여러개의 qr코드 한 번에 생성하는 코드 만들고 실행
""" [참고] https://pypi.org/project/qrcode/ """
file_path = "./qr코드모음.txt"
with open(file_path, 'rt', encoding="UTF8") as f:
    read_lines = f.readlines()
    for line in read_lines:
        line = line.strip()
        print(line)

        qr_data2 = line
        qr_img2 = qrcode.make(qr_data2)
        save_path2 = f'./{qr_data2}.png'
        qr_img2.save(save_path2)

# rt: 읽기용, 텍스트모드
# line.strip() : 줄 마지막 줄바꿈 문자 삭제
