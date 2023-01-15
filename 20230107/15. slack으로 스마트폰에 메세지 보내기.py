import requests
import json

slack_webhook_url = ['slackwebhookurl']

def send_slack_webhook(str_text):
    headers = {
        "Content-type": "application/json"
    }

    data = {
        "text" : str_text
    }

    res = requests.post(slack_webhook_url, headers=headers, data=json.dumps(data))

    if res.status_code == 200:
        return "ok"
    else:
        return "error"

print(send_slack_webhook("안녕하세요 저는 파이썬 봇입니다."))
