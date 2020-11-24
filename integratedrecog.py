import cv2
import numpy as np
import RPi.GPIO as GPIO
import urllib3
#import urllib.request
import urlopen
import time
import os 
import os.path
from pyfingerprint.pyfingerprint import PyFingerprint
from random import *
#from pad4pi import rpi_gpio
#import pygame
from tkinter import*
import tkinter as tk 
from tkinter import Message, Text
import numpy as np 
from PIL import Image, ImageTk 
import pandas as pd
import time
import cv2 
import os 
import tkinter.ttk as ttk 
import tkinter.font as font
import serial


#******************************************#
myAPI='DJHQW435OIMH92IV'
baseURL='https://api.thingspeak.com/update?api_key=%s'%myAPI
a=0
b=0
c=0
d=0
e=0
f=0
g=0
q=0
n=0
j=0
l=0
m=0
voter1=0
voter2=0
k=''
L1 = 18
L2 = 23
L3 = 24
L4 = 25

C1 = 10
C2 = 9
C3 = 11
#C4 = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(L3, GPIO.OUT)
GPIO.setup(L4, GPIO.OUT)

GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
##    if(GPIO.input(C4) == 1):
##        print(characters[3])
def imshow(filename):
    img= pygame.image.load(filename)
    size=img.get_rect().size
    screen=pygame.display.set_mode(size)
    screen.blit(img,(0,0))
    pygame.display.flip()
def imclose():
    pygame.display.quit()
def readLinevote(line, characters):####
    global a,b,e,d,c,g,q,j,l,m,n
    GPIO.output(line, GPIO.HIGH)
    if(GPIO.input(C1) == 1):
        #print(characters[0])
        key=characters[0]
        #print(key)
        if(key=='1'):
            if(d==1):
                a=a+1
                #imshow('bjp.png')
                time.sleep(3)
                #imclose()
                BJP='%.2f'%a
                elec= 'http://embsmartevm.dbandroid.online/save_values.php?'+'party_id='+str(key)+'&user_id='+str(z)
                http = urllib3.PoolManager()   
                resp = http.request('GET', elec)   
                print(resp.status)   
                print(elec)    
                print("sent")    
                #print("Response: {}".format(conn.read()))
                #print(conn.read())
                #conn.close()
##                conn=urllib2.request.urlopen(baseURL+'&field1=%s'%(BJP))
##                print(conn.read())
##                conn.close()
                print("party 1:",a)
                lcd_string(str(key),LCD_LINE_2)
                d=0
                #k=''
        elif(key=='4'):
            if(d==1):
                c=c+1
                #imshow('tdp.png')
                time.sleep(3)
                #imclose()
                TDP='%.2f'%c
                elec= 'http://embsmartevm.dbandroid.online/save_values.php?'+'party_id='+str(key)+'&user_id='+str(z)
                http = urllib3.PoolManager()   
                resp = http.request('GET', elec)   
                print(resp.status)   
                print(elec)    
                print("sent")    
                #print("Response: {}".format(conn.read()))
                #print(conn.read())
                #conn.close()
##                conn=urllib2.request.urlopen(baseURL+'&field4=%s'%(TDP))
##                print(conn.read())
##                conn.close()
                print("party 4:",c)
                lcd_string(str(key),LCD_LINE_2)
                d=0
                #k=''
        elif(key=='7'):
            if(d==1):
                g=g+1
                #imshow('tdp.png')
                time.sleep(3)
                #imclose()
                a7='%.2f'%g
                elec= 'http://embsmartevm.dbandroid.online/save_values.php?'+'party_id='+str(key)+'&user_id='+str(z)
                http = urllib3.PoolManager()   
                resp = http.request('GET', elec)   
                print(resp.status)   
                print(elec)    
                print("sent")    
                #print("Response: {}".format(conn.read()))
                #print(conn.read())
                #conn.close()
##                conn=urllib2.request.urlopen(baseURL+'&field6=%s'%(a7))
##                print(conn.read())
##                conn.close()
                print("party 7:",g)
                lcd_string(str(key),LCD_LINE_2)
                d=0
                #k=''
    elif(GPIO.input(C2) == 1):
        #print(characters[1])
        key=characters[1]
        #print(key)
        if(key=='2'):
            if(d==1):
                b=b+1
                #imshow('ycp.jpeg')
                time.sleep(3)
                #imclose()
                YCP='%.2f'%b
                elec= 'http://embsmartevm.dbandroid.online/save_values.php?'+'party_id='+str(key)+'&user_id='+str(z)
                http = urllib3.PoolManager()   
                resp = http.request('GET', elec)   
                print(resp.status)   
                print(elec)    
                print("sent")    
                #print("Response: {}".format(conn.read()))
                #print(conn.read())
                #conn.close()
