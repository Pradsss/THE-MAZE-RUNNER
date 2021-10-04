from tkinter import *
import random
root=Tk()

from PIL import Image,ImageTk
img = Image.open("C:\\Users\\Pradipti\\Pictures\\Saved Pictures\\scifi.jpg")
photoimage = ImageTk.PhotoImage(img)
label=Label(root,image=photoimage)
label.place(x=0,y=-1000)
root.geometry("100x100")
root.title("registration")
label1=Label(root,text="SIGN UP FOR THE UNBEATABLE QUESTS!!!!AND PROVE WHO U R!!!:)",font=("segeo script",20,"bold"),relief=SUNKEN,fg="white",bg="black")
label1.pack(fill=BOTH,padx=3,pady=3)
l2=Label(root,text="YOU ARE CALLED AS:)",font=("segeo script",20,"bold"),fg="white",relief=SUNKEN,bg="red")
l3=Label(root,text="EMAIL-ID:)",font=("segeo script",20,"bold"),fg="white",relief=SUNKEN,bg="red")
l4=Label(root,text="HOW OLD ARE YOU:)",font=("segeo script",20,"bold"),fg="white",relief=SUNKEN,bg="red")
R1=StringVar()
R2=StringVar()
l5=Label(root,text="GENDER M/F:)",font=("segeo script",20,"bold"),fg="white",relief=SUNKEN,bg="red")
l6=Label(root,text="DATE(YYYY-MM-DD):)",font=("segeo script",20,"bold"),fg="white",relief=SUNKEN,bg="red")


l2.place(x=100,y=100)
l3.place(x=100,y=150)
l4.place(x=100,y=200)
l5.place(x=100,y=250)
l6.place(x=100,y=300)

n=StringVar()
e=StringVar()
a=StringVar()
d=StringVar()
g=StringVar()
e1=Entry(root,textvar=n,font=("comic sans ms",20),fg="blue")
e1.place(x=600,y=100)
e2=Entry(root,textvar=e,font=("comic sans ms",20),fg="red")
e2.place(x=600,y=150)
e3=Entry(root,textvar=a,font=("comic sans ms",20),fg="green")
e3.place(x=600,y=200)
e4=Entry(root,textvar=g,font=("comic sans ms",20),fg="black")
e4.place(x=600,y=250)
e5=Entry(root,textvar=d,font=("comic sans ms",20),fg="black")
e5.place(x=600,y=300)
email=e.get()#global

def write():
    import tkinter.messagebox as msg
    f1=open("THE BATTLESS.txt","w")
    f1.write("name:"+n.get()+" "+"emailid:"+str(e.get())+" "+"age:"+str(a.get())+" "+"date:"+str(d.get())+" ")
    f1.flush()
    f1.close()
    f2=open("THE BATTLESS.txt","r")
    l=f2.readlines()
    msg.showinfo("","GO TO THE PYTHON SHELL")
    for i in l:
        msg.showinfo("YOU IDENTIFY URSELF AS:))","{}".format(i))
    msg.showinfo("YOUR EMAIL IS","{}".format(e.get()))
    msg.showinfo("HEYYY!!!!","YOUR ID IS THE ONLY TREASURE YOU POSSESS *_* ")
    f2.close()
    return(n.get(),str(e.get()),str(a.get()),str(d.get()))
    


#details function removed    
                                                                                                                              
def inst():
    win=Toplevel()
    from PIL import Image,ImageTk
    img = Image.open("C:\\Users\\Pradipti\\Pictures\\Saved Pictures\\warriors.jpg")
    photoimage = ImageTk.PhotoImage(img)
    l=Label(win,image=photoimage)
    l.place(x=0,y=-100)
    win.geometry("250x250")
    win.title("WELCOME TO MAZE RUNNER!!!")
    label=Label(win,text='--> Maze Runner is an app where your gaming skills will be put to test.',relief="solid",font=("segeo script",14,"bold"),bg="yellow")
    l1=Label(win,text='--> To start off, there are 5 games and a total of 15 minutes to complete all of them.',relief="solid",font=("segeo script",14,"bold"),bg="yellow")
    l2=Label(win,text='--> The games in this app along with the time allotted are as follows:',relief="solid",font=("segeo script",14,"bold"),bg="yellow")
    l3=Label(win,text=' 1. Bingo, 2mins',relief="solid",font=("segeo script",14,"bold"),bg="yellow")
    l4=Label(win,text=' 2. Jumbled words, 2mins',relief="solid",font=("segeo script",14,"bold"),bg="yellow" )
    l5=Label(win,text=' 3. Hangman, 2mins',relief="solid",font=("segeo script",14,"bold"),bg="yellow" )
    l6=Label(win,text=' 4. Box, 5mins', relief="solid",font=("segeo script",14,"bold"),bg="yellow")
    l7=Label(win,text=' 5. Fireball, 4mins',relief="solid",font=("segeo script",14,"bold"),bg="yellow")
    l8=Label(win,text='--> After completing all the games a statistical view of your performance is shown.',relief="solid",font=("segeo script",14,"bold"),bg="yellow" )
    l9=Label(win,text='--> If the game is not completed within 15 mintues, 20 points will be deducted.',relief="solid",font=("segeo script",14,"bold"),bg="yellow" )
    l10=Label(win,text='--> Your time will start as soon as you start the first game.',relief="solid",font=("segeo script",14,"bold"),bg="yellow" )
    l11=Label(win,text='--> Good luck! Challenge everything!',relief="solid",font=("segeo script",14,"bold"),bg="yellow" )
    label.place(x=100,y=100)
    l1.place(x=100,y=150)
    l2.place(x=100,y=200)
    l3.place(x=100,y=250)
    l4.place(x=100,y=300)
    l5.place(x=100,y=350)
    l6.place(x=100,y=400)
    l7.place(x=100,y=450)
    l8.place(x=100,y=500)
    l9.place(x=100,y=550)
    l10.place(x=100,y=600)
    l11.place(x=100,y=650)

    
def exitt():
    exit()
