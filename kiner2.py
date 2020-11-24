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
import RPi.GPIO as GPIO
#import time
LCD_RS=27
LCD_E=22
LCD_D4=6
LCD_D5=13
LCD_D6=19
LCD_D7=26

LCD_WIDTH=16
LCD_CHR= True
LCD_CMD= False

LCD_LINE_1 = 0x80
LCD_LINE_2 = 0xc0

E_PULSE = 0.001
E_DELAY = 0.001


    #GPIO.setup(ir,GPIO.IN,pull_up_down=GPIO.PUD_UP)
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
lcd_init()


##
##lbl = tk.Label(window, text = "No.", 
##width = 20, height = 2, fg ="green", 
##bg = "white", font = ('times', 15, ' bold ') ) 
##lbl.place(x = 400, y = 200) 

##txt = tk.Entry(window, 
##width = 20, bg ="white", 
##fg ="green", font = ('times', 15, ' bold ')) 
##txt.place(x = 700, y = 215) 

##lbl2 = tk.Label(window, text ="Name", 
##width = 20, fg ="green", bg ="white", 
##height = 2, font =('times', 15, ' bold ')) 
##lbl2.place(x = 400, y = 300) 
##
##txt2 = tk.Entry(window, width = 20, 
##bg ="white", fg ="green", 
##font = ('times', 15, ' bold ') ) 
##txt2.place(x = 700, y = 315)
##def party1():
##    
##        bjp=ImageTk.PhotoImage(Image.open("/home/pi/Desktop/evm/tdp.png"))
##        bjp_label=Label(image=bjp)
##        bjp_label.pack()
        # Both ID and Name is used for recognising the Image 
##        Id =(txt.get()) 
##        name =(txt2.get()) 
##        
##        # Checking if the ID is numeric and name is Alphabetical 
##        if(is_number(Id) and name.isalpha()): 
##                # Opening the primary camera if you want to access 
##                # the secondary camera you can mention the number 
##                # as 1 inside the parenthesis 
##                cam = cv2.VideoCapture(0) 
##                # Specifying the path to haarcascade file 
##                harcascadePath = "data/haarcascade_frontalface_default.xml"
##                # Creating the classier based on the haarcascade file. 
##                detector = cv2.CascadeClassifier(harcascadePath) 
##                # Initializing the sample number(No. of images) as 0 
##                sampleNum = 0
##                while(True): 
##                        # Reading the video captures by camera frame by frame 
##                        ret, img = cam.read()
##                        print('cam_1',ret)
##                        # Converting the image into grayscale as most of 
##                        # the the processing is done in gray scale format 
##                        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
##                        
##                        # It converts the images in different sizes 
##                        # (decreases by 1.3 times) and 5 specifies the 
##                        # number of times scaling happens 
##                        faces = detector.detectMultiScale(gray, 1.3, 5) 
##                        
##                        # For creating a rectangle around the image 
##                        for (x, y, w, h) in faces: 
##                                # Specifying the coordinates of the image as well 
##                                # as color and thickness of the rectangle.       
##                                # incrementing sample number for each image 
##                                cv2.rectangle(img, (x, y), ( 
##                                        x + w, y + h), (255, 0, 0), 2) 
##                                sampleNum = sampleNum + 1
##                                # saving the captured face in the dataset folder 
##                                # TrainingImage as the image needs to be trained 
##                                # are saved in this folder 
##                                cv2.imwrite( 
##                                        "TrainingImage/"+name +"."+Id +'.'+ str( 
##                                                sampleNum) + ".jpg", gray[y:y + h, x:x + w]) 
##                                # display the frame that has been captured 
##                                # and drawn rectangle around it. 
##                        cv2.imshow('frame', img) 
##                        # wait for 100 miliseconds 
##                        if cv2.waitKey(100) & 0xFF == ord('q'): 
##                                break
##                        # break if the sample number is more than 60 
##                        elif sampleNum>60: 
##                                break
##                # releasing the resources 
##                cam.release() 
##                # closing all the windows 
##                cv2.destroyAllWindows() 
##                # Displaying message for the user 
##                res = "Images Saved for ID : " + Id +" Name : "+ name 
##                # Creating the entry for the user in a csv file 
##                row = [Id, name] 
##                with open(r'UserDetails/UserDetails.csv', 'a+') as csvFile: 
##                        writer = csv.writer(csvFile) 
##                        # Entry of the row in csv file 
##                        writer.writerow(row) 
##                csvFile.close() 
##                message.configure(text = res) 
##        else: 
##                if(is_number(Id)): 
##                        res = "Enter Alphabetical Name"
##                        message.configure(text = res) 
##                if(name.isalpha()): 
##                        res = "Enter Numeric Id"
##                        message.configure(text = res)
        #return 0