##                conn=urllib2.request.urlopen(baseURL+'&field2=%s'%(YCP))
##                print(conn.read())
##                conn.close()
                print("party 2:",b)
                lcd_string(str(key),LCD_LINE_2)
                d=0
                #k=''
        elif(key=='5'):
            if(d==1):
                q=q+1
                #imshow('tdp.png')
                time.sleep(3)
                #imclose()
                jsp='%.2f'%q
                elec= 'http://embsmartevm.dbandroid.online/save_values.php?'+'party_id='+str(key)+'&user_id='+str(z)
                http = urllib3.PoolManager()   
                resp = http.request('GET', elec)   
                print(resp.status)   
                print(elec)    
                print("sent")    
                #print("Response: {}".format(conn.read()))
                #print(conn.read())
                #conn.close()
##                conn=urllib2.request.urlopen(baseURL+'&field8=%s'%(a8))
##                print(conn.read())
##                conn.close()
                print("party 5:",q)
                lcd_string(str(key),LCD_LINE_2)
                d=0
                #k=''
        elif(key=='8'): 
            if(d==1):
                n=n+1
                #imshow('tdp.png')
                time.sleep(3)
                #imclose()
                a8='%.2f'%n
                elec= 'http://embsmartevm.dbandroid.online/save_values.php?'+'party_id='+str(key)+'&user_id='+str(z)
                http = urllib3.PoolManager()   
                resp = http.request('GET', elec)   
                print(resp.status)   
                print(elec)    
                print("sent")    
                #print("Response: {}".format(conn.read()))
                #print(conn.read())
                #conn.close()
##                conn=urllib2.request.urlopen(baseURL+'&field8=%s'%(a8))
##                print(conn.read())
##                conn.close()
                print("party 8:",n)
                lcd_string(str(key),LCD_LINE_2)
                d=0
        elif(key=='0'):
            if(d==1):
                j=j+1
                #imshow('tdp.png')
                time.sleep(3)
                #imclose()
                a0='%.2f'%j
                elec= 'http://embsmartevm.dbandroid.online/save_values.php?'+'party_id='+str(key)+'&user_id='+str(z)
                http = urllib3.PoolManager()   
                resp = http.request('GET', elec)   
                print(resp.status)   
                print(elec)    
                print("sent")    
                #print("Response: {}".format(conn.read()))
                #print(conn.read())
                #conn.close()
##                conn=urllib2.request.urlopen(baseURL+'&field5=%s'%(a0))
##                print(conn.read())
##                conn.close()
                print("party 0:",j)
                lcd_string(str(key),LCD_LINE_2)
                d=0
                #k=''
    elif(GPIO.input(C3) == 1):
        #print(characters[2])
        key=characters[2]
       # print(key)
        if(key=='3'):
            if(d==1):
                e=e+1
                #imshow('congress.png')
                time.sleep(3)
                #imclose()
                CONG='%.2f'%e
                elec= 'http://embsmartevm.dbandroid.online/save_values.php?'+'party_id='+str(key)+'&user_id='+str(z)
                http = urllib3.PoolManager()   
                resp = http.request('GET', elec)   
                print(resp.status)   
                print(elec)    
                print("sent")    
                #print("Response: {}".format(conn.read()))
                #print(conn.read())
                #conn.close()
##                conn=urllib2.request.urlopen(baseURL+'&field3=%s'%(CONG))
##                print(conn.read())
##                conn.close()
                print("party 3:",e)
                lcd_string(str(key),LCD_LINE_2)
                d=0
                #k=''
        elif(key=='6'):
            if(d==1):
                l=l+1
                #imshow('tdp.png')
                time.sleep(3)
                #imclose()
                a6='%.2f'%l
                elec= 'http://embsmartevm.dbandroid.online/save_values.php?'+'party_id='+str(key)+'&user_id='+str(z)
                http = urllib3.PoolManager()   
                resp = http.request('GET', elec)   
                print(resp.status)   
                print(elec)    
                print("sent")    
                #print("Response: {}".format(conn.read()))
                #print(conn.read())
                #conn.close()
##                conn=urllib2.request.urlopen(baseURL+'&field7=%s'%(a6))
##                print(conn.read())
##                conn.close()
                print("party 6:",l)
                lcd_string(str(key),LCD_LINE_2)
                d=0
                #k=''
        elif(key=='9'):
            if(d==1):
                m=m+1
                #imshow('tdp.png')
                time.sleep(3)
                #imclose()
                a9='%.2f'%m
                elec= 'http://embsmartevm.dbandroid.online/save_values.php?'+'party_id='+str(key)+'&user_id='+str(z)
                http = urllib3.PoolManager()   
                resp = http.request('GET', elec)   
                print(resp.status)   
                print(elec)    
                print("sent")    
                #print("Response: {}".format(conn.read()))
                #print(conn.read())
                #conn.close()
##                conn=urllib2.request.urlopen(baseURL+'&field9=%s'%(a9))
##                print(conn.read())
##                conn.close()
                print("party 9:",m)
                lcd_string(str(key),LCD_LINE_2)
                d=0
                #k=''
    GPIO.output(line, GPIO.LOW)