def submit():
    import tkinter.messagebox as msg
    msg.showinfo("WELCOME TO THE MAZE","THE HOURGLASS HAS IT'S SAND RUNNING AND STRATEGIES ARE DEPLETING .....SO BE BRAVE!!")
    name=n.get()
    age=a.get()
    email=e.get()
    gen=g.get()
    write()
   
    f1=open("THE BATTLESS.txt","r")
    b=f1.read()

    if "@" not in email and ".com" not in email:#checking email
        msg.showinfo("","{} PLEASE ENTER A VALID EMAIL ID.Eg:John@xyz.com".format(name))
    if email in b:
        msg.showinfo("","YOU HAVE ALREADY REGISRERED!!!DONOT REGISTER AGAIN".format(name))
    
    if int(age)>10:
        msg.showinfo("","{} U R ELIGIBLE TO FIGHT UR OWN WAY OUT".format(name))
        
    else:
        msg.showinfo(name,"U R STILL A LONG WAY TO GROW UP PLEASE EXIT...U R NOT ELIGIBLE")
    if gen not in ["M","F","m","f"]:
        msg.showinfo("","{} PLEASE ENTER A VALID GENDER M/F".format(name))
    
#instruction button    
menu=Menu(root)
root.config(menu=menu)
submenu=Menu(menu)
menu.add_cascade(label="THE DOOR",menu=submenu)
submenu.add_command(label="EXIT",command=exitt)
submenu2=Menu(menu)
menu.add_cascade(label="THE SKILLS TO PLAY",menu=submenu2)
submenu2.add_command(label="INSTRUCTIONS",command=inst)    
    
    

def db(): 
    name1=n.get()
    email1=e.get()
    age1=a.get()
    date1=d.get()
    gender=g.get()
    b=""
    f=""
    h=""
    j=""
    import mysql.connector as sqltor
    con=sqltor.connect(host="localhost",user="root",passwd="T!$51h#86B7",database="MR")
    cursor=con.cursor()
    st="insert into mrds(name,emailid,age,gender,Date,bingo,fire,hang,jumb)values('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(name1,email1,age1,gender,date1,b,f,h,j)
    cursor.execute(st)
    con.commit()
    
    
def graphh():
    import mysql.connector as sqltor
    import datetime
    con=sqltor.connect(host="localhost",user="root",passwd="T!$51h#86B7",database="MR")
    cursor=con.cursor()
    s=[]
    email=e.get()
    st="select * from mrds where emailid='{}'".format(email)
    cursor.execute(st)
    data=cursor.fetchall()
    for row in data:
        for i in row:
            s.append(i)
        
    con.close()
    k=[]
    for i in range(5,9):
        
        k.append(s[i])
    

    b=k[0]
    f=k[1]
    h=k[2]
    j=k[3]

    l1=b.split()
    B=l1[0]
    l2=f.split()
    F=l2[0]
    l3=h.split()
    H=l3[0]
    l4=j.split()
    J=l4[0]
    print(B)
    print(F)
    print(H)
    print(J)
    import numpy as np
    import matplotlib.pyplot as plt
    x=np.arange(4)
    sc=[[50,50,20,20],[B,F,H,J]]
    
    plt.plot(x,sc[1],color='r',label="your score")
    plt.legend(loc="upper left")
    plt.title("Your score graph")
    plt.xticks(np.arange(4),("BINGO","Fireball","Hangman","Jumbled words"))
    plt.show()
   
    
    
    
    
def close_window():
    exitt()
    
    
