from flask import current_app
from app.Extensions import mail
from flask_mail import Message
from threading import Thread

def SeedEmail(sender, recipients, email_title, email_body='', email_html=''):
    '''发送邮件
    Args
        email_title(str)邮件名
        email_body(str)邮件内容
        email_html(str)邮件内容(html)
        sender(str)发件人
        recipients(list)收件人
    '''
    # 创建上下文
    app = current_app._get_current_object()

    # 创建邮件
    message = Message(email_title, sender=sender, recipients=recipients)
    message.body = email_body
    message.html = email_html
    
    # 异步提交
    thr = Thread(target=_send_async_mail, args=[app, message])
    thr.start()

def _send_async_mail(app, message):  # target function
    with app.app_context():
        mail.send(message)