import math
import random
from fractions import Fraction
a=0
b=0
run=0
wick=0
tot=0
totwick=0
balls1=0
balls2=0
bp1=0
bp=0
bp2=0

k=random.randint(0,1)
if k==1:
   s1='Shane'
   s2='Adarsh'
elif k==0:
   s1='Adarsh'
   s2='Shane'

players=[s1,s2,"cooper","Tom","Freddy","harman","Uday","Khan","Sam","jason","kevin"]
Runscored=[0,0,0,0,0,0,0,0,0,0,0]
Ballsplayed=[0,0,0,0,0,0,0,0,0,0,0]

for i in range(6):
   
    a= random.randint(0,50)
    b=random.randint(0,(50-a))
    if b in range(0,20):
        wick=0
    elif b in range(20,40):
        wick=1
    else:
        wick=2
    if a in range(0,19):
        run=random.randint(0,10)
    elif a in range(19,30):
        run=random.randint(int(a/3),13-totwick)
    elif a in range(31,45):
        run=random.randint(int(0),19-(2*totwick))
    elif a in range(46,51):
         run=random.randint(int(a/5),29-(2*totwick))
    tot=tot+run
    totwick=totwick+wick
    score1=random.randint(0,run)
    score2=run-score1
    if score1>=score2:
        if score1==0:
           bp=random.randint(0,3)
        elif score1 in range(1,4):
           bp=random.randint(1,6)
        elif score1 in range(4,12):
           bp=random.randint(2,6)
        elif score1 in range(12,18):
           bp=random.randint(3,6)
        elif score1 in range(18,24):
           bp=random.randint(4,6)
        elif score1 in range(24,30):
           bp=random.randint(5,6)
        bp2=6-bp
    else:
        if score1==0:
           bp2=random.randint(0,3)
        elif score1 in range(1,4):
           bp2=random.randint(1,6)
        elif score1 in range(4,12):
           bp2=random.randint(2,6)
        elif score1 in range(12,18):
           bp2=random.randint(3,6)
        elif score1 in range(18,24):
           bp2=random.randint(4,6)
        elif score1 in range(24,30):
           bp2=random.randint(5,6)
        bp=6-bp2
    Ballsplayed[totwick]=Ballsplayed[totwick]+bp
    Ballsplayed[totwick+1]=Ballsplayed[totwick+1]+bp2
    Runscored[totwick]=Runscored[totwick]+score1
    Runscored[totwick + 1]=Runscored[totwick + 1]+score2
    print(tot,"-",totwick,"(",i+1,")",players[totwick] ,Runscored[totwick] ,'(',Ballsplayed[totwick],')',players[totwick+1] ,Runscored[totwick+1] ,'(',Ballsplayed[totwick+1],')')
print("Poweplay ends")
q=input("")

for i in range(6,12):
     if totwick==10:
        break
     a= random.randint(0,50)
     b=random.randint(0,(50-a))
     if b in range(0,25):
        wick=0
     elif b in range(25,40):
        wick=1
     else:
        wick=2
     if a in range(0,19):
        run=random.randint(2,11-totwick)
     elif a in range(19,30):
        run=random.randint(2,14-(2*(totwick-1)))
     elif a in range(31,45):
        run=random.randint(int(a/5),20-(2*(totwick-1)))
     elif a in range(46,51):
         run=random.randint(int(5),31-(2*totwick))
     tot=tot+run
     totwick=totwick+wick
     
     score1=random.randint(0,run)
     score2=run-score1
     Runscored[totwick]=Runscored[totwick]+score1
     Runscored[totwick + 1]=Runscored[totwick + 1]+score2
     if score1>=score2:
        if score1==0:
           bp=random.randint(0,3)
        elif score1 in range(1,4):
           bp=random.randint(1,6)
        elif score1 in range(4,12):
           bp=random.randint(2,6)
        elif score1 in range(12,18):
           bp=random.randint(3,6)
        elif score1 in range(18,24):
           bp=random.randint(4,6)
        elif score1 in range(24,30):
           bp=random.randint(5,6)
        bp2=6-bp
     else:
        if score1==0:
           bp2=random.randint(0,3)
        elif score1 in range(1,4):
           bp2=random.randint(1,6)
        elif score1 in range(4,12):
           bp2=random.randint(2,6)
        elif score1 in range(12,18):
           bp2=random.randint(3,6)
        elif score1 in range(18,24):
           bp2=random.randint(4,6)
        elif score1 in range(24,30):
           bp2=random.randint(5,6)
        bp=6-bp2
     Ballsplayed[totwick]=Ballsplayed[totwick]+bp
     Ballsplayed[totwick+1]=Ballsplayed[totwick+1]+bp2
     
     print(tot,"-",totwick,"(",i+1,")",players[totwick] ,Runscored[totwick] ,'(',Ballsplayed[totwick],')',players[totwick+1] ,Runscored[totwick+1] ,'(',Ballsplayed[totwick+1],')')