def fire():
    import time
    t1=time.time()

    def fireballg():
        
        ######################################################################
        # Trajectory formula
        # y=x*tan(a) - g*x*x/(2*v*v*cos(a)*cos(a))
        # where
        # y is vertical position (m)
        # x is horizontal position (m)
        # g is gravitional constant (9.8 m/s/s)
        # v is initial velocity [combined component](m/s)
        # a is the angle of initial velocity from horizontal plane (in radian)
        #
        # Maximum distance at horizontal plane:
        # at y=0
        # x=2*v*v*cos(a)*cos(a)*tan(a)/g
        # i.e x=2*v*v*cos(a)*sin(a)/g
        # This program will randomly position the target.
        # A fire ball will be thrown with initial velocity and angle as input
        # If the fire ball hits the target the score will be increased and the
        # target position will be randomly changed
        #
        # - By Pradipti Mondal, Class XI
        ########################################################################

        import random
        import math
        

        curScore=0
        prevScore=0
        b=[]
        c=[]
        minTargetRange=100
        maxTargetRange=255
        randomTarget1=5
        randomTarget2=maxTargetRange-minTargetRange
        target=250
        step=5
        stepTargetLabel=50
        g=9.8 #gravitational constant
        v=0 #velocity
        angleDegree=0 #angle in degree
        a=0 #angle in radian
        d=0 # computed target based on input velocity and angle
        dmax=0

        def setTarget(minTargetRange,randomTarget1,randomTarget2,step):
            target=minTargetRange+random.randint(randomTarget1,randomTarget2)
            j=(int)(target/step)
            
            target=j*step # set the target in steps
            return target

        def printTarget(target,step):
            print ("!!! Target:[",target-step,"-",target+step,"] metre!!!")

        def printTargetLine(step,target,maxTargetRange,stepTargetLabel):
            print ("o",end="")
            for i in range (step,target-step,step):
                print (" ",end="")
            print ("o",end="")
            print()
            print ("|",end="")
            for i in range (step,target-step,step):
                if(i%stepTargetLabel == 0):
                    print ("|",end="")
                else:
                    print ("-",end="")
            print ("|",end="")
            
            for i in range (target+step,maxTargetRange,step):
                if(i%stepTargetLabel == 0):
                    print ("|",end="")
                else:
                    print ("-",end="")
            print()
            print (" ",end="")
            j=0
            k=0
            for i in range (step,maxTargetRange,step):
                if(i%stepTargetLabel == 0):
                    print (i,end="")
                    k=(int)(i/stepTargetLabel)
                    if k>=2:
                        j=j+2
                    else:
                        j=j+1
                else:
                    if (j>0):
                        j=j-1
                    else:
                        print (" ",end="")
            print()
            print()

        def getVelocity():
            
            while (True):
                v = int (input ("Velocity [0-50] m/s: "))
                if (v <0) or (v>50):
                    print ("Wrong input !!!")
                else:
                    break
            return v
        def getAngle():
            while(True):
                angleDegree = int (input ("Angle degree [0-90]: "))
                if (angleDegree <0) or (angleDegree>90):
                    print ("Wrong input !!!")
                else:
                    break
            a=angleDegree*22/(7*180) # angle in radian
            return a 

        def computeTarget(a,v,g):
            d=(int)(2*v*v*math.cos(a)*math.sin(a)/g) # achieved target
            return d

        def computeMaxRange(v,g):
            dmax=(int)(v*v/g) #Maximum distance at angle = 45 degree
            return dmax

        def printTrajectory(step,d,a):
            b[:]=[]
            c[:]=[]
            max=0
            for x in range (step,d,step):
                y=x*math.tan(a) - g*x*x/(2*v*v*math.cos(a)*math.cos(a))
                z=(int)(y)
                b.append(z) # Y-axis data in a list
                c.append(x) # X-axis data in a list
                if (z>max):
                    max=z
            #print (b)
            #print (c)
            for i in range (max,0,-1):
                prev=c[0]
                for j in range (0,len(b),1):
                    if (b[j] == i):
                        space=(int)((c[j]-prev)/step)
                        print (" "*space,end="")
                        print ("*",end="")
                        prev=c[j]
                print()

        def printResult(curScore,step,d,target):

            if ((d >= target-step)and(d <= target+step)):
                curScore+=50
                
                print("You have hit the target at distance = !!!",d)
                
            else:
                print("Reached distance of ",d," !!! You have missed the target [",target-step,"-",target+step,"]!!!")
            print("Your score = ",curScore)
            return curScore


        target=setTarget(minTargetRange,randomTarget1,randomTarget2,step)    
        

        while(True):
            if curScore != prevScore:
                # Change the target position only if the target is hit
                target=setTarget(minTargetRange,randomTarget1,randomTarget2,step)
                prevScore=curScore
            
            printTargetLine(step,target,maxTargetRange,stepTargetLabel)
            printTarget(target,step)
            
            v=getVelocity()
            a=getAngle()
            d=computeTarget(a,v,g)
            #dmax=computeMaxRange(v,g) # for debugging
            printTrajectory(step,d,a)
            printTargetLine(step,target,maxTargetRange,stepTargetLabel)
            
            curScore=printResult(curScore,step,d,target)
            key=input("Press any key to continue, 'q' to exit]: ")
            if key == 'q':
                break
            else:
                continue

        return curScore


    q=fireballg()
    t2=time.time()
    t=t2-t1
    sc=str(q)+" "+str(t)
    if t>240:
        print("you have exceeded the time limit and the time taken is:",t)
        print("20 points is deducted from your score")
        print("score=",q)
        
    else:
        print("score=",q)
        print("time taken",t)
    email1=e.get()
    import mysql.connector as sqltor
    con=sqltor.connect(host="localhost",user="root",passwd="T!$51h#86B7",database="MR")
    cursor=con.cursor()
    j="update mrds set fire=%s where emailid=%s"
    i=(sc,email1)
    cursor.execute(j,i)
    con.commit()
    
            