LCD_RS=17
LCD_E=27
LCD_D4=6
LCD_D5=13
LCD_D6=19
LCD_D7=26
buzz=5
LCD_WIDTH=16
LCD_CHR= True
LCD_CMD= False

LCD_LINE_1 = 0x80
LCD_LINE_2 = 0xc0

E_PULSE = 0.001
E_DELAY = 0.001
def lcd_init():
    lcd_byte(0x33,LCD_CMD)
    lcd_byte(0x32,LCD_CMD)
    lcd_byte(0x06,LCD_CMD)
    lcd_byte(0x0c,LCD_CMD)
    lcd_byte(0x28,LCD_CMD)
    lcd_byte(0x01,LCD_CMD)
    time.sleep(E_DELAY)

def lcd_byte(bits,mode):
    GPIO.output(LCD_RS,mode)
    GPIO.output(LCD_D4,False)
    GPIO.output(LCD_D5,False)
    GPIO.output(LCD_D6,False)
    GPIO.output(LCD_D7,False)
    if bits&0x10==0x10:
        GPIO.output(LCD_D4,True)
    if bits&0x20==0x20:
        GPIO.output(LCD_D5,True)
    if bits&0x40==0x40:
        GPIO.output(LCD_D6,True)
    if bits&0x80==0x80:
        GPIO.output(LCD_D7,True)
    lcd_toggle_enable()

    GPIO.output(LCD_D4,False)
    GPIO.output(LCD_D5,False)
    GPIO.output(LCD_D6,False)
    GPIO.output(LCD_D7,False)
    if bits&0x01==0x01:
        GPIO.output(LCD_D4,True)
    if bits&0x02==0x02:
        GPIO.output(LCD_D5,True)
    if bits&0x04==0x04:
        GPIO.output(LCD_D6,True)
    if bits&0x08==0x08:
        GPIO.output(LCD_D7,True)

    lcd_toggle_enable()

def lcd_toggle_enable():
    time.sleep(E_DELAY)
    GPIO.output(LCD_E,True)
    time.sleep(E_PULSE)
    GPIO.output(LCD_E,False)
    time.sleep(E_DELAY)

def lcd_string(message,line):
    message=message.ljust(LCD_WIDTH," ")
    lcd_byte(line,LCD_CMD)
    for i in range(LCD_WIDTH):
        lcd_byte(ord(message[i]),LCD_CHR)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LCD_E, GPIO.OUT)
GPIO.setup(LCD_RS,GPIO.OUT)
GPIO.setup(LCD_D4,GPIO.OUT)
GPIO.setup(LCD_D5,GPIO.OUT)
GPIO.setup(LCD_D6,GPIO.OUT)
GPIO.setup(LCD_D7,GPIO.OUT)
GPIO.setup(buzz,GPIO.OUT)
lcd_init()
##KEYPAD = [
##    ["1", "2", "3"],
##    ["4", "5", "6"],
##    ["7", "8", "9"],
##    ["*", "0", "#"]
##]
##
##COL_PINS = [10, 9, 11] # BCM numbering
##ROW_PINS = [18,23,24,25] # BCM numbering
##
##factory = rpi_gpio.KeypadFactory()
##keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)

##******************************************#
##def printKey(key):
##        print(key)
##        return(key)
##        #time.sleep(5)
##        global c,d,e,f
##        if key== 1:
##           c=c+1
##           print(c)
##        elif key==2:
##           d=d+1
##           print(d)
##        elif key==3:
##           e=e+1
##           print(e)
##        elif key==4:
##           f=f+1
##           print(f)
##        #lcd_string(ord(key),LCD_CHR)
##        #print(key)
##    ##def printKey(key):
##    #lcd_byte(ord(key),LCD_CHR)
##        print(key)

###******************************************#
##
### printKey will be called each time a keypad button is pressed
##keypad.registerKeyPressHandler(printKey)
try:
    f = PyFingerprint('/dev/ttyS0', 57600, 0xFFFFFFFF, 0x00000000)

    if ( f.verifyPassword() == False ):
        raise ValueError('The given fingerprint sensor password is wrong!')

except Exception as e:
    print('The fingerprint sensor could not be initialized!')
    print('Exception message: ' + str(e))   
#while True:
            
##recognizer = cv2.face.LBPHFaceRecognizer_create()
##recognizer.read('trainer.yml')
##cascadePath = "haarcascade_frontalface_default.xml"
##faceCascade = cv2.CascadeClassifier(cascadePath);
##
##font = cv2.FONT_HERSHEY_SIMPLEX
##
###iniciate id counter
##id = 0
##
### names related to ids: example ==> Marcelo: id=1,  etc
##names = ['None', 'user1', 'user2', 'user3', 'user4', 'user5'] 
##
### Initialize and start realtime video capture
##cam = cv2.VideoCapture(0)
#cam.set(3, 640) # set video widht
#cam.set(4, 480) # set video height

