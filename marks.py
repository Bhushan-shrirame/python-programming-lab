name=input("ENTER YOUR NAME=")               #INPUTING THE NAME FROM USER
roll=int(input("ENTER YOUR ROLL NUMBER="))   #INPUTING THE ROLL NUMBER OF STUDENT AS INTEGER DATA TYPE
eng=int(input("ENTER YOUR ENGLISH MARKS="))  #INPUTING THE STUDENT'S ENGLISH MARKS AS INTEGER DATA TYPE
math=int(input("ENTER YOUR MATHS MARKS="))   #INPUTING THE STUDENT'S MATHEMATICS MARKS AS INTEGER DATA TYPE
sci=int(input("ENTER YOUR SCIENCE MARKS="))  #INPUTING THE STUDENT'S SCIENCE MARKS AS INTEGER DATA TYPE
s=math+sci+eng                               #STORING THE SUM OF MARKS IN VARIABLE S
avg=s/3                                      #TAKING THE AVERAGE OF THE MARKS AND STORING IT IN VARIABLE AVG
print("SUM OF MARKS="+str(s))                #PRINTING THE SUM OF MARKS OF STUDENT
print("AVERAGE MARKS="+str(avg))             #PRINTING THE AVERAGE MARKS OF STUDENT