#def party2(): 
##        # Local Binary Pattern Histogram is an Face Recognizer 
##        # algorithm inside OpenCV module used for training the image dataset 
##        recognizer = cv2.face.LBPHFaceRecognizer_create() 
##        # Specifying the path for HaarCascade file 
##        harcascadePath = "data/haarcascade_frontalface_default.xml"
##        # creating detector for faces 
##        detector = cv2.CascadeClassifier(harcascadePath) 
##        # Saving the detected faces in variables 
##        faces, Id = getImagesAndLabels("TrainingImage")
##        print(Id)
##        # Saving the trained faces and their respective ID's 
##        # in a model named as "trainner.yml". 
##        recognizer.train(faces, np.array(Id))    
##        recognizer.save("TrainingImageLabel/Trainner.yml") 
##        # Displaying the message 
##        res = "Image Trained"
##        message.configure(text = res)
  #  return 0

#def party3(): 
##        # get the path of all the files in the folder 
##        imagePaths =[os.path.join(path, f) for f in os.listdir(path)] 
##        faces =[] 
##        # creating empty ID list 
##        Ids =[] 
##        # now looping through all the image paths and loading the 
##        # Ids and the images saved in the folder 
##        for imagePath in imagePaths: 
##                # loading the image and converting it to gray scale 
##                pilImage = Image.open(imagePath).convert('L') 
##                # Now we are converting the PIL image into numpy array 
##                imageNp = np.array(pilImage, 'uint8') 
##                # getting the Id from the image 
##                Id = int(os.path.split(imagePath)[-1].split(".")[1]) 
##                # extract the face from the training image sample 
##                faces.append(imageNp) 
##                Ids.append(Id)           
##        return faces, Ids
   # return 0
# For testing phase 
#def party4():
##        col_names =  ['Id','Name']
##        attendance = pd.DataFrame(columns = col_names)
##        recognizer = cv2.face.LBPHFaceRecognizer_create() 
##        # Reading the trained model 
##        recognizer.read("TrainingImageLabel/Trainner.yml") 
##        harcascadePath = "data/haarcascade_frontalface_default.xml"
##        faceCascade = cv2.CascadeClassifier(harcascadePath) 
##        # getting the name from "userdetails.csv" 
##        df = pd.read_csv(r"UserDetails/UserDetails.csv") 
##        cam = cv2.VideoCapture(0) 
##        font = cv2.FONT_HERSHEY_SIMPLEX
    #return 0
#def chips():

