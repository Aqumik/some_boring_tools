# -*-coding:utf-8-*-
from datetime import time
from email.header import Header
from email.mime.text import MIMEText
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
from email.mime.application import MIMEApplication


# user_logout(authid)


def sendMail(mailto, subject, body, format='plain'):
    # if isinstance(body,unicode):
    #     body = str(body)
    Date = time.ctime(time.time())
    print(Date)
    me = ("%s<" + fromMail + ">") % (Header("aqumik", 'utf-8'),)
    textApart = MIMEText(body, format, 'utf-8')
    msg = MIMEMultipart()
    # msg = MIMEText(body,format,'utf-8')
    # if not isinstance(subject,unicode):
    #     subject = unicode(subject)
    msg['Subject'] = subject
    msg['From'] = me
    msg['To'] = Header(mailto)
    msg['Date'] = Header(Date)
    msg["Accept-Language"] = "zh-CN"
    msg["Accept-Charset"] = "ISO-GBK-1,utf-8,GBK"

    # xlsFile = time + '.xlsx'
    # xlsApart = MIMEApplication(open(xlsFile, 'rb').read())
    # xlsApart.add_header('Content-Disposition', 'attachment', filename=xlsFile)

    # msg.attach(xlsApart)
    msg.attach(textApart)
    # print(msg)

    try:
        # s = smtplib.SMTP_SSL('mail.system.cooo.com', 465)
        s = smtplib.SMTP('mail.system.cooo.com', 25)
        # s.connect(host)
        s.login(user, password)
        s.sendmail(me, mailto, msg.as_string())
        s.close()
        print('邮件发送成功 ')
        return True
    except Exception as e:
        print(str(e))
        return False


host = 'aqumik@system.cooo.com'
user = 'aqumik@system.cooo.com'
fromMail = 'aqumik@system.cooo.com'  # mail from
body = 'gbk'
subjest = '测试'
password = 'aqumik'  # ********************Your email Password！！！！**********************
mailto = 'aqumik@cooo.com'  # mail to
sendMail(mailto, subjest, body)
