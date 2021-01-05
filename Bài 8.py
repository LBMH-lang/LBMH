import smtplib
import getpass
n = int( input('Số lần muốn gửi email'))
if n <= 0:
    print('vui lòng nhập lại số lần muốn gửi maill')
else:
    #Thông tin cơ bản
    email = input('Email của bạn là:')
    password = getpass.getpass('Password: ')
    address = input('Người nhận: ')
    msg = input('Nội dung:')
    #Gửi mail
    clinet = smtplib.SMTP('smtp.gmail.com',587)
    clinet.starttls()
    clinet.login(email , password)
    for i in range(n):
        clinet.sendmail(email , address , msg)
    print(n, 'tin nhắn đã được gửi tới', address)
    clinet.quit()
    
    