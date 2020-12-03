from array import *
a=array('i', [-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12])
n=int(input("Enter the length of the array: "))
while True:
    for i in range(n):
        x=int(input("Enter a value: "))
        a.append(x)
        print(a)
        k=25
        s=int(input("Enter the number to be searched: "))
        c=0
        try:
        #for j in range(k):
            if a.index(s)>=0:
                    print("FOUND!")
                    c+= 1
                #break
        except Exception as e:
            print("Not found")
            print('Exception message:'+str(e))
            #exit(1)
##        if(c!=1):
##            print("NOT FOUND!")