# Define min window size to be recognized as a face
#minW = 0.1*cam.get(3)
#minH = 0.1*cam.get(4)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzz,GPIO.LOW)
i=0
count=1
def wind():
    window = tk.Tk() 
    window.title("ELECTIONS")
    window.geometry("1350x695+0+0")
    window.resizable(width=False,height=False)
    window.configure(background ='white') 
    window.grid_rowconfigure(0, weight = 1) 
    window.grid_columnconfigure(0, weight = 1) 
    message = tk.Label( 
        window, text ="PARTY", 
        bg ="white", fg = "black",# width = 50, 
       # height = 3,
        font = ('times', 30, 'bold')) 
        
    message.place(x = 650, y = 0) 
    tdp=Image.open("/home/pi/Desktop/Main codes/Reference-main/tdp.jpeg")
    resize_tdp=tdp.resize((200,200),Image.ANTIALIAS)
    tdp_new=ImageTk.PhotoImage(resize_tdp)
    tdp_label=Label(image=tdp_new)#,height=300,width=500)
    tdp_label.pack(pady=20)
    tdp_label.place(x=1100,y=100)
    ##
    bjp=Image.open("/home/pi/Desktop/Main codes/Reference-main/BJPI.png")
    resize_bjp=bjp.resize((200,200),Image.ANTIALIAS)
    bjp_new=ImageTk.PhotoImage(resize_bjp)
    bjp_label=Label(image=bjp_new)#,height=300,width=500)
    bjp_label.pack(pady=20)
    bjp_label.place(x=365,y=100)
    ##
    cong=Image.open("/home/pi/Desktop/Main codes/Reference-main/congress.jpeg")
    resize_cong=cong.resize((200,200),Image.ANTIALIAS)
    cong_new=ImageTk.PhotoImage(resize_cong)
    cong_label=Label(image=cong_new)#,height=300,width=500)
    cong_label.pack(pady=20)
    cong_label.place(x=855,y=100)
    ##
    ycp=Image.open("/home/pi/Desktop/Main codes/Reference-main/ycp.jpeg")
    resize_ycp=ycp.resize((200,200),Image.ANTIALIAS)
    ycp_new=ImageTk.PhotoImage(resize_ycp)
    ycp_label=Label(image=ycp_new)#,height=300,width=500)
    ycp_label.pack(pady=20)
    ycp_label.place(x=600,y=95)

    o0=Image.open("/home/pi/Desktop/Main codes/Reference-main/teapot.jpeg")
    resize_o0=o0.resize((200,200),Image.ANTIALIAS)
    o0_new=ImageTk.PhotoImage(resize_o0)
    o0_label=Label(image=o0_new)#,height=300,width=500)
    o0_label.pack(pady=20)
    o0_label.place(x=110,y=95)

    o5=Image.open("/home/pi/Desktop/Main codes/Reference-main/match.jpeg")
    resize_o5=o5.resize((200,200),Image.ANTIALIAS)
    o5_new=ImageTk.PhotoImage(resize_o5)
    o5_label=Label(image=o5_new)#,height=300,width=500)
    o5_label.pack(pady=20)
    o5_label.place(x=110,y=385)

    o6=Image.open("/home/pi/Desktop/Main codes/Reference-main/mug.png")
    resize_o6=o6.resize((200,200),Image.ANTIALIAS)
    o6_new=ImageTk.PhotoImage(resize_o6)
    o6_label=Label(image=o6_new)#,height=300,width=500)
    o6_label.pack(pady=20)
    o6_label.place(x=370,y=385)

    o7=Image.open("/home/pi/Desktop/Main codes/Reference-main/mango.png")
    resize_o7=o7.resize((200,200),Image.ANTIALIAS)
    o7_new=ImageTk.PhotoImage(resize_o7)
    o7_label=Label(image=o7_new)#,height=300,width=500)
    o7_label.pack(pady=20)
    o7_label.place(x=600,y=385)

    o8=Image.open("/home/pi/Desktop/Main codes/Reference-main/tail.png")
    resize_o8=o8.resize((200,200),Image.ANTIALIAS)
    o8_new=ImageTk.PhotoImage(resize_o8)
    o8_label=Label(image=o8_new)#,height=300,width=500)
    o8_label.pack(pady=20)
    o8_label.place(x=860,y=385)

    o9=Image.open("/home/pi/Desktop/Main codes/Reference-main/duck.jpeg")
    resize_o9=o9.resize((200,200),Image.ANTIALIAS)
    o9_new=ImageTk.PhotoImage(resize_o9)
    o9_label=Label(image=o9_new)#,height=300,width=500)
    o9_label.pack(pady=20)
    o9_label.place(x=1100,y=385)

    party0 = tk.Button(window, text ="0. 0", 
    ##command = party1,
    fg ="white", bg ="green", 
    width = 20, height = 3, activebackground = "Red", 
    font =('times', 15, ' bold ')) 
    party0.place(x = 100, y = 300)
    #window.mainloop()
    party1 = tk.Button(window, text ="1. BJP", 
    ##command = party1,
    fg ="white", bg ="green", 
    width = 20, height = 3, activebackground = "Red", 
    font =('times', 15, ' bold ')) 
    party1.place(x = 350, y = 300) 
    party2 = tk.Button(window, text ="2. YCP", 
    #command = party2,
    fg ="white", bg ="green", 
    width = 20, height = 3, activebackground = "Red", 
    font =('times', 15, ' bold ')) 
    party2.place(x = 590, y = 300) 
    party3 = tk.Button(window, text ="3. CONGRESS", 
    #command = party3,
    fg ="white", bg ="green", 
    width = 20, height = 3, activebackground = "Red", 
    font =('times', 15, ' bold ')) 
    party3.place(x = 840, y = 300)
    party4 = tk.Button(window, text ="4. TDP", 
    #command = party4,
    fg ="white", bg ="green", 
    width = 20, height = 3, activebackground = "Red", 
    font =('times', 15, ' bold ')) 
    party4.place(x = 1090, y = 300)
    party5 = tk.Button(window, text ="5.5 ", 
    #command = party4,
    fg ="white", bg ="green", 
    width = 20, height = 3, activebackground = "Red", 
    font =('times', 15, ' bold ')) 
    party5.place(x = 100, y = 590)
    party6 = tk.Button(window, text ="6. 6", 
    #command = party4,
    fg ="white", bg ="green", 
    width = 20, height = 3, activebackground = "Red", 
    font =('times', 15, ' bold ')) 
    party6.place(x = 350, y = 590)
    party7 = tk.Button(window, text ="7. 7", 
    #command = party4,
    fg ="white", bg ="green", 
    width = 20, height = 3, activebackground = "Red", 
    font =('times', 15, ' bold ')) 
    party7.place(x = 590, y = 590)
    party8 = tk.Button(window, text ="8. 8", 
    #command = party4,
    fg ="white", bg ="green", 
    width = 20, height = 3, activebackground = "Red", 
    font =('times', 15, ' bold ')) 
    party8.place(x = 840, y = 590)
    party9 = tk.Button(window, text ="9. 9", 
    ##command = party1,
    fg ="white", bg ="green", 
    width = 20, height = 3, activebackground = "Red", 
    font =('times', 15, ' bold ')) 
    party9.place(x = 1090, y = 590)
    quitWindow = tk.Button(window, text ="check party and click here", 
    command = window.destroy, fg ="white", bg ="green", 
    width = 20, height = 3, activebackground = "Red", 
    font =('times', 15, ' bold ')) 
    quitWindow.place(x = 0, y = 0) 
    window.mainloop()

    #time.sleep(10)
    #window.destroy()
    #return 0