while True:
    window = tk.Tk() 
    window.title("ELECTIONS") 
    window.configure(background ='white') 
    window.grid_rowconfigure(0, weight = 1) 
    window.grid_columnconfigure(0, weight = 1) 
    message = tk.Label( 
        window, text ="PARTY", 
        bg ="white", fg = "black",# width = 50, 
       # height = 3,
        font = ('times', 30, 'bold')) 
        
    message.place(x = 650, y = 0)
    tdp=Image.open("/home/pi/Desktop/evm/tdp.png")
    resize_tdp=tdp.resize((200,200),Image.ANTIALIAS)
    tdp_new=ImageTk.PhotoImage(resize_tdp)
    tdp_label=Label(image=tdp_new)#,height=300,width=500)
    tdp_label.pack(pady=20)
    tdp_label.place(x=1100,y=100)
    ##
    bjp=Image.open("/home/pi/Desktop/evm/BJPI.jpg")
    resize_bjp=bjp.resize((200,200),Image.ANTIALIAS)
    bjp_new=ImageTk.PhotoImage(resize_bjp)
    bjp_label=Label(image=bjp_new)#,height=300,width=500)
    bjp_label.pack(pady=20)
    bjp_label.place(x=365,y=100)
    ##
    cong=Image.open("/home/pi/Desktop/evm/congress.jpg")
    resize_cong=cong.resize((200,200),Image.ANTIALIAS)
    cong_new=ImageTk.PhotoImage(resize_cong)
    cong_label=Label(image=cong_new)#,height=300,width=500)
    cong_label.pack(pady=20)
    cong_label.place(x=855,y=100)
    ##
    ycp=Image.open("/home/pi/Desktop/evm/ycp.jpeg")
    resize_ycp=ycp.resize((200,200),Image.ANTIALIAS)
    ycp_new=ImageTk.PhotoImage(resize_ycp)
    ycp_label=Label(image=ycp_new)#,height=300,width=500)
    ycp_label.pack(pady=20)
    ycp_label.place(x=600,y=95)

    o0=Image.open("/home/pi/Desktop/evm/teapot.jpeg")
    resize_o0=o0.resize((200,200),Image.ANTIALIAS)
    o0_new=ImageTk.PhotoImage(resize_o0)
    o0_label=Label(image=o0_new)#,height=300,width=500)
    o0_label.pack(pady=20)
    o0_label.place(x=110,y=95)

    o5=Image.open("/home/pi/Desktop/evm/match.jpg")
    resize_o5=o5.resize((200,200),Image.ANTIALIAS)
    o5_new=ImageTk.PhotoImage(resize_o5)
    o5_label=Label(image=o5_new)#,height=300,width=500)
    o5_label.pack(pady=20)
    o5_label.place(x=110,y=385)

    o6=Image.open("/home/pi/Desktop/evm/mug.png")
    resize_o6=o6.resize((200,200),Image.ANTIALIAS)
    o6_new=ImageTk.PhotoImage(resize_o6)
    o6_label=Label(image=o6_new)#,height=300,width=500)
    o6_label.pack(pady=20)
    o6_label.place(x=370,y=385)

    o7=Image.open("/home/pi/Desktop/evm/mango.png")
    resize_o7=o7.resize((200,200),Image.ANTIALIAS)
    o7_new=ImageTk.PhotoImage(resize_o7)
    o7_label=Label(image=o7_new)#,height=300,width=500)
    o7_label.pack(pady=20)
    o7_label.place(x=600,y=385)

    o8=Image.open("/home/pi/Desktop/evm/tail.jpg")
    resize_o8=o8.resize((200,200),Image.ANTIALIAS)
    o8_new=ImageTk.PhotoImage(resize_o8)
    o8_label=Label(image=o8_new)#,height=300,width=500)
    o8_label.pack(pady=20)
    o8_label.place(x=860,y=385)

    o9=Image.open("/home/pi/Desktop/evm/teapot.jpeg")
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
    quitWindow = tk.Button(window, text ="Quit", 
    command = window.destroy, fg ="white", bg ="green", 
    width = 20, height = 3, activebackground = "Red", 
    font =('times', 15, ' bold ')) 
    quitWindow.place(x = 0, y = 0)
    #lcd_string("Hello",LCD_LINE_1)
    #time.sleep(5)
    #lcd_string("WORKING...",LCD_LINE_1)
##quitWindow = tk.Button(window, text ="Quit", 
##command = window.destroy, fg ="white", bg ="green", 
##width = 20, height = 3, activebackground = "Red", 
##font =('times', 15, ' bold ')) 
##quitWindow.place(x = 1100, y = 500) 
    window.mainloop()
##while True:
    
    #time.sleep(10)
   # chips()
