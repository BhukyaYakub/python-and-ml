'''AIM : It is an emergency chatbot -The RescueBot. The sole purpose of this bot is to help people in tricky and tough emergencies regarding crimes.
         It is a demo version of how people can be talked through to solve an emergency situation by this bot.
         RescueBot helps people to immediately acquire help by sending their location, name and emergency details to the police control room via sms or email .This bot also suggests safety measures to overcome these dire situations until help comes.
         RescueBot gives people new hope and strength to handle crisis.
         RescueBot gives deaf and dumb citizens a chance to survive as they cannot use the previlidge of calling the police.
         The illiterate, educated, poor , rich, weak , strong no matter who-- everyone alike can find help through RescueBot.''' 



import random
import string
import time
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login("yakub832@gmail.com", "8185893614") 
  
# message to be sent
fromaddr = "yakub832@gmail.com"
toaddr = "b131832@rgukt.ac.in"

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr




def f0():
    name=input("What is your name? : ")
    loc=input("\nWhat is your location? : ")
    hurt=input("\nIs anyone hurt?y/n : ")
    
    if hurt=="y":
        print("Don't panic!\nHelp is on the way!") 
        vic=str(input("\nHow many people are hurt? : "))
    else :
        vic="none"
    print("The concerned authorities have been informed of your situation and will be there for your aid.\n   You have to be at your strongest when you're feeling at your weakest.")
    #the information entered above must be sent to the mail of the rescue team or to their respective phone number via sms.
    body = 'Name : %s' % name+"\nLocation : %s" %loc+"\nAnyone hurt ? %s"%hurt+"\nHow many are hurt ? "+vic
    msg.attach(MIMEText(body, "plain"))

    str1=msg.as_string()
    # sending the mail 
    s.sendmail("yakub832@gmail.com", "b131832@rgukt.ac.in",str1) 
    print("\nEmail sent successfully !!\nPlease answer the follow up questions for better understanding of your situation : ")
    return 0
        

def f1():
    name=input("\nAre you alone? y/n : ")
    if name=="y":
        print("Talk things through.\nStay calm.\nTry to move into a crowded place")
    acc=input("\nDo you recognize the accused?y/n : ")
    if acc=="y":
        a=str(input("Enter full name of accused: "))
    else :
        a="unknown"
    print("Try to move into a crowded place.\nInform anyone nearby.\nRemain calm but vigilant.\nIf things get out of hand seek attention from the crowd and let people know about your situation.")
    body = '\n\nAdditional Details :\nVictim Alone : %s' %name+"\nAccused : %s" %a
    msg.attach(MIMEText(body, "plain"))
    str1=msg.as_string()
    # sending the mail 
    s.sendmail("yakub832@gmail.com", "b131832@rgukt.ac.in",str1)
        
def f2():
    num=input("\nHow many attackers are there? : ")
    vic=input("\nIs the attacker still in the vicinity? y/n : ")
    if vic=="y":
        print("\nMake sure you move into a safe area, far away from the accused.\nRemain calm and don't instigate the attacker.")
    acc=input("\nDo you recognize the accused?y/n : ")
    if acc=="y":
        a=input("Enter full name of accused: ")
    else :
        a="unknown"
    print("Do not make any sudden movements.It may create tension for the attacker and instigate them.\nDo not compromise on your's or other's safety.")
    body = '\n\nAdditional Details :\nNo. of Attackers : '+num+"\nAttacker in the vicinity ? %s"%vic+"\nAccused : %s" %a
    msg.attach(MIMEText(body, "plain"))
    str1=msg.as_string()
    # sending the mail 
    s.sendmail("yakub832@gmail.com", "b131832@rgukt.ac.in",str1)