#def camera():
  #global count,i,k,voter1
    
  
##                readLinevote(L1, ["1","2","3"])
##                readLinevote(L2, ["4","5","6"])
##                readLinevote(L3, ["7","8","9"])
##                readLinevote(L4, ["*","0","#"])
##                time.sleep(0.1)
##                time.sleep(5)
  
#return(str(id))

while True:
    readLinevote(L1, ["1","2","3"])
    readLinevote(L2, ["4","5","6"])
    readLinevote(L3, ["7","8","9"])
    readLinevote(L4, ["*","0","#"])
    time.sleep(0.1)
    if(d==0):
        lcd_string("Enter Aadhar",LCD_LINE_1)
        #k=''
        def readLine(line, characters):
                #k=''
                global k
                GPIO.output(line, GPIO.HIGH)
                if(GPIO.input(C1) == 1):
                    #print(characters[0])
                    key=characters[0]
                    #print(key)
                    if(len(str(k))<5):
                        if(key=='1'):
                            #print("working...")
                            k=str(k)+key
                            print(k)
                            lcd_string(str(k),LCD_LINE_2)
                        if(key=='4'):
                            #print("working...")
                            k=str(k)+key
                            print(k)
                            lcd_string(str(k),LCD_LINE_2)
                        if(key=='7'):
                            #print("working...")
                            k=str(k)+key
                            print(k)
                            lcd_string(str(k),LCD_LINE_2)
                if(GPIO.input(C2) == 1):
                    #print(characters[1])
                    key=characters[1]
                    if(len(str(k))<5):
                    #print(key)
                        if(key=='2'):
                            #print("working...")
                            k=str(k)+key
                            print(k)
                            lcd_string(str(k),LCD_LINE_2)
                        if(key=='5'):
                            #print("working...")
                            k=str(k)+key
                            print(k)
                            lcd_string(str(k),LCD_LINE_2)
                        if(key=='8'):
                            #print("working...")
                            k=str(k)+key
                            print(k)
                            lcd_string(str(k),LCD_LINE_2)
                        if(key=='0'):
                            #print("working...")
                            k=str(k)+key
                            print(k)
                            lcd_string(str(k),LCD_LINE_2)
                if(GPIO.input(C3) == 1):
                    #print(characters[2])
                    key=characters[2]
                    if(len(str(k))<5):
                    #print(key)
                        if(key=='3'):
                            #print("working...")
                            k=str(k)+key
                            print(k)
                            lcd_string(str(k),LCD_LINE_2)
                        if(key=='6'):
                            #print("working...")
                            k=str(k)+key
                            print(k)
                            lcd_string(str(k),LCD_LINE_2)
                        if(key=='9'):
                            #print("working...")
                            k=str(k)+key
                            print(k)
                            lcd_string(str(k),LCD_LINE_2)
                    if(len(str(k))==5):
                        if(key=='#'):
                            print(k)
            ##    if(GPIO.input(C4) == 1):
            ##        print(characters[3])
                
                GPIO.output(line, GPIO.LOW)
                return(len(str(k)),str(k))
    readLine(L1, ["1","2","3"])
    readLine(L2, ["4","5","6"])
    readLine(L3, ["7","8","9"])
    readLine(L4, ["*","0","#"])
    time.sleep(0.1)
    #time.sleep(20)
    #lcd_string("Place your thumb",LCD_LINE_1)
    if(len(str(k))==5):
     if(str(k)=='12345'):
       if(voter1==0):
        GPIO.output(buzz, GPIO.LOW)