print('End of 12th Over')
q=input("")
for i in range(12,16):
     
     a= random.randint(0,50)
     b=random.randint(0,(50-a))
     if b in range(0,20):
        wick=0
     elif b in range(20,40):
        wick=1
     else:
        wick=2
     if a in range(0,19):
        run=random.randint(int(a/3),13-totwick)
     elif a in range(19,30):
        run=random.randint(4,int(a/2))
     elif a in range(31,45):
        run=random.randint(5,18-(totwick))
     elif a in range(46,51):
         run=random.randint(int(5),30-totwick)
     tot=tot+run
     totwick=totwick+wick
     score1=random.randint(0,run)
     score2=run-score1
     balls1=random.randint(int(run/6),3+int(run/6))
     balls2=6-balls1
     Ballsplayed[totwick]=Ballsplayed[totwick]+balls1
     Ballsplayed[totwick+1]=Ballsplayed[totwick+1]+balls2
    
     Runscored[totwick]=Runscored[totwick]+score1
     Runscored[totwick + 1]=Runscored[totwick + 1]+score2
     print(tot,"-",totwick,"(",i+1,")",players[totwick] ,Runscored[totwick] ,'(',Ballsplayed[totwick],')',players[totwick+1] ,Runscored[totwick+1] ,'(',Ballsplayed[totwick+1],')')
print('End of 16th Over')   
q=input("")
for i in range(16,19):
   
     if totwick in range(0,6):
         a= random.randint(0,50)
         b=random.randint(0,(50-a))
         if b in range(0,20):
            wick=0
         elif b in range(20,40):
            wick=1
         else:
             wick=2
         if a in range(0,16):
            run=random.randint(5-int(totwick/3),int(5+(a/2)))
         elif a in range(16,27):
            run=random.randint(6,int(a/2)+3)
         elif a in range(27,45):
            run=random.randint(7,20)
         elif a in range(46,51):
             run=random.randint(int(7),30)
         tot=tot+run
         totwick=totwick+wick
         score1=random.randint(0,run)
         score2=run-score1
         Runscored[totwick]=Runscored[totwick]+score1
         Runscored[totwick + 1]=Runscored[totwick + 1]+score2
         balls1=random.randint(int(run/6),3+int(run/6))
         balls2=6-balls1
         Ballsplayed[totwick]=Ballsplayed[totwick]+balls1
         Ballsplayed[totwick+1]=Ballsplayed[totwick+1]+balls2
         print(tot,"-",totwick,"(",i+1,")",players[totwick] ,Runscored[totwick] ,'(',Ballsplayed[totwick],')',players[totwick+1] ,Runscored[totwick+1] ,'(',Ballsplayed[totwick+1],')')
     else:
         a= random.randint(0,50)
         b=random.randint(0,(50-a))
         if b in range(0,20):
            wick=0
         else:
            wick=1
         if a in range(0,19):
            run=random.randint(3,9)
         elif a in range(19,30):
            run=random.randint(3,int(a/2.5))
         elif a in range(31,45):
            run=random.randint(3,16)
         elif a in range(46,51):
             run=random.randint(int(4),24)
         tot=tot+run
         totwick=totwick+wick
         score1=random.randint(0,run)
         score2=run-score1
         Runscored[totwick]=Runscored[totwick]+score1
         Runscored[totwick + 1]=Runscored[totwick + 1]+score2
         balls1=random.randint(int(run/6),3+int(run/6))
         balls2=6-balls1
         Ballsplayed[totwick]=Ballsplayed[totwick]+balls1
         Ballsplayed[totwick+1]=Ballsplayed[totwick+1]+balls2
         print(tot,"-",totwick,"(",i+1,")",players[totwick] ,Runscored[totwick] ,'(',Ballsplayed[totwick],')',players[totwick+1] ,Runscored[totwick+1] ,'(',Ballsplayed[totwick+1],')')