def f3():
    dan=input("\nAre you in the danger zone?y/n : ")
    if dan=="y":
        print("\nPull the nearest Fire Alarm.\nBe sure to feel doors for heat before opening them.\n Stay low to the ground\nKeep hand on the wall.\nSearch for the nearest Fire Extinguisher.")
    else :
        print("Help in putting out the fire.\nNotify the area Fire Department.\nHelp in the rescue but be careful.")
    source=input("\nWhat is the source of the fire? : ")
    trap=input("\nHow many people are trapped inside the building? : ")
    lon=input("\nHow long has it been since the fire started? : ")
    body = '\n\nAdditional Details :\nSource of Fire : %s' %source+"\nNo of People trapped : "+a+"\nEstimated Fire Period : %s"%lon
    msg.attach(MIMEText(body, "plain"))
    str1=msg.as_string()
    # sending the mail 
    s.sendmail("yakub832@gmail.com", "b131832@rgukt.ac.in",str1)

def f4():
    age=input("\nWhat is the age of the child? : ")
    gen=input("\nwhat is the name of the victim? : ")
    name=input("\nWhat is the name of the abuser? : ")
    wit=input("\nAre you a witness?y/n : ")
    if wit=="y":
        print("\nYou need to protect the child from further harm.\nBut be careful not to take the law into your own hands.")
    print("\nThe local Child Protective Services are on their way.Please remain calm and vigilant")
    body = '\n\nAdditional Details :\nAge of the child : %s' %age+"\nName of the victim : %s"%gen+"\nName of the abuser : %s"%name
    msg.attach(MIMEText(body, "plain"))
    str1=msg.as_string()
    # sending the mail 
    s.sendmail("yakub832@gmail.com", "b131832@rgukt.ac.in",str1)
    

def f5():
    vic=input("\nAre you the victim?y/n : ")
    lon=input("\nIs the abuse frequent?y/n : ")
    if lon=="y":
        h=input("\nHow long has this been happening for? : ")
    name=input("\nWhat is the abuser's full name : ")    
    print("\nThe victim must be strong and not lose hope.\nDon't hide it and suffer alone.\nHelp is on the way.")
    body = '\n\nAdditional Details :\nAre you the victim ? : %s' %vic+"\nHow long has the abuse been going on ? : %s"%h+"\nAbuser's Name : %s"%name
    msg.attach(MIMEText(body, "plain"))
    str1=msg.as_string()
    # sending the mail 
    s.sendmail("yakub832@gmail.com", "b131832@rgukt.ac.in",str1)

    
def f6():
    cas=input("\nHow many casualties? : ")
    att=input("\nHow many attackers are there? : ")
    vic=input("\nAre you the victim?y/n : ")
    if vic=="y":
        print("\nClear away from the danger zone.\nSeek any local help until the Rescue Team arrives")
    ty=input("\nWhat type of hate crime is it? : ")
    body = '\n\nAdditional Details :\nCasualties : %s' %cas+"\nNo of Attackers : "+att+"\nAre you the victim ? : %s"%vic+"\nType of Hate Crime : %s"%ty
    msg.attach(MIMEText(body, "plain"))
    str1=msg.as_string()
    # sending the mail 
    s.sendmail("yakub832@gmail.com", "b131832@rgukt.ac.in",str1)

def f7():
    ar=input("\nAre you still in the area of gas leakage?y/n : ")
    leak=input("\nHow long has the gas been leaking? : ")
    peop=input("\nHow many people are there in the vicinity?")
    print("\nDo not inhale the gas.\nImmediately evacuate the area.\nCaution the neighbourhood.")
    body = '\n\nAdditional Details :\nDuration of Gas Leakage : %s' %leak+"\nNo of People trapped : %s"%peop
    msg.attach(MIMEText(body, "plain"))
    str1=msg.as_string()
    # sending the mail 
    s.sendmail("yakub832@gmail.com", "b131832@rgukt.ac.in",str1)
    
def f8():
    at=input("\nHow many attackers are there? : ")
    sd=input("\nAre you the victim?y/n :")
    if sd=="y":
        k=input("\nAre you familiar with the attackers?y/n : ")
    else :
        k="unknown"
    print("\nScream for help\n Move into a crowded place")
    body = '\n\nAdditional Details :\nNo of Attackers : %s' %at+"\nAre you the Victim : %s"%sd+"\nAttacker Name : %s"%k
    msg.attach(MIMEText(body, "plain"))
    str1=msg.as_string()
    # sending the mail 
    s.sendmail("yakub832@gmail.com", "b131832@rgukt.ac.in",str1)
    