##        conn=urllib2.request.urlopen(baseURL+'&field8=%s'%(str(k)))
##        print(conn.read())
##        conn.close()
        lcd_string("Place ur finger",LCD_LINE_1)
        lcd_string("and wait",LCD_LINE_2)
        print('Waiting for finger...')
        time.sleep(2)
    ## Wait that finger is read
        while ( f.readImage() == False ):
             pass

    ## Converts read image to characteristics and stores it in charbuffer 1
        f.convertImage(0x01)

    ## Searchs template
        result = f.searchTemplate()

        positionNumber = result[0]
        accuracyScore = result[1]
        if(positionNumber==1):
            #b=1
            #f=1
            z=str(positionNumber)
            print('Found template at position #' + str(positionNumber))
            print('The accuracy score is: ' + str(accuracyScore))
            os.system('python /home/pi/open.py')
            wind()
            #lcd_string("1.BJP 2.YCP",LCD_LINE_1)
            #lcd_string("3.CONG 4.TDP",LCD_LINE_2)
            time.sleep(2)              
            lcd_string("PRESS &WAIT",LCD_LINE_1)
            lcd_string("  ",LCD_LINE_2)
            d=1
            #time.sleep(8)
            k=''
            voter1=1
        elif ( positionNumber != 1 ):
            #print('No match found!')
            y=0
            lcd_string("fingr not matchd",LCD_LINE_1)
            lcd_string("",LCD_LINE_2)
            time.sleep(1)
            #camera()
            recognizer = cv2.face.createLBPHFaceRecognizer()
            recognizer.load('trainer.yml')
            cascadePath = "haarcascade_frontalface_default.xml"
            faceCascade = cv2.CascadeClassifier(cascadePath);

            font = cv2.FONT_HERSHEY_SIMPLEX

            lcd_string("Look at camera",LCD_LINE_1)
                #iniciate id counter
            id = 0

                # names related to ids: example ==> Marcelo: id=1,  etc
            names = ['None', 'user1', 'user2', 'user3', 'user4', 'user5'] 

                # Initialize and start realtime video capture
            cam = cv2.VideoCapture(0)
            while True:
              ret, img =cam.read()
                #img = cv2.flip(img, -1) # Flip vertically
              gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                
              faces = faceCascade.detectMultiScale(gray,1.2,5)
            ##        gray,
            ##        scaleFactor = 1.2,
            ##        minNeighbors = 5,
            ##        minSize = (int(minW), int(minH)),
            ##       )

              for(x,y,w,h) in faces:
                  cv2.rectangle(img, (x,y), (x+w,y+h), (225,0,0), 2)
                  id, confidence = recognizer.predict(gray[y:y+h,x:x+w])


                    # Check if confidence is less them 100 ==> "0" is perfect match 
                  if (confidence < 60):
                      z=id
                      id = names[id]
                        
                      confidence = "  {0}%".format(round(100 - confidence))
                      if(count == 1):
                                  print('face id:',str(id),' detected')
                                    
                                  count =2
                                  i=0
                                  k=''
                                                
                  else:
                      id = "unknown"
                      print('no face detected')
                      confidence = "  {0}%".format(round(100 - confidence))
                        
                      time.sleep(0.1)

                        
                  cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
                  cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
                  #return(str(id))
                  if(str(id)=='user1'):
                    if(voter1==0):
                      k=''
                      print("Opening party id's")
                      time.sleep(1)
                        #k=''
                      wind()
                      time.sleep(3)
                      d=1
                            #lcd_string("1.BJP 2.YCP",LCD_LINE_1)
                            #lcd_string("3.CONG 4.TDP",LCD_LINE_2)
                        #time.sleep(4)
                            #lcd_string("1.BJP 2.YCP",LCD_LINE_1)
                            #lcd_string("3.CONG 4.TDP",LCD_LINE_2)
                           # time.sleep(6)              
                ##                    lcd_string("PRESS &WAIT",LCD_LINE_1)
                ##                    lcd_string("  ",LCD_LINE_2)
                        #    d=1
                            #time.sleep(8)
                        #k=''
                      lcd_string("PRESS &WAIT ",LCD_LINE_1)
                      lcd_string("  ",LCD_LINE_2)
                      time.sleep(0.1)
                      time.sleep(5)
            ##        elif(str(id)=='user2'):
            ##            print("Opening party id's")
            ##            time.sleep(1)
            ##            #k=''
            ##            wind()
            ##            time.sleep(3)
            ##            d=1
            ##                #lcd_string("1.BJP 2.YCP",LCD_LINE_1)
            ##                #lcd_string("3.CONG 4.TDP",LCD_LINE_2)
            ##            #time.sleep(4)
            ##                #lcd_string("1.BJP 2.YCP",LCD_LINE_1)
            ##                #lcd_string("3.CONG 4.TDP",LCD_LINE_2)
            ##               # time.sleep(6)              
            ##    ##                    lcd_string("PRESS &WAIT",LCD_LINE_1)
            ##    ##                    lcd_string("  ",LCD_LINE_2)
            ##            #    d=1
            ##                #time.sleep(8)
            ##            #k=''
            ##            voter2=1
            ##            lcd_string("PRESS &WAIT ",LCD_LINE_1)
            ##            lcd_string("  ",LCD_LINE_2)
                  elif(str(id)=='unknown'): 
                      lcd_string('Invalid voter',LCD_LINE_1)
                      lcd_string("  ",LCD_LINE_2)
              cv2.imshow('camera',img)
              i= i+1
                #print('i: ',int(i))
              if(i == 100):
                    #print('i: ',int(i))
                  count=1
                  i=0

              if (str(id)=='user1'):
                  d=1
                  #voter1=1
                  break# Press 'ESC' for exiting video
              if cv2.waitKey(10) & 0xff== ord('q'):
                  break
            ##    elif k == 60:
            ##        break

            # Do a bit of cleanup
            print("\n [INFO] Exiting Program and cleanup stuff")
            cam.release()
            cv2.destroyAllWindows()
            voter1=1
            #y=0
            
