# 收邮件
import time
import sys
import os 
import base64

import poplib
import email
from email.parser import Parser
from email.header import decode_header 

import smtplib 
from email.header import Header 
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart  
from email.mime.nonmultipart import MIMENonMultipart
from email.charset import Charset 
from email import message
import telnetlib

import projectconfig from config
from comm import *


# 收邮件
def recv_mail(_save_file_dir):

    __ret = False;
    try:
        server = poplib.POP3_SSL(sign_mail_server, mail_recv_port, timeout=100)

        server.user(mail_user)
        server.pass_(mail_password) 

        resp, mails, octets = server.list()

        mail_count = len(mails)
        index = mail_count;

        msg = None;
        del_index = -1;
        while index > 0:
            resp, lines, octets = server.retr(index)
            msg_content = b'\r\n'.join(lines).decode('utf-8')
            msg = Parser().parsestr(msg_content)
            if check_recv_sign_mail(_check_title, msg) == True:
                del_index = index;
                break;
            else:
                index = index - 1;
        else:
            str_trace('no email with max recv count !!')
            msg = None; 
            __ret = False;

        if msg == None:
            str_trace("no mail !!");
        else:
            if not is_exists(_save_file_dir):
                os.makedirs(_save_file_dir)

            if get_attachment_file(_save_file_dir, msg):
                server.dele(del_index);
                __ret = True;

        server.quit();

    except BaseException as __exp:
        raise __exp;

    return __ret

# 收附件
def get_attachment_file(_save_path, _msg):
    attachment_files = []
    for part in _msg.walk():
        # 获取附件名称类型
        file_name = part.get_filename()
        if file_name:
            h = email.header.Header(file_name)
            # 对附件名称进行解
            dh = email.header.decode_header(h)
            filename = dh[0][0]
            if dh[0][1]:
                # 将附件名称可读化
                filename_tmp = name_decode_str(str(filename, dh[0][1]))
                filename = _decode_attach_file_name(filename_tmp);

                data = part.get_payload(decode=True)
                # 在指定目录下创建文件，注意二进制文件需要用wb模式打开
                delete_file(_save_path + '/' + filename)
                att_file = open(_save_path + '/' + filename, 'wb')
                attachment_files.append(filename)
                att_file.write(data)  # 保存附件
                att_file.close()
                
    return len(attachment_files);