def f9():
    na="unknown"
    mw="unknown"
    au=input("\nAre you the victim?y/n :")
    if au=="y":
        s=input("\nDo you recognise the attacker?y/n :")
        if s=="y":
           na=input("\nWhat is the full name of the attacker? :")
           print("\nMove into a crowded area as quickly as possible.")
    mw=input("\nWhat is the murder weapon? :")
    body = '\n\nAdditional Details :\nAre you the Victim ? %s' %au+"\nAttacker Name : %s"%na+"\nMurder Weapon : %s"%mw
    msg.attach(MIMEText(body, "plain"))
    str1=msg.as_string()
    # sending the mail 
    s.sendmail("yakub832@gmail.com", "b131832@rgukt.ac.in",str1)
    
def f10():
    hm=input("\nHow many attackers?:")
    ki=input("\nAre you the victim?y/n :")
    if ki=="y" :
       h=input("\nDo you recognise the attacker?y/n :")
       mt=("\nWhat is the motive of the kidnap? : ")
    print("\nDo not try to instigate the kidnappers at anytime.\nPay attention to background noise and distinct information")
    body = '\n\nAdditional Details :\nAttackers : %s' %hm+"\nVictim ? %s"%ki+"\nRecognise the Kidnapper ? %s"%h+"\nKidnapping Motive : %s"%mt
    msg.attach(MIMEText(body, "plain"))
    str1=msg.as_string()
    # sending the mail 
    s.sendmail("yakub832@gmail.com", "b131832@rgukt.ac.in",str1)

def f11():
    tc=input("\nWhat is the time of cease? : ")
    ht=input("\nHow many hostages? : ")
    cs=input("\nHow many casualities? : ")
    wd=input("\nWhat are the demands? : ")
    nt=input("\nHow many attackers? : ")
    print("\nDo not instigate the terrorists.\nDo not jeapordize the safety of your fellow hostages.\nBe vigilant")
    body = '\n\nAdditional Details :\nTime of Cease : %s' %tc+"\nHostages : %s"%ht+"\nCasualties : %s"%cs+"\nDemands : %s"%wd+"\nAttackers : %s"%nt
    msg.attach(MIMEText(body, "plain"))
    str1=msg.as_string()
    # sending the mail 
    s.sendmail("yakub832@gmail.com", "b131832@rgukt.ac.in",str1)
    
  
    
crimes={"1":"ANTISOCIAL BEHAVIOUR","2":"BURGLARY/ROBBERY","3":"FIRE","4":"CHILD ABUSE","5":"DOMESTIC VIOLENCE","6":"HATE CRIME","7":"GAS LEAKAGE","8":"RAPE/SEXUAL HARASSMENT","9":"MURDER","10":"KIDNAP","11":"TERRORISM"}
print("EMERGENCIES  :--\n ")
for x,y in crimes.items():
    print(x,y)
while True:
    print("This is RescueBot.\nWhat is your emergency : ")
    a=input()
    if a in crimes.keys():
        r=str(random.randint(0,sys.maxsize))
        print("Your emergency is "+crimes.get(a))
        msg['Subject'] = crimes[a]+" : "+r
        h=f0()
        break
    else:
        print("Your choice is wrong!")
b=int(a)
if b==1 :
    f1()
elif b==2 :
    f2()
elif b==3 :
    f3()
elif b==4 :
    f4()
elif b==5 :
    f5()
elif b==6 :
    f6()
elif b==7 :
    f7()
elif b==8 :
    f8()
elif b==9 :
    f9()
elif b==10 :
    f10()
else :
    f11()
  


  
#this information must also be sent to the response team via email or sms.
print("\n\nThank You for using RescueBot.Be strong and wait for help.")
    
# terminating the session 
s.quit()     