##                else:
##                    id = "unknown"
##                    print('no face detected')
##                    lcd_string("Invalid candid",LCD_LINE_1)
##                    lcd_string("         ",LCD_LINE_2)
##                    confidence = "  {0}%".format(round(100 - confidence))
##                    k=''
##                    time.sleep(0.1)     
        ##            #a=1            
                   
                
       elif(voter1==1):
           GPIO.output(buzz, GPIO.HIGH)
           #buzz=1
           k=''
##     elif(str(k)!='12345'):
##         k=''
##         GPIO.output(buzz, GPIO.LOW)
     elif(str(k)=='54321'):
       if(voter2==0):
##        conn=urllib2.request.urlopen(baseURL+'&field8=%s'%(str(k)))
##        print(conn.read())
##        conn.close()
        GPIO.output(buzz, GPIO.LOW)
        lcd_string("Place ur finger",LCD_LINE_1)
        lcd_string("and wait",LCD_LINE_2)
        print('Waiting for finger...')
        time.sleep(2)
    ## Wait that finger is read
        while ( f.readImage() == False ):
             pass

    ## Converts read image to characteristics and stores it in charbuffer 1
        f.convertImage(0x01)

    ## Searchs template
        result = f.searchTemplate()

        positionNumber = result[0]
        accuracyScore = result[1] 
        if(positionNumber==2):
            z=str(positionNumber)
            print('Found template at position #' + str(positionNumber))
            print('The accuracy score is: ' + str(accuracyScore))
            os.system('python /home/pi/open.py')
            wind()
            #lcd_string("1.BJP 2.YCP",LCD_LINE_1)
            #lcd_string("3.CONG 4.TDP",LCD_LINE_2)
            time.sleep(2)              
            lcd_string("PRESS &WAIT",LCD_LINE_1)
            lcd_string("  ",LCD_LINE_2)
            d=1
            #time.sleep(8)
            k=''
            voter2=1
        elif ( positionNumber != 2 ):
            #print('No match found!')
            y=0
            lcd_string("fingr not matchd",LCD_LINE_1)
            lcd_string("",LCD_LINE_2)
            time.sleep(1)
            #camera()
            recognizer = cv2.face.createLBPHFaceRecognizer()
            recognizer.load('trainer.yml')
            cascadePath = "haarcascade_frontalface_default.xml"
            faceCascade = cv2.CascadeClassifier(cascadePath);

            font = cv2.FONT_HERSHEY_SIMPLEX
            lcd_string("Look at camera",LCD_LINE_1)
                #iniciate id counter
            id = 0

                # names related to ids: example ==> Marcelo: id=1,  etc
            names = ['None', 'user1', 'user2', 'user3', 'user4', 'user5'] 

                # Initialize and start realtime video capture
            cam = cv2.VideoCapture(0)
            while True:
              ret, img =cam.read()
                #img = cv2.flip(img, -1) # Flip vertically
              gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                
              faces = faceCascade.detectMultiScale(gray,1.2,5)
            ##        gray,
            ##        scaleFactor = 1.2,
            ##        minNeighbors = 5,
            ##        minSize = (int(minW), int(minH)),
            ##       )

              for(x,y,w,h) in faces:
                  cv2.rectangle(img, (x,y), (x+w,y+h), (225,0,0), 2)
                  id, confidence = recognizer.predict(gray[y:y+h,x:x+w])


                    # Check if confidence is less them 100 ==> "0" is perfect match 
                  if (confidence < 60):
                      z=id
                      id = names[id]
                        
                      confidence = "  {0}%".format(round(100 - confidence))
                      if(count == 1):
                                  print('face id:',str(id),' detected')
                                    
                                  count =2
                                  i=0
                                  k=''
                                                
                  else:
                      id = "unknown"
                      print('no face detected')
                      confidence = "  {0}%".format(round(100 - confidence))
                        
                      time.sleep(0.1)

                        
                  cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
                  cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
                  #return(str(id))
                  if(str(id)=='user2'):
                    if(voter2==0):
                      print("Opening party id's")
                      time.sleep(1)
                        #k=''
                      wind()
                      time.sleep(3)
                      d=1
                            #lcd_string("1.BJP 2.YCP",LCD_LINE_1)
                            #lcd_string("3.CONG 4.TDP",LCD_LINE_2)
                        #time.sleep(4)
                            #lcd_string("1.BJP 2.YCP",LCD_LINE_1)
                            #lcd_string("3.CONG 4.TDP",LCD_LINE_2)
                           # time.sleep(6)              
                ##                    lcd_string("PRESS &WAIT",LCD_LINE_1)
                ##                    lcd_string("  ",LCD_LINE_2)
                        #    d=1
                            #time.sleep(8)
                        #k=''
                      lcd_string("PRESS &WAIT ",LCD_LINE_1)
                      lcd_string("  ",LCD_LINE_2)
                      time.sleep(0.1)
                      time.sleep(5)
            ##        elif(str(id)=='user2'):
            ##            print("Opening party id's")
            ##            time.sleep(1)
            ##            #k=''
            ##            wind()
            ##            time.sleep(3)
            ##            d=1
            ##                #lcd_string("1.BJP 2.YCP",LCD_LINE_1)
            ##                #lcd_string("3.CONG 4.TDP",LCD_LINE_2)
            ##            #time.sleep(4)
            ##                #lcd_string("1.BJP 2.YCP",LCD_LINE_1)
            ##                #lcd_string("3.CONG 4.TDP",LCD_LINE_2)
            ##               # time.sleep(6)              
            ##    ##                    lcd_string("PRESS &WAIT",LCD_LINE_1)
            ##    ##                    lcd_string("  ",LCD_LINE_2)
            ##            #    d=1
            ##                #time.sleep(8)
            ##            #k=''
            ##            voter2=1
            ##            lcd_string("PRESS &WAIT ",LCD_LINE_1)
            ##            lcd_string("  ",LCD_LINE_2)
                  elif(str(id)=='unknown'): 
                      lcd_string('Invalid voter',LCD_LINE_1)
                      lcd_string("  ",LCD_LINE_2)
              cv2.imshow('camera',img)
              i= i+1
                #print('i: ',int(i))
              if(i == 100):
                    #print('i: ',int(i))
                  count=1
                  i=0

              if (str(id)=='user2'):
                  d=1
                  #voter2=1
                  break# Press 'ESC' for exiting video
              if cv2.waitKey(10) & 0xff== ord('q'):
                  break
            ##    elif k == 60:
            ##        break

            # Do a bit of cleanup
            print("\n [INFO] Exiting Program and cleanup stuff")
            cam.release()
            cv2.destroyAllWindows()
            voter2=1
            #y=0
##                else:
##                    id = "unknown"
##                    print('no face detected')
##                    lcd_string("Invalid candid",LCD_LINE_1)
##                    lcd_string("         ",LCD_LINE_2)
##                    confidence = "  {0}%".format(round(100 - confidence))
##                    k=''
##                    time.sleep(0.1)     
        ##            #a=1            
                   
                
       elif(voter2==1):
           GPIO.output(buzz, GPIO.HIGH)
           #buzz=1
           k=''
     elif(str(k)!='54321' or str(k)!='12345'):
         k=''
         GPIO.output(buzz, GPIO.LOW)
         
              
# printKey will be called each time a keypad button is pressed
            #positionNumber1=positionNumber
            #if str(k)==str(positionNumber):
        
                #time.sleep(5)
                #keypad.registerKeyPressHandler(printKey)
                #lcd_byte(ord(key),LCD_CHR)
                #print(key)