def jumbled():
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("WELCOME TO THE MARATHON OF SPELLINGS!!!!!")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("SPELLAMNESIA")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("ITS GOING TO BE FUN!!!")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("AN ADDICTION THAT WILL NEVER GET OVER..........................................")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print()
   
    print("PLEASE READ THE INSTRUCTIONS GIVEN BELOW")
    print("-------------------------------------------------------------------------------")
    print("* WORDS WITH PLURALS ARE NOT ACCEPTED")
    print("* WORDS ENTERED AS THE ANSWERS FOR THE JUMBLED WORDS MUST BE MEANINGFUL AND APT")
    print("* THIS QUIZ IS SUITABLE FOR THOSE WHO WANT TO ENHANCE THEIR VOCABLLARY SKILLS")
    print('''* IN THE FOLLOWING ROWS WORDS ARE JUMBLED UP ON THE LEFT HAND SIDE AND A CLUE IS GIVEN TO HELP YOU RE-ARRANGE THE WORD.''')
    print("PLEASE USE CAPITAL LETTERS OR YOUR ANSWER WILL NOT BE ACCEPTED")
    print("LAST BUT NOT THE LEAST, I WISH YOU ENJOY THIS QUIZ TO THE FULLEST")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("1. BEGGINNER(3-4 letter words)")
    print("2. INTERMEDIATE(5-6letter words)")
    print("3. ADVANCED(more than 6 letter words")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print()
    import time
    t1=time.time()
    def jumble():
        s=0
        ans1='c'

        ch=int(input("ENTER YOUR CHOICE OF LEVEL FROM ABOVE:"))
        while ans1=='c':
            
            if ch==1:
                print("LETS BEGIN!!!")
               
                print("1. DAD")
                print("enter 'c' to get a clue")
                ans1=input()
                if ans1=='c':
                    print("YOUR CLUE: IT IS A MATHEMATICAL OPERATOR")
                    str1=input("ENTER YOUR ANSWER:")
                else:
                    str1=input("ENTER YOUR ANSWER:")
                if str1=="ADD":
                    print("YOU ARE CORRECT!!")
                    s+=5
                else:
                    print("YOUR ANSWER WAS:ADD")
                    print("BETTER LUCK NEXT TIME")
                print()
                
                print("2. IDK")
                print("enter 'c' to get a clue")
                ans1=input()
                if ans1=='c':
                    print("YOUR CLUE: A CHILD")
                    str2=input("ENTER YOUR ANSWER:")
                else:
                    str2=input("ENTER YOUR ANSWER:")
                if str2=="KID":
                    print("YOU ARE CORRECT!!")
                    s+=5
                else:
                    print("YOUR ANSWER WAS:KID")
                    print("BETTER LUCK NEXT TIME")
                print()
                
                print("3. SLIT")
                print("enter 'c' to get a clue")
                ans1=input()
                if ans1=='c':
                    print("YOUR CLUE: AN INFORMATION WRITTEN IN ORDER")
                    str3=input("ENTER YOUR ANSWER:")
                else:    
                    str3=input("ENTER YOUR ANSWER:")
                if str3=="LIST":
                    print("YOU ARE CORRECT!!")
                    s+=5
                else:
                    print("YOUR ANSWER WAS:LIST")
                    print("BETTER LUCK NEXT TIME")
                print()

                print("4. LETB")
                print("enter 'c' to get a clue")
                ans1=input()
                if ans1=='c':
                    print("YOUR CLUE: A PART OF FORMAL WEAR")
                    str4=input("ENTER YOUR ANSWER:")
                else:    
                    str4=input("ENTER YOUR ANSWER:")
                if str4=="BELT":
                    print("YOU ARE CORRECT!!")
                    s+=5
                else:
                    print("YOUR ANSWER WAS:BELT")
                    print("BETTER LUCK NEXT TIME")
                print()
            
                print("5. AMY")
                print("enter 'c' to get a clue")
                ans1=input()
                if ans1=='c':
                    print("YOUR CLUE: A MONTH")
                    str5=input("ENTER YOUR ANSWER:")
                else:    
                    str5=input("ENTER YOUR ANSWER:")
                if str5=="MAY":
                    print("YOU ARE CORRECT!!")
                    s+=5
                else:
                    print("YOUR ANSWER WAS:MAY")
                    print("BETTER LUCK NEXT TIME")        
                print()
            
                print("6. LILB")
                print("enter 'c' to get a clue")
                ans1=input()
                if ans1=='c':
                    print("YOUR CLUE: A LIST WITH ITEMS AND PRICE")
                    str6=input("ENTER YOUR ANSWER:")
                else:    
                    str6=input("ENTER YOUR ANSWER:")
                if str6=="BILL":
                    print("YOU ARE CORRECT!!")
                    s+=5
                else:
                    print("YOUR ANSWER WAS:BILL")
                    print("BETTER LUCK NEXT TIME")        
                print()
            
                print("7. SUPH")
                print("enter 'c' to get a clue")
                ans1=input()
                if ans1=='c':
                    print("YOUR CLUE: ACTION OF DOOR")
                    str7=input("ENTER YOUR ANSWER:")
                else:    
                    str7=input("ENTER YOUR ANSWER:")
                    
                if str7=="PUSH":
                    print("YOU ARE CORRECT!!")
                    s+=5
                else:
                    print("YOUR ANSWER WAS:PUSH")
                    print("BETTER LUCK NEXT TIME")        
                print()
            
                print("8. SETR")
                print("enter 'c' to get a clue")
                ans1=input()
                if ans1=='c':
                    print("YOUR CLUE: ANOTHER WORD FOR STATIONARY")
                    str8=input("ENTER YOUR ANSWER:")
                else:    
                    str8=input("ENTER YOUR ANSWER:")
                if str8=="REST":
                    print("YOU ARE CORRECT!!")
                    s+=5
                else:
                    print("YOUR ANSWER WAS:REST")
                    print("BETTER LUCK NEXT TIME")        
                print()
            
                print("9. KCSO")
                print("enter 'c' to get a clue")
                ans1=input()
                if ans1=='c':
                    print("YOUR CLUE: A GARMENT WORN IN THE FOOT")
                    str9=input("ENTER YOUR ANSWER:")
                else:    
                    str9=input("ENTER YOUR ANSWER:")
                    
                if str9=="SOCK":
                    print("YOU ARE CORRECT!!")
                    s+=5
                else:
                    print("YOUR ANSWER WAS:SOCK")
                    print("BETTER LUCK NEXT TIME")        
                print()
            
                print("10. DRAW")
                print("enter 'c' to get a clue")
                ans1=input()
                if ans1=='c':
                    print("YOUR CLUE: A DIVISION OF A CITY OR TOWN")
                    str10=input("ENTER YOUR ANSWER:")
                else:    
                    str10=input("ENTER YOUR ANSWER:")
                if str10=="WARD":
                    print("YOU ARE CORRECT!!")
                    s+=5
                else:
                    print("YOUR ANSWER WAS:WARD")
                    print("BETTER LUCK NEXT TIME")        
                print()
        
                print("11. STUD")
                print("enter 'c' to get a clue")
                ans1=input()
                if ans1=='c':
                    print("YOUR CLUE: ANOTHER WORD FOR DIRT")
                    str11=input("ENTER YOUR ANSWER:")
                else:    
                    str11=input("ENTER YOUR ANSWER:")
                if str11=="DUST":
                    print("YOU ARE CORRECT!!")
                    s+=5
                else:
                    print("YOUR ANSWER WAS:DUST")
                    print("BETTER LUCK NEXT TIME")        
                print()
            
                print("12. EARH")
                print("enter 'c' to get a clue")
                ans1=input()
                if ans1=='c':
                    print("YOUR CLUE: EXAMINE OR HEAR")
                    str12=input("ENTER YOUR ANSWER:")
                else:    
                    str12=input("ENTER YOUR ANSWER:")
                if str12=="HEAR":
                    print("YOU ARE CORRECT!!")
                    s+=5
                else:
                    print("YOUR ANSWER WAS:HEAR")
                    print("BETTER LUCK NEXT TIME")        
                    print()
                print("YOU HAVE COME TO THE END OF THIS LEVEL")
                print("PLEASE CHOOSE A NEW LEVEL")
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            if ch==2:
                print("1. GRANY ")
                print("enter 'c' to get a clue")
                ans1=input()
                if ans1=='c':
                    print("YOUR CLUE: TEMPER")
                    str13=input("ENTER YOUR ANSWER:")
                else:
                    str13=input("ENTER YOUR ANSWER:")
                if str13=="ANGRY":
                    print("YOU ARE CORRECT!!")
                    s+=5
                else: 
                    print("YOUR ANSWER WAS:ANGRY")
                    print("BETTER LUCK NEXT TIME")
                    print()
            
                print("2. VRABE")
                print("enter 'c' to get a clue")
                ans1=input()
                if ans1=='c':
                    print("YOUR CLUE: COURAGEOUS")
                    str14=input("ENTER YOUR ANSWER:")
                else:
                    str14=input("ENTER YOUR ANSWER:")
                if str14=="BRAVE":
                    print("YOU ARE CORRECT!!")
                    s+=5
                else:
                    print("YOUR ANSWER WAS:BRAVE")
                    print("BETTER LUCK NEXT TIME")
                    print()
            
                print("3. IDALY")
                print("enter 'c' to get a clue")
                ans1=input()
                if ans1=='c':
                    print("YOUR CLUE: EVERYDAY")
                    str15=input("ENTER YOUR ANSWER:")
                else:    
                    str15=input("ENTER YOUR ANSWER:")
                if str15=="DAILY":
                    print("YOU ARE CORRECT!!")
                    s+=5
                else:
                    print("YOUR ANSWER WAS:DAILY")
                    print("BETTER LUCK NEXT TIME")
                    print()

                print("4. GREEED")
                print("enter 'c' to get a clue")
                ans1=input()
                if ans1=='c':
                    print("YOUR CLUE: RELATED TO ANGLES")
                    str16=input("ENTER YOUR ANSWER:")
                else:    
                    str16=input("ENTER YOUR ANSWER:")
                if str16=="DEGREE":
                    print("YOU ARE CORRECT!!")
                    s+=5
                else:
                    print("YOUR ANSWER WAS:DEGREE")
                    print("BETTER LUCK NEXT TIME")
                    print()

                print("5. CAFTOR")
                print("enter 'c' to get a clue")
                ans1=input()
                if ans1=='c':
                    print("YOUR CLUE: FACTORISE")
                    str17=input("ENTER YOUR ANSWER:")
                else:    
                    str17=input("ENTER YOUR ANSWER:")
                        
                if str17=="FACTOR":
                    print("YOU ARE CORRECT!!")
                    s+=5
                else:
                    print("YOUR ANSWER WAS:FACTOR")
                    print("BETTER LUCK NEXT TIME")
                    print()

                print("6. DIMELD")
                print("enter 'c' to get a clue")
                ans1=input()
                if ans1=='c':
                    print("YOUR CLUE: CENTRE")
                    str18=input("ENTER YOUR ANSWER:")
                else:
                    str18=input("ENTER YOUR ANSWER:")
                        
                if str18=="MIDDLE":
                    print("YOU ARE CORRECT!!")
                    s+=5
                else:
                    print("YOUR ANSWER WAS:MIDDLE")
                    print("BETTER LUCK NEXT TIME")        
                    print()
            
                print("7. VERNE")
                print("enter 'c' to get a clue")
                ans1=input()
                if ans1=='c':
                    print("YOUR CLUE: CARRIER OF BLOOD")
                    str19=input("ENTER YOUR ANSWER:")
                else:    
                    str19=input("ENTER YOUR ANSWER:")
                        
                if str19=="NERVE":
                    print("YOU ARE CORRECT!!")
                    s+=5
                else:
                    print("YOUR ANSWER WAS:NERVE")
                    print("BETTER LUCK NEXT TIME")
                    print()
            
                print("8. ORATI")
                print("enter 'c' to get a clue")
                ans1=input()
                if ans1=='c':
                    print("YOUR CLUE: RATIONAL")
                    str20=input("ENTER YOUR ANSWER:")
                else:    
                    str20=input("ENTER YOUR ANSWER:")
                        
                if str20=="RATIO":
                    print("YOU ARE CORRECT!!")
                    s+=5
                else:
                    print("YOUR ANSWER WAS:RATIO")
                    print("BETTER LUCK NEXT TIME")
                    print()
            
                print("9. VESLO")
                print("enter 'c' to get a clue")
                ans1=input()
                if ans1=='c':
                    print("YOUR CLUE: FIGURE OUT")
                    str21=input("ENTER YOUR ANSWER:")
                else:    
                    str21=input("ENTER YOUR ANSWER:")
                        
                if str21=="SOLVE":
                    print("YOU ARE CORRECT!!")
                    s+=5
                else:
                    print("YOUR ANSWER WAS:SOLVE")
                    print("BETTER LUCK NEXT TIME")
                    print()
            
                print("10. COKTS")
                print("enter 'c' to get a clue")
                ans1=input()
                if ans1=='c':
                    print("YOUR CLUE: INVENTORY")
                    str22=input("ENTER YOUR ANSWER:")
                else:    
                    str22=input("ENTER YOUR ANSWER:")
                        
                if str22=="STOCK":
                    print("YOU ARE CORRECT!!")
                    s+=5
                else:
                    print("YOUR ANSWER WAS:STOCK")
                    print("BETTER LUCK NEXT TIME")
                    print()
            
                print("11. TIWRE")
                print("enter 'c' to get a clue")
                ans1=input()
                if ans1=='c':
                    print("YOUR CLUE: COMPOSE")
                    str23=input("ENTER YOUR ANSWER:")
                else:    
                    str23=input("ENTER YOUR ANSWER:")
                        
                if str23=="WRITE":
                    print("YOU ARE CORRECT!!")
                    s+=5
                else:
                    print("YOUR ANSWER WAS:WRITE")
                    print("BETTER LUCK NEXT TIME")
                    print()
            
                print("12. HOUST")
                print("enter 'c' to get a clue")
                ans1=input()
                if ans1=='c':
                    print("YOUR CLUE: A DIRECTION")
                    str24=input("ENTER YOUR ANSWER:")
                else:    
                    str24=input("ENTER YOUR ANSWER:")
                        
                if str24=="SOUTH":
                    print("YOU ARE CORRECT!!")
                    s+=5
                else:
                    print("YOUR ANSWER WAS:SOUTH")
                    print("BETTER LUCK NEXT TIME")
                    print()
                print("YOU HAVE COME TO THE END OF THIS LEVEL")
                print("PLEASE CHOOSE A NEW LEVEL")
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            if ch==3:
                print("1. DIDCANATE")
                print("enter 'c' to get a clue")
                ans1=input()
                if ans1=='c':
                    print("YOUR CLUE: NOMINEE")
                    str25=input("ENTER YOUR ANSWER:")
                else:    
                    str25=input("ENTER YOUR ANSWER:")
                if str25=="CANDIDATE":
                    print("YOU ARE CORRECT!!")
                    s+=5
                else:
                    print("YOUR ANSWER WAS:CANDIDATE")
                    print("BETTER LUCK NEXT TIME")
                    print()
            
                print("2. FIDCONENCE")
                print("enter 'c' to get a clue")
                ans1=input()
                if ans1=='c':
                    print("YOUR CLUE: ASSURED")
                    str26=input("ENTER YOUR ANSWER:")
                else:    
                    str26=input("ENTER YOUR ANSWER:")
                        
                if str26=="CONFIDENCE":
                    print("YOU ARE CORRECT!!")
                    s+=5
                else:
                    print("YOUR ANSWER WAS:CONFIDENCE")
                    print("BETTER LUCK NEXT TIME")
                    print()
            
                print("3. SEASIDE")
                print("enter 'c' to get a clue")
                ans1=input()
                if ans1=='c':
                    print("YOUR CLUE: ILLNESS")
                    str27=input("ENTER YOUR ANSWER:")
                else:    
                    str27=input("ENTER YOUR ANSWER:")
                        
                if str27=="DISEASE":
                    print("YOU ARE CORRECT!!")
                    s+=5
                else:
                    print("YOUR ANSWER WAS:DISEASE")
                    print("BETTER LUCK NEXT TIME")
                    print()
            
                print("4. RUSSEIRP")
                print("enter 'c' to get a clue")
                ans1=input()
                if ans1=='c':
                    print("YOUR CLUE: AMAZEMENT")
                    str28=input("ENTER YOUR ANSWER:")
                else:    
                    str28=input("ENTER YOUR ANSWER:")
                    
                if str28=="SURPRISE":
                    print("YOU ARE CORRECT!!")
                    s+=5
                else:
                    print("YOUR ANSWER WAS:SURPRISE")
                    print("BETTER LUCK NEXT TIME")
                    print()
            
                print("5. MENTAPART")
                print("enter 'c' to get a clue")
                ans1=input()
                if ans1=='c':
                    print("YOUR CLUE: HOUSING")
                    str29=input("ENTER YOUR ANSWER:")
                else:    
                    str29=input("ENTER YOUR ANSWER:")
                    str29=input("ENTER YOUR ANSWER:")
                if str29=="APARTMENT":
                    print("YOU ARE CORRECT!!")
                    s+=5
                else:
                    print("YOUR ANSWER WAS:APARTMENT")
                    print("BETTER LUCK NEXT TIME")
                    print()

                print("6. TMENTDERAP")
                print("enter 'c' to get a clue")
                ans1=input()
                if ans1=='c':
                    print("YOUR CLUE: SECTOR")
                    str29=input("ENTER YOUR ANSWER:")
                else:    
                    str29=input("ENTER YOUR ANSWER:")
                    str29=input("ENTER YOUR ANSWER:")
                if str29=="DEPATMENT":
                    print("YOU ARE CORRECT!!")
                    s+=5
                else:
                    print("YOUR ANSWER WAS:DEPARTMENT")
                    print("BETTER LUCK NEXT TIME")        
                    print()
            
                print("7. MEABRRSADES")
                print("enter 'c' to get a clue")
                ans1=input()
                if ans1=='c':
                    print("YOUR CLUE: ASHAMED")
                    str30=input("ENTER YOUR ANSWER:")
                else:
                   str31=input("ENTER YOUR ANSWER:")
                if str31=="EMBARRASSED":
                    print("YOU ARE CORRECT!!")
                    s+=5
                else:
                   print("YOUR ANSWER WAS:EMBARASSED")
                   print("BETTER LUCK NEXT TIME")
                   print()
            
                print("8. EIGNROF")
                print("enter 'c' to get a clue")
                ans1=input()
                if ans1=='c':
                    print("YOUR CLUE: OVERSEAS")
                    str32=input("ENTER YOUR ANSWER:")
                else:
                    str32=input("ENTER YOUR ANSWER:")
                if str32=="FOREIGN":
                   print("YOU ARE CORRECT!!")
                   s+=5
                else:
                    print("YOUR ANSWER WAS:FOREIGN")
                    print("BETTER LUCK NEXT TIME")        
                    print()
            
                print("9. ALLYRENEG")
                print("enter 'c' to get a clue")
                ans1=input()
                if ans1=='c':
                    print("YOUR CLUE: NORMALLY")
                    str33=input("ENTER YOUR ANSWER:")
                else:    
                   str33=input("ENTER YOUR ANSWER:")
                   str33=input("ENTER YOUR ANSWER:")
                if str33=="GENERALLY":
                   print("YOU ARE CORRECT!!")
                   s+=5
                else:
                    print("YOUR ANSWER WAS:GENERALLY")
                    print("BETTER LUCK NEXT TIME")        
                    print()

                print("10. SROTYHSI")
                print("enter 'c' to get a clue")
                ans1=input()
                if ans1=='c':
                   print("YOUR CLUE: PAST EVENT")
                   str34=input("ENTER YOUR ANSWER:")
                else:    
                   str34=input("ENTER YOUR ANSWER:")
                   str34=input("ENTER YOUR ANSWER:")
                if str34=="HISTORY":
                   print("YOU ARE CORRECT:!!")
                   s+=5
                else:
                    print("YOUR ANSWER WAS:HISTORY")
                    print("BETTER LUCK NEXT TIME")        
                    print()
            
                print("11. LARLYMSII")
                print("enter 'c' to get a clue")
                ans1=input()
                if ans1=='c':
                    print("YOUR CLUE: SAME")
                    str35=input("ENTER YOUR ANSWER:")
                else:    
                    str35=input("ENTER YOUR ANSWER:")
                    str35=input("ENTER YOUR ANSWER:")
                if  str35=="SIMILARLY":
                    print("YOU ARE CORRECT!!")
                    s+=5
                else:
                    print("YOUR ANSWER WAS:SIMILARLY")
                    print("BETTER LUCK NEXT TIME")        
                    print()
            
                print("12. CESSUSC")
                print("enter 'c' to get a clue")
                ans1=input()
                if ans1=='c':
                   print("A STATE OF PROSPERITY AND FAME")
                   str36=input("ENTER YOUR ANSWER:")
                else:    
                   str36=input("ENTER YOUR ANSWER:")
                   str36=input("ENTER YOUR ANSWER:")
                if str36=="SUCESS":
                   print("YOU ARE CORRECT!!")
                   s+=5
                else:
                   print("YOUR ANSWER WAS:SUCESS")
                   print("BETTER LUCK NEXT TIME")        
                   print()
                print("YOU HAVE COME TO THE END OF THIS LEVEL")
                print("PLEASE CHOOSE A NEW LEVEL")
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        return s

    r=jumble()
    t2=time.time()
    t=t2-t1
    if t>120:
        print("Oops,you have elapsed the time")
        time.sleep(0.5)
        print("the game has to be finished in 120s and you have taken",t,"seconds")
        time.sleep(0.5)
        print(" 20 points would be deducted from your score")
        r=r-20
        print("score=",r)
        
    else:
        if r==0:
            print("OOPS BETTER LUCK NEXT TIME")
        else:
            print("you have finished the game within the time limit and the time taken is",t)
            time.sleep(0.5)
            print("So your score is",r)
    
    
    score1=str(r)+" "+str(t)
    #insert this into the db
    
    
    email1=e.get()
    import mysql.connector as sqltor
    con=sqltor.connect(host="localhost",user="root",passwd="T!$51h#86B7",database="MR")
    cursor=con.cursor()
    q="update mrds set jumb=%s where emailid=%s"
    i=(score1,email1)
    cursor.execute(q,i)
    con.commit()
    
    



