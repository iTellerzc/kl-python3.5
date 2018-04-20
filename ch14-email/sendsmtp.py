#! /usr/bin/python3
#-*-coding:UTF-8-*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header
sender = '1084197477@qq.com'
pwd = 'pqkuckgixwklicbg'
receivers=['iTeller_zc@163.com']

#三个参数：第一个为文本内容，第二个plain设置文本格式，第三个设置utf-8编码
message = MIMEText('tracy：你好啊！python问题请教你！', 'plain', 'utf-8')
message['From'] = Header('iTeller_zc', 'utf-8')
message['To'] = Header('tracy', 'utf-8')

subject = 'tracy, this is Python SMTP邮件'
message['Subject'] = Header(subject, 'utf-8')

try:
	smptObj = smtplib.SMTP_SSL("smtp.qq.com", 465)
	smptObj.login(sender, pwd)
	smptObj.sendmail(sender, receivers, message.as_string())
	print('邮件发送成功')
except smtplib.SMTPException as e:
	print('Error:无法发送邮件.Case%s'%e)