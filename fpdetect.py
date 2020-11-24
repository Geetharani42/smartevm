import os.path
import time
#import urllib3
#import RPi.GPIO as GPIO
#from keypad import keypad
from pyfingerprint.pyfingerprint import PyFingerprint
#import digitalio
#import board
#from sim800l import SIM800L
from random import *
#import adafruit_character_lcd.character_lcd as characterlcd
import os


##lcd_columns = 16
##lcd_rows = 2
##
##lcd_rs = digitalio.DigitalInOut(board.D7)
##lcd_en = digitalio.DigitalInOut(board.D8)
##lcd_d4 = digitalio.DigitalInOut(board.D25)
##lcd_d5 = digitalio.DigitalInOut(board.D11)
##lcd_d6 = digitalio.DigitalInOut(board.D9)
##lcd_d7 = digitalio.DigitalInOut(board.D10)
##
##lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6,
##                                      lcd_d7, lcd_columns, lcd_rows)
##
##
##lcd.clear()
##lcd_line_1 = '  WELCOME TO\n'
##lcd_line_2 = 'ATM USING FP'
##lcd.message = lcd_line_1 + lcd_line_2
##time.sleep(2)
try:
    f = PyFingerprint('/dev/ttyAMA0', 57600, 0xFFFFFFFF, 0x00000000)

    if ( f.verifyPassword() == False ):
        raise ValueError('The given fingerprint sensor password is wrong!')

except Exception as e:
    print('The fingerprint sensor could not be initialized!')
    print('Exception message: ' + str(e))
    #exit(1)


##sim800l=SIM800L('/dev/serial0')
##GPIO.setwarnings(False)
##GPIO.setmode(GPIO.BCM)
##GPIO.setup(17 , GPIO.OUT)
##GPIO.setup(27 , GPIO.OUT)
##GPIO.output(17,False)
##GPIO.output(27,False)
##time.sleep(0.5)
##if __name__ == '__main__':
##    # Initialize
##    kp = keypad(columnCount = 3)
##    
while True:
            print('Waiting for finger...')
##            lcd.clear()
##            lcd_line_1 = 'WELCOME TO ATM\n'
##            lcd_line_2 = 'SCAN YOUR FINGER'
##            lcd.message = lcd_line_1 + lcd_line_2
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

            if ( positionNumber == -1 ):
                        print('No match found!')
##                        lcd.clear()
##                        lcd_line_1 = 'No match found!\n'
##                        lcd_line_2 = 'Try again....'
##                        lcd.message = lcd_line_1 + lcd_line_2
                        time.sleep(2)
                        #os.execv(sys.executable, ['python'] + sys.argv)        
            else:
                        print('Found template at position #' + str(positionNumber))
##                        lcd.clear()
##                        lcd_line_1 = 'ID FOUND:'+str(positionNumber)+' \n'
##                        lcd_line_2 = 'Genrating OTP'
##                        lcd.message = lcd_line_1 + lcd_line_2
##                        time.sleep(2)
                        print('The accuracy score is: ' + str(accuracyScore))
                        os.system('python /home/pi/open.py')

            positionNumber1=positionNumber
            
            
                                            
##            if(positionNumber1 >=0):
##                    print('data uploding to server')
##                    lcd.clear()
##                    lcd_line_1 = 'OTP Sent to \n'
##                    lcd_line_2 = 'register mobile'
##                    lcd.message = lcd_line_1 + lcd_line_2
##                    time.sleep(2)
##                    value = randint(1000, 9999)
##                    print('OTP for Your ATM:',int(value))
##                    sms="OTP for Your ATM:" + str(value)
##                    dest="7780775887"
##                    sim800l.send_sms(dest,sms)
##                    time.sleep(2)
##                    otp_k=int(value)
##                    print('enter OTP')
##                    lcd.clear()
##                    lcd_line_1 = 'Enter OTP \n'
##                    lcd_line_2 = ''
##                    lcd.message = lcd_line_1 + lcd_line_2
##                    time.sleep(2)
##                    seq = []
##                    for i in range(4):
##                                        digit = None
##                                        while digit == None:
##                                            digit = kp.getKey()
##                                        seq.append(digit)
##                                        print(seq)
##                                        otp_i = ''.join(str(e) for e in seq)
##                                        lcd_line_2 = str(otp_i)
##                                        lcd.message = lcd_line_1 + lcd_line_2
##                                        time.sleep(0.4)
##                                        
##                    
##                    print(otp_i)
##                    lcd.clear()
##                    lcd_line_1 = 'Enter OTP \n'
##                    lcd_line_2 = str(otp_i)
##                    lcd.message = lcd_line_1 + lcd_line_2
##                    time.sleep(2)
##                    if int(otp_k) == int(otp_i):
##                                print ("Valid OTP")
##                                lcd.clear()
##                                lcd_line_1 = 'VALID OTP \n'
##                                lcd_line_2 = 'Thank You'
##                                lcd.message = lcd_line_1 + lcd_line_2
##                                time.sleep(2)
##                                
##                    else:
##                            print("Invalid OTP")
##                            GPIO.output(17,True)
##                            GPIO.output(27,True)
##                            time.sleep(2)
##                            lcd.clear()
##                            lcd_line_1 = 'INVALID OTP \n'
##                            lcd_line_2 = 'Sending Alert'
##                            lcd.message = lcd_line_1 + lcd_line_2
##                            time.sleep(1)
##                            sms="INVALID OTP enterd for Your ATM card"
##                            dest="7780775887"
##                            sim800l.send_sms(dest,sms)
##                            print("MSG sent:")
##                            lcd.clear()
##                            lcd_line_1 = 'Msg alert sent \n'
##                            lcd_line_2 = 'Sucessfully!'
##                            lcd.message = lcd_line_1 + lcd_line_2
##                            time.sleep(2)
##                            GPIO.output(17,False)
##                            GPIO.output(27,False)
##                            time.sleep(0.5)

            