def bingo():
    import random
    import time
    print("************WELCOME TO THE BINGO CHALLENGE*************")
    time.sleep(2)
    print("YOU WOULD BE GIVEN 120s TO COMPLETE THE GAME")
    time.sleep(2)
    print("SO HERE ARE THE INSTRUCTIONS OF THE GAME")
    time.sleep(1)
    print("1.The user has to chose the size of the grid of the bingo card(N) he wishes to play in")
    time.sleep(1)
    print("2.The user has to enter the range of the numbers he wishes to be on the bingo card")
    time.sleep(1)
    print("3.the user then has to guess N*N values")
    time.sleep(1)
    print("4.the user would win only if each value that he has entered is present on the bingo card")
    time.sleep(1)
    print("For instance,if the user enters minimum value 20 and maximum value 50 and grid size is 3 then:")
    print("The user has to enter any nine numbers within the range 20-50 and those nine values have to be present on the bingo card")
    time.sleep(1)
    print("5.The game is timed,so the user has to complete the game within the time limit of 120s")
    time.sleep(1)
    print("SO ALL THE BEST...AND LETS SEE HOW LUCKY YOU ARE")
    t1=time.time()
    def bingog():
        
        score=0
        gs=int(input("enter the size of ur grid IF 2x2 THEN 2 IF NXN THEN N"))
        min=int(input("enter min value"))
        max=int(input("enter max value"))
        card=[]
        l=[]
        l1=[]

        rr=range(min,max)
        card=random.sample(rr,gs*gs)
        for i in range(gs):
            s=""
            for j in range(gs):
                s+=str(card[i+j*gs])+"\t"
                l=s.split()
            for i in l:
                
                l1.append(i)
            
        for z in range(gs*gs):
            k=input("enter number")
            if k in l1:
                l1.remove(k)
            

        if len(l1)==0:
            score+=50
            print("U WON!!!")
            print("ur bingo card was:")
            for i in range(gs):
                s=""
                for j in range(gs):
                    s+=str(card[i+j*gs])+"\t"
                print(s)
        else:
            score=0
            
            print("ur bingo card was:")
            for i in range(gs):
                s=""
                for j in range(gs):
                    s+=str(card[i+j*gs])+"\t"
                print(s)
                                                                                                                                                                                                                                                                                                                                           
        return score
    p=bingog()
    t2=time.time()
    t=t2-t1
    if t>120:
        print("Oops,you have elapsed the time")
        time.sleep(0.5)
        print("the game has to be finished in 120s and you have taken",t,"seconds")
        time.sleep(0.5)
        print(" 20 points would be deducted from your score")
        p=p-25
        print("score=",p)
    else:
        if p==0:
            print("OOPS BETTER LUCK NEXT TIME")
            print("the time taken is",t)
        else:
            print("you have finished the game within the time limit and the time taken is",t)
            time.sleep(0.5)
            print("So your score is",p)
    score=str(p)+" "+str(t)
    

    email1=e.get()
    import mysql.connector as sqltor
    con=sqltor.connect(host="localhost",user="root",passwd="T!$51h#86B7",database="MR")
    cursor=con.cursor()
    q="update mrds set bingo=%s where emailid=%s"
    i=(score,email1)
    cursor.execute(q,i)
    con.commit()

     
        
