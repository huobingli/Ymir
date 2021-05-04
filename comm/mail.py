# 收发邮件
import email
import poplib
import poplib
import sys,os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from config.projectconfig import sign_mail_password, sign_mail_port_recv, sign_mail_port_send, sign_mail_server, sign_mail_user, mail_method
import telnetlib
import imaplib
import smtplib
from func_tools import tools
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email import message
from email.charset import Charset
from email.parser import Parser

class MailMIMEBase(message.Message):
    def __init__(self, _type):
        super(message.Message, self).__init__()
        self.add_header('Content-Type', str(_type))

class MailMIMEApp(MailMIMEBase):
    def __init__(self, content, file_name, _charset):
        if _charset is None:
            try:
                content.encode('us-ascii')
                _charset = 'us-ascii'
            except UnicodeDecodeError:
                _charset = "utf-8"
        if isinstance(_charset, Charset):
            _charset = str(_charset)
        super(MailMIMEBase, self).__init__(self, f'application/octet-stream; name="{file_name}"')
        self.set_payload(content, _charset)

class Mail:
    '''
    邮件模块
    '''
    @classmethod
    def makeMIMEMeassage(cls, **kwargs):
        '''
        构造mail传输数据
        '''
        msg = MIMEMultipart()
        for each in kwargs.keys():
            msg[each] = kwargs[each]1
        return msg
    
    @classmethod
    def makeFileMessage(cls, **kwargs):
        '''
        attach 文件流
        '''
        with open(kwargs["filename"], "rb", Charset='utf-8') as f:
            attach_file = MailMIMEApp(f.read())
            attach_file['Content-Disposition'] = f'attachment; filename="{kwargs["filename"]}"'
            return attach_file

    # @tools.funcWrap
    def sendMail(self, **kwargs):
        '''
        发送邮件
        '''
        server = self.connectMailServerByIMAP(sign_mail_port_send)
        message = self.makeMIMEMeassage(**kwargs)
        server.set_debuglevel(0)
        server.sendmail(from_addr=message["From"], to_addrs=message["To"], msg=message.as_string())

    def connectMailServerByPOP3(self, port=sign_mail_port_recv):
        '''
        POP3连接邮件服务器
        '''
        telnetlib.Telnet(sign_mail_server, port)
        server = poplib.POP3_SSL(sign_mail_server, port, timeout=100)
        server.user(sign_mail_user)
        server.pass_(sign_mail_password)
        return server
        '''
        resp, mails, octets = server.list()
        index = len(mails)
        resp, lines, octets = server.retr(index)
        msg_content = b'\r\n'.join(lines).decode('utf-8')
        msg = Parser().parsestr(msg_content)
        print(msg)
        return server
        '''

    def connectMailServerByIMAP(self, port=sign_mail_port_recv):
        '''
        IMAP连接邮件服务器
        '''
        server = smtplib.SMTP_SSL(host=sign_mail_server)
        server.connect(host=sign_mail_server, port=port)
        server.login(sign_mail_user, sign_mail_password)
        return server
    
    def receiveMails(self):
        server = None
        if mail_method == "POP3":
            server = self.connectMailServerByPOP3()
        elif mail_method == "IMAP":
            server = self.connectMailServerByIMAP()
        return server
    
mail = Mail()
if __name__ == "__main__":
    # di = {
    #     "From" : sign_mail_user,
    #     "To" : ",".join(["wangyang@test.com"]),
    #     "Subject" : Header("hello", 'utf-8')
    # }
    # mail.sendMail(**di)  # 字典组包发送
    # mail.sendMail(From=sign_mail_user, To=",".join(["wangyang@test.com"]), 'Subject'=Header("hello", 'utf-8')) #关键字发送
    
    #收取邮件 获取收取到的邮件的server
    server = mail.receiveMails()