q=input("")
for i in range(19,20):
     
     
     if totwick in range(0,6):
         a= random.randint(0,50)
         b=random.randint(0,(50-a))
         if b in range(0,20):
            wick=0
         elif b in range(20,35):
            wick=1
         else:
            wick=2
         if a in range(0,16):
            run=random.randint(5,12)
         elif a in range(16,30):
            run=random.randint(6,int(a/2)+1)
         elif a in range(31,41):
            run=random.randint(7,20)
         elif a in range(41,51):
             run=random.randint(int(5),30)
         tot=tot+run
         totwick=totwick+wick
         score1=random.randint(0,run)
         score2=run-score1
         Runscored[totwick]=Runscored[totwick]+score1
         Runscored[totwick + 1]=Runscored[totwick + 1]+score2
         balls1=random.randint(int(run/6),3+int(run/6))
         balls2=6-balls1
         Ballsplayed[totwick]=Ballsplayed[totwick]+balls1
         Ballsplayed[totwick+1]=Ballsplayed[totwick+1]+balls2
         print(tot,"-",totwick,"(",i+1,")",players[totwick] ,Runscored[totwick] ,'(',Ballsplayed[totwick],')',players[totwick+1] ,Runscored[totwick+1] ,'(',Ballsplayed[totwick+1],')')
     else:
         a= random.randint(0,50)
         b=random.randint(0,(50-a))
         if b in range(0,20):
            wick=0
         elif b in range(20,35):
            wick=1
         else:
            wick=2
         if a in range(0,16):
            run=random.randint(3,9)
         elif a in range(16,30):
            run=random.randint(5,int(a/2.5))
         elif a in range(31,45):
            run=random.randint(6,14)
         elif a in range(46,51):
             run=random.randint(int(5),27-(totwick))
         tot=tot+run
         totwick=totwick+wick
         score1=random.randint(0,run)
         score2=run-score1
         Runscored[totwick]=Runscored[totwick]+score1
         Runscored[totwick + 1]=Runscored[totwick + 1]+score2
         balls1=random.randint(int(run/6),3+int(run/6))
         balls2=6-balls1
         Ballsplayed[totwick]=Ballsplayed[totwick]+balls1
         Ballsplayed[totwick+1]=Ballsplayed[totwick+1]+balls2
         print(tot,"-",totwick,"(",i+1,")",players[totwick] ,Runscored[totwick] ,'(',Ballsplayed[totwick],')',players[totwick+1] ,Runscored[totwick+1] ,'(',Ballsplayed[totwick+1],')')

for z in range(0,totwick+2):
    if Ballsplayed[z]==0:
        strikerate=0
    else:
        strikerate=(Runscored[z]/Ballsplayed[z])*100
    print(players[z],Runscored[z],'(',Ballsplayed[z],')',"S/R - ",int(strikerate))
    
