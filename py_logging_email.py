import logging
import logging.handlers
import time


mailhost = ('mail.system.cococococo.com',25)
print(type(mailhost))
fromaddr = 'aqumik@system.cococococo.com'
toaddrs = ['yunwei@cococococo.com']
subject = '【Jenkins】推送项目失败'
credentials = ('aqumik@system.cococococo.com','aqumik')
smtp_handler = logging.handlers.SMTPHandler(mailhost=mailhost,fromaddr=fromaddr,toaddrs=toaddrs,subject=subject,credentials=credentials)
# smtp_handler = logging.handlers.SMTPHandler(mailhost=("smtp.example.com",25),fromaddr="from@example.com",toaddrs="to@example.com",subject=u"AppName error!")

logger = logging.getLogger()
logger.addHandler(smtp_handler)
#
try:
  测试测试
except Exception as e:
  email_send_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
  logger.exception('邮件发送时间：%s\nJenkins推送失败\ncommit为\n\n报错信息如下：'%email_send_time)