def hang():
    
    import time
    name=n.get()
    print("Hi!",name,"Welcome to Lakshay's comp project")
    print('You are playing:-')
    print('Hangman')
    print("You have chosen to play:-")
    print('H',end='')
    time.sleep(0.5)
    print('A',end='')
    time.sleep(0.5)
    print('N',end='')
    time.sleep(0.5)
    print('G',end='')
    time.sleep(0.5)
    print('M',end='')
    time.sleep(0.5)
    print('A',end='')
    time.sleep(0.5)
    print('N')

    t1=time.time()
    def hangman():
        
        import random            

        print("The category/topic for this game would be the PYTHON PROGRAMMUNG LANGUAGE",'\n'"Quite your field of expertise I presume",name,";)",'\n')

        #waiting for one second
        time.sleep(1)
        print("Start guessing")
        time.sleep(0.5)
        word2=['python','dictionaries','keywords','tuples','boolean','lists','palindrome','float','decimal','boolean','strings','nesting','random']
        word=list(random.choice(word2))
        l=len(word)
        guesses=['_ ']*l
        print(guesses)
        turns=10
        failed=0
        c=0
        g=''
        s=0

        while turns!=0:
            print("The number of turns remaining=",turns,'\n')
            time.sleep(0.5)
            guess=input("Enter a character")
            for i in range(0,l):
                if guess==word[i]:
                    guesses[i]=guess
                    c=c+1
            print(guesses)
            if guesses==word:
                print("Congratulations",name,"! You have won! :)")
                s+=20
                break
            else:
                if c==0:
                    turns=turns-1
                    print("Sorry",name,"!, but",guess,"is incorrect :(")
                    c=0
                else:
                    turns=turns
                    print("Good guess",name,"! :)")
                    c=0
        if guesses!=word:
            print("Sorry",name,"!, You have lost :(")
            print("Your word was",word)
        return s
                   
    z=hangman()
    t2=time.time()
    t=t2-t1
    if t>120:
        print("Oops,you have elapsed the time")
        time.sleep(0.5)
        print("the game has to be finished in 120s and you have taken",t,"seconds")
        time.sleep(0.5)
        print(" 20 points would be deducted from your score")
        z=z-20
        print("score=",z)
    else:
        if z==0:
            print("OOPS BETTER LUCK NEXT TIME")
            print("You havent scored any points :o")
            print("the time taken is",t)
        else:
            print("you have finished the game within the time limit and the time taken is",t)
            time.sleep(0.5)
            print("So your score is",z)


    sc=str(z)+" "+str(t)
    email1=e.get()
    import mysql.connector as sqltor
    con=sqltor.connect(host="localhost",user="root",passwd="T!$51h#86B7",database="MR")
    cursor=con.cursor()
    q="update mrds set hang=%s where emailid=%s"
    i=(sc,email1)
    cursor.execute(q,i)
    con.commit()
    
    
   

            
    
    





