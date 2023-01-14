'''네이버 메일 보내기'''
# import smtplib
# from email.mime.text import MIMEText
#
# send_email = "네이버이메일주소"
# send_pwd = "네이버비밀번호"
#
# recv_email = "받을 이메일 주소"
#
# smtp_name = "smtp.naver.com"
# smtp_port = 587
#
# text = """
#     2023년 1월 7일 날씨 맑지만 미세먼지로 인해 흐림.
#     오늘은 엄마 아빠의 결혼 기념일이자,
#     피겨 첫 수업 날이며, 끝나고 스터디도 하는 날이다.
#     마치고 힘도 들고 배도 고파서 경대에 와서 서브웨이를 먹었다.
#     저녁까지 아름다운 하루가 되기를!
# """
#
# msg = MIMEText(text)
#
# msg["Subject"] = "여누하루"
# msg['From'] = send_email
# msg['To'] = recv_email
# print(msg.as_string())
#
# s = smtplib.SMTP(smtp_name, smtp_port)
# s.starttls()
# s.login(send_email, send_pwd)
# s.sendmail(send_email, recv_email, msg.as_string())
#
# s.quit()

'''구글 이메일 보내기'''
#
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.mime.application import MIMEApplication
#
# send_email = "구글이메일주소"
# send_pwd = "구글앱비밀번호"
#
# recv_email = "받을이메일주소"
#
# smtp_name = "smtp.gmail.com"
# smtp_port = 587
#
# text = """
#     첨부파일 메일 테스트 내용 입니다.
# """
#
# # msg = MIMEText(text)
#
# msg = MIMEMultipart()
#
# msg['Subject'] = "첨부파일 테스트 입니다."
# msg['From'] = send_email
# msg['To'] = recv_email
# # print(msg.as_string())
#
# contentPart = MIMEText(text)
# msg.attach(contentPart)
#
# etc_file_path = r'/Users/yeonu/PycharmProjects/study/20230107/첨부파일.txt'
# with open(etc_file_path, 'rb') as f:
#     etc_part = MIMEApplication(f.read())
#     etc_part.add_header('Content-Disposition', 'attachment', filename="첨부파일.txt")
#     msg.attach(etc_part)
#
# s = smtplib.SMTP(smtp_name, smtp_port)
# s.starttls()
# s.login(send_email, send_pwd)
# s.sendmail(send_email, recv_email, msg.as_string())
# s.quit()


'''html 형식메일 보내기'''
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

send_email = "네이버이메일주소"
send_pwd = "네이버비밀번호"

recv_email = "네이버이메일주소"

smtp_name = "smtp.naver.com"
smtp_port = 587

msg = MIMEMultipart()

msg['Subject'] = "html로 보내는 메일 입니다."
msg['From'] = send_email
msg['To'] = recv_email

html_body = """
<!-- #######  THIS IS A COMMENT - Visible only in the source editor #########-->
<p>안녕하세요 html 형식으로 보내는 이메일 테스트 입니다.</p>
<p><span style="color: #3366ff;">글자의 색상을 지정하거나</span></p>
<h1><strong>크기를 조정할 수 있습니다.</strong></h1>
<p>표도 만들 수 있습니다.</p>
<table style="height: 67px;" border="1" width="339" cellspacing="1">
<tbody>
<tr>
<td style="width: 105.671875px;">1</td>
<td style="width: 105.671875px;">2</td>
<td style="width: 105.671875px;">3</td>
</tr>
<tr>
<td style="width: 105.671875px;">표를</td>
<td style="width: 105.671875px;">만들 수&nbsp;</td>
<td style="width: 105.671875px;">있습니다.</td>
</tr>
<tr>
<td style="width: 105.671875px;">4</td>
<td style="width: 105.671875px;">5</td>
<td style="width: 105.671875px;">6</td>
</tr>
</tbody>
</table>
"""

msg.attach(MIMEText(html_body, 'html'))

s = smtplib.SMTP(smtp_name, smtp_port)
s.starttls()
s.login(send_email, send_pwd)
s.sendmail(send_email, recv_email, msg.as_string())
s.quit()
