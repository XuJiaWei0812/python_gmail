import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 郵件內容設定
msg = MIMEText('你好呀！這是用 Python 寄的信～', 'plain', 'utf-8') # 創建一個MIMEText物件，第一參數是郵件內容，第二參數是MIME的subtype，傳送純文字時使用'plain'
msg['Subject'] = Header('這是郵件標題', 'utf-8')                   # 郵件的標題，這裡需要使用Header物件進行編碼
msg['From'] = Header('發件人暱稱 <sender@example.com>', 'utf-8') # 發件人的名字和郵件地址
msg['To'] = 'receiver@example.com'                                # 收件人的郵件地址
msg['Cc'] = 'cc@example.com'                                      # 副本收件人郵件地址，可選

# SMTP服務器連接設定
try:
    smtp = smtplib.SMTP('smtp.gmail.com', 587) # 建立SMTP連接，這裡使用Gmail的SMTP服務器和默認的端口587
    smtp.ehlo()                                # 用來識別自己對SMTP伺服器說"hello"，是SMTP的一個命令
    smtp.starttls()                            # 啟用TLS加密，提高安全性
    smtp.login('your_email@gmail.com', 'your_app_password') # 使用Gmail帳號和應用程式密碼進行登錄

    # 發送郵件
    status = smtp.send_message(msg, from_addr='sender@example.com', to_addrs=['receiver@example.com', 'cc@example.com'])
    if status == {}:
        print('郵件傳送成功！')
    else:
        print('郵件傳送失敗！')
except Exception as e:
    print(f'發生錯誤：{e}')
finally:
    smtp.quit() # 斷開SMTP連接