def login():
    from PIL import Image,ImageTk
    wind=Toplevel()
    
    img0 = Image.open("C:\\Users\\Pradipti\\Pictures\\Saved Pictures\\aurora.jpg")
    p1 = ImageTk.PhotoImage(img0)
    l=Label(wind,image=p1)
    l.place(x=0,y=0)
    wind.title("HI!!!THIS IS YOUR BATTLEFIELD FOR 10 MINUTES !!CHOOSE WISELY TO WIN!!")
    wind.geometry("800x800")

    menu=Menu(root)
    wind.config(menu=menu)
    submenu=Menu(menu)
    menu.add_cascade(label="THE CLIMB",menu=submenu)
    submenu.add_command(label="GRAPH OF YOUR SCORE :)",command=graphh)
    
    
    

    
    img1 = Image.open("C:\\Users\\Pradipti\\Pictures\\Saved Pictures\\jumbled.webp")
    img1=img1.resize((150,150),Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(img1)
    a=Label(wind,image=photo)
    a.place(x=50,y=100)

    
    img2 = Image.open("C:\\Users\\Pradipti\\Pictures\\Saved Pictures\\hangman.jpg")
    img2 = img2.resize((150, 150), Image.ANTIALIAS) 
    photo2 = ImageTk.PhotoImage(img2)
    b=Label(wind,image=photo2,width=50,height=50)
    b.place(x=200,y=100)
    
    img3 = Image.open("C:\\Users\\Pradipti\\Pictures\\Saved Pictures\\fire.jpg")
    img3 = img3.resize((150, 150), Image.ANTIALIAS)
    photo3= ImageTk.PhotoImage(img3)
    c=Label(wind,image=photo3,width=100,height=100)
    c.place(x=50,y=300)
    
    img4 = Image.open("C:\\Users\\Pradipti\\Pictures\\Saved Pictures\\bingo.jpg")
    img4 = img4.resize((150, 150), Image.ANTIALIAS)
    photo4 = ImageTk.PhotoImage(img4)
    d=Label(wind,image=photo4,width=50,height=50)
    d.place(x=200,y=300)

    
    R1=StringVar()
    R2=StringVar()
    R3=StringVar()
    R4=StringVar()

    
    r1=Button(wind,text="JUMBLED WORDS",font=("segeo script",15,"bold"),fg="white",relief=SUNKEN,bg="red",command=jumbled)
    r2=Button(wind,text="HANGMAN",font=("segeo script",15,"bold"),fg="white",relief=SUNKEN,bg="red",command=hang)
    r3=Button(wind,text="FIREBALL",font=("segeo script",15,"bold"),fg="white",relief=SUNKEN,bg="red",command=fire)
    r4=Button(wind,text="BINGO",font=("segeo script",15,"bold"),fg="white",relief=SUNKEN,bg="red",command=bingo)
    r5=Button(wind,text="EXIT",font=("segeo script",15,"bold"),fg="white",relief=SUNKEN,bg="red",command=close_window)

    
    r1.place(x=50,y=50)
    r2.place(x=200,y=150)
    r3.place(x=50,y=250)
    r4.place(x=200,y=350)
    r5.place(x=50,y=500)

    
    wind.mainloop()
    


    
submit=Button(root,text="SUBMIT",width=20,bg="yellow",fg="brown",command=submit,font=("comic sans ms",20,"bold"))
submit.place(x=600,y=500)
login=Button(root,text="THE MAZE(ONLY FOR REGISTERED USERS)",width=50,bg="yellow",fg="brown",command=login,font=("comic sans ms",15,"bold"))
login.place(x=300,y=650)
login1=Button(root,text="REGISTER",width=30,bg="yellow",fg="brown",command=db,font=("comic sans ms",15,"bold"))
login1.place(x=600,y=350)#details button added

            

root.mainloop()
