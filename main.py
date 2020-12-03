import time
from pyfingerprint.pyfingerprint import PyFingerprint
import RPi.GPIO as gpio
import serial
import urllib3
from urllib.request import urlopen
from array import *
a=array('i', [-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12])
pos=array('i',[1234,2345,3456,4567,5678,6789,7890,8901,123])
n=40
RS =7
EN =8
D4 =25
D5 =24
D6 =23
D7 =18
party1=22
party2=27
party3=17

enrol=5
delet=6
inc=13
dec=19
iden=26

buzz=1


l=0
y=0
k=0
d=0
##HIGH=1
##LOW=0

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(RS, gpio.OUT)
gpio.setup(EN, gpio.OUT)
gpio.setup(D4, gpio.OUT)
gpio.setup(D5, gpio.OUT)
gpio.setup(D6, gpio.OUT)
gpio.setup(D7, gpio.OUT)
gpio.setup(buzz, gpio.OUT)

gpio.setup(enrol, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(delet, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(inc, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(dec, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(iden, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(party1, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(party2, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(party3, gpio.IN, pull_up_down=gpio.PUD_UP)
#gpio.setup(led, gpio.OUT)
gpio.output(buzz, gpio.LOW)
try:
    f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

    if ( f.verifyPassword() == False ):
        raise ValueError('The given fingerprint sensor password is wrong!')

except Exception as e:
    print('Exception message: ' + str(e))
    exit(1)

def begin():
  lcdcmd(0x33) 
  lcdcmd(0x32) 
  lcdcmd(0x06)
  lcdcmd(0x0C) 
  lcdcmd(0x28) 
  lcdcmd(0x01) 
  time.sleep(0.0005)
 
def lcdcmd(ch): 
  gpio.output(RS, 0)
  gpio.output(D4, 0)
  gpio.output(D5, 0)
  gpio.output(D6, 0)
  gpio.output(D7, 0)
  if ch&0x10==0x10:
    gpio.output(D4, 1)
  if ch&0x20==0x20:
    gpio.output(D5, 1)
  if ch&0x40==0x40:
    gpio.output(D6, 1)
  if ch&0x80==0x80:
    gpio.output(D7, 1)
  gpio.output(EN, 1)
  time.sleep(0.005)
  gpio.output(EN, 0)
  # Low bits
  gpio.output(D4, 0)
  gpio.output(D5, 0)
  gpio.output(D6, 0)
  gpio.output(D7, 0)
  if ch&0x01==0x01:
    gpio.output(D4, 1)
  if ch&0x02==0x02:
    gpio.output(D5, 1)
  if ch&0x04==0x04:
    gpio.output(D6, 1)
  if ch&0x08==0x08:
    gpio.output(D7, 1)
  gpio.output(EN, 1)
  time.sleep(0.005)
  gpio.output(EN, 0)
  
def lcdwrite(ch): 
  gpio.output(RS, 1)
  gpio.output(D4, 0)
  gpio.output(D5, 0)
  gpio.output(D6, 0)
  gpio.output(D7, 0)
  if ch&0x10==0x10:
    gpio.output(D4, 1)
  if ch&0x20==0x20:
    gpio.output(D5, 1)
  if ch&0x40==0x40:
    gpio.output(D6, 1)
  if ch&0x80==0x80:
    gpio.output(D7, 1)
  gpio.output(EN, 1)
  time.sleep(0.005)
  gpio.output(EN, 0)
  # Low bits
  gpio.output(D4, 0)
  gpio.output(D5, 0)
  gpio.output(D6, 0)
  gpio.output(D7, 0)
  if ch&0x01==0x01:
    gpio.output(D4, 1)
  if ch&0x02==0x02:
    gpio.output(D5, 1)
  if ch&0x04==0x04:
    gpio.output(D6, 1)
  if ch&0x08==0x08:
    gpio.output(D7, 1)
  gpio.output(EN, 1)
  time.sleep(0.005)
  gpio.output(EN, 0)
def lcdclear():
  lcdcmd(0x01)
 
def lcdprint(Str):
  l=0;
  l=len(Str)
  for i in range(l):
    lcdwrite(ord(Str[i]))
    
def setCursor(x,y):
    if y == 0:
        n=128+x
    elif y == 1:
        n=192+x
    lcdcmd(n)

def enrollFinger():
    lcdcmd(1)
    lcdprint("Enrolling Finger")
    time.sleep(2)
    print('Waiting for finger...')
    lcdcmd(1)
    lcdprint("Place Finger")
    while ( f.readImage() == False ):
        pass
    f.convertImage(0x01)
    result = f.searchTemplate()
    positionNumber = result[0]
    if ( positionNumber >= 0 ):
        print('Template already exists at position #' + str(positionNumber))
        lcdcmd(1)
        lcdprint("Finger ALready")
        lcdcmd(192)
        lcdprint("   Exists     ")
        time.sleep(2)
        return
    print('Remove finger...')
    lcdcmd(1)
    lcdprint("Remove Finger")
    time.sleep(2)
    print('Waiting for same finger again...')
    lcdcmd(1)
    lcdprint("Place Finger")
    lcdcmd(192)
    lcdprint("   Again    ")
    while ( f.readImage() == False ):
        pass
    f.convertImage(0x02)
    if ( f.compareCharacteristics() == 0 ):
        print("Fingers do not match")
        lcdcmd(1)
        lcdprint("Finger Did not")
        lcdcmd(192)
        lcdprint("   Mactched   ")
        time.sleep(2)
        return
    f.createTemplate()
    positionNumber = f.storeTemplate()
    print('Finger enrolled successfully!')
    lcdcmd(1)
    lcdprint("registration id:")
    lcdcmd(192)
    lcdprint(str(pos[positionNumber]))
   # lcdprint("successfully")
    print('New template position #' + str(positionNumber))
    time.sleep(2)

def searchFinger():
    global d
##    try:
    if d==0:
        print('Waiting for finger...')
        while( f.readImage() == False ):
            #pass
            time.sleep(.5)
            return
        f.convertImage(0x01)
        result = f.searchTemplate()
        positionNumber = result[0]
        accuracyScore = result[1]
        if positionNumber == -1 :
            print('No match found!')
            lcdcmd(1)
            lcdprint("No Match Found")
            time.sleep(2)
            return
        else:
            print('Found template at position #' + str(positionNumber))
            lcdcmd(1)
            lcdprint("Authorized voter")
            #lcdprint(str(positionNumber))
            s=positionNumber
            try:
                if a.index(s)>=0:
                    print("Found!")
                    lcdcmd(192)
                    lcdprint("Already voted")
                    gpio.output(buzz, gpio.HIGH)
                    time.sleep(5)
                    gpio.output(buzz, gpio.LOW)
                    d=0
            except Exception as e:
                print("Not found!")
                print('Exception message:'+str(e))
                a.append(positionNumber)
                print(a)
                h=pos[positionNumber]
                vote='http://embsmartevm.dbandroid.online/save_values.php?'+'user_id='+str(h)
                http=urllib3.PoolManager()
                resp=http.request('GET',vote)
                print(resp.status)
                print(vote)
                print("sent")
                d=1            
                time.sleep(2)
def vote():
    global d,l,y,k
    if d==1:
        lcdcmd(1)
        lcdprint("press party")
        lcdcmd(192)
        lcdprint("switch to vote")
        if gpio.input(party1)==0:
                p=1
                l=l+1
                print(l)
                vote='http://embsmartevm.dbandroid.online/save_values.php?'+'party_id='+str(p)
                http=urllib3.PoolManager()
                resp=http.request('GET',vote)
                print(resp.status)
                print(vote)
                print("sent")
                d=0
        elif gpio.input(party2)==0:
                p=2
                y=y+1
                print(y)
                vote='http://embsmartevm.dbandroid.online/save_values.php?'+'party_id='+str(p)
                http=urllib3.PoolManager()
                resp=http.request('GET',vote)
                print(resp.status)
                print(vote)
                print("sent")
                d=0
        elif gpio.input(party3)==0:
                p=3
                k=k+1
                print(k)
                vote='http://embsmartevm.dbandroid.online/save_values.php?'+'party_id='+str(p)
                http=urllib3.PoolManager()
                resp=http.request('GET',vote)
                print(resp.status)
                print(vote)
                print("sent")
                d=0
##    except Exception as e:
##        print('Operation failed!')
##        print('Exception message: ' + str(e))
##        exit(1)
    
def deleteFinger():
    positionNumber = 0
    count=0
    lcdcmd(1)
    lcdprint("Delete Finger")
    lcdcmd(192)
    lcdprint("Position: ")
    lcdcmd(0xca)
    lcdprint(str(count))
    while gpio.input(enrol) == True:   # here enrol key means ok
        if gpio.input(inc) == False:
            count=count+1
            if count>1000:
                count=1000
            lcdcmd(0xca)
            lcdprint(str(count))
            time.sleep(0.2)
        elif gpio.input(dec) == False:
            count=count-1
            if count<0:
                count=0
            lcdcmd(0xca)
            lcdprint(str(count))
            time.sleep(0.2)
    positionNumber=count
    if f.deleteTemplate(positionNumber) == True :
        print('Template deleted!')
        lcdcmd(1)
        lcdprint("Finger Deleted");
        time.sleep(2)

begin()
lcdcmd(0x01)
lcdprint("FingerPrint ")
lcdcmd(0xc0)
lcdprint("based ")
time.sleep(3)
lcdcmd(0x01)
lcdprint("voting")
lcdcmd(0xc0)
lcdprint("system  ")
time.sleep(3)
flag=0
lcdclear()

while True:
    if d==0:
    #gpio.output(led, HIGH)
        lcdcmd(1)
        lcdprint("Press switch")
        lcdcmd(192)
        lcdprint("for voting")
        #time.sleep(5)
        if gpio.input(enrol) == 0:
            #gpio.output(led, LOW)
            enrollFinger()
        elif gpio.input(delet) == 0:
            #gpio.output(led, LOW)
            while gpio.input(delet) == 0:
                time.sleep(0.1)
                deleteFinger()
        elif gpio.input(iden)==0:
            searchFinger()
    elif d==1:
        vote()
