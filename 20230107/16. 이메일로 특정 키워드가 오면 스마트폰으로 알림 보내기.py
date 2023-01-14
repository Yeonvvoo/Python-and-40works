import imaplib
import email
from email import policy
import requests
import json
import time

slack_webhook_url = "https://hooks.slack.com/services/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"

def send_slack_webhook(str_text):
    headers = {
        "Content-type": "application/jsp"
    }

    data = {
        "text": str_text
    }

    res = requests.post(slack_webhook_url, headers=headers, data=json.dumps(data))

    if res.status_code == 200:
        return "ok"
    else:
        return "error"

# 문자열 인코딩
def find_encoding_info(txt):
    info = email.header.decode_header(txt)
    subject, encode = info[0]
    return subject, encode

# 네이버 메일로 로그인
imap = imaplib.IMAP4_SSL('imap.gmail.com')
id = '구글이메일주소'
pw = '구글앱비밀번호'
imap.login(id, pw)

# 보내는 데이터 저장할 리스트 생성
send_list = []

# 받은 메일함에서 메일 read
while True:
    try:
        imap.select('INBOX')
        resp, data = imap.uid('search', None, 'All')
        all_email = data[0].split()
        # 최신 5개의 이메일만 read
        last_email = all_email[-5:]

        # 최신 메일부터 출력(reversed)
        for mail in reversed(last_email):
            result, data = imap.uid('fetch', mail, '(RFC822)')
            raw_email = data[0][1]
            email_message = email.message_from_bytes(raw_email, policy=policy.default)

            # 보낸사람, 받은시간, 제목을 문자열 형태로 바인딩
            email_from = str(email_message['From'])
            email_date = str(email_message['Date'])
            subject, encode = find_encoding_info(email_message['Subject'])
            subject_str = str(subject)
            # "보안" 찾으면 찾은 위치 반환, 그렇지 못하면 -1 반환
            if subject_str.find("보안") >= 0:
                slack_send_message = email_from + '\n' + email_date + '\n' + subject_str
                if slack_send_message not in send_list:
                    send_slack_webhook(slack_send_message)
                    print(slack_send_message)
                    send_list.append(slack_send_message)
        time.sleep(30)
    except KeyboardInterrupt:
        break


    # # 본문 내용 출력 (text만)
    # message = ''
    # if email_message.is_multipart():
    #     for part in email_message.get_payload():
    #         if part.get_content_type() == 'text/plain':
    #             bytes = part.get_payload(decode=True)
    #             encode = part.get_content_charset()
    #             message = message + str(bytes, encode)
    # print(message)
    # print('=' * 70)

imap.close()
imap.logout()
