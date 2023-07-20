#question 1
def check_password_strength(string):
    u=0
    l=0
    n=0
    c=0
    for i in range (0,len(string)):
        k=ord(string[i])
        if k in range(65,91):
            u+=1
        elif k in range(97,123):
            l+=1
        elif k in range(48,57):
            n+=1
        elif k in range(32,48) or k in range(58,65) or k in range(91,97) or k in range(123,127):
            c+=1
    if u!=0 and l!=0 and n!=0 and c!=0 and len(string)>7:
        print("Good Password")
        return True    
    else:
        if u==0:
            print("Please include atleast one Upper case alphabet")
        if l==0:
            print("please include atleast one lower case alphabet")
        if n==0:
            print("please include atleast one number")
        if c==0:
            print("please include atleast one special character")
        if len(string)<8:
            print("Password length should be minimum 8")
        return False
string=input("Enter your password : ")
a=check_password_strength(string)
print(a)

#question 2
import psutil ,time
from win10toast import ToastNotifier
Notification=ToastNotifier()
while True:
    cpu_percent_usage=psutil.cpu_percent()
    print("current_cpu_status:",cpu_percent_usage)
    if cpu_percent_usage>80:
        print("Alert! CPU usage exceeds threshold:",cpu_percent_usage)
        title="CPU Alert"
        message="Cpu excess usage" ,cpu_percent_usage
        Notification.show_toast(title,message)
    time.sleep(2)

#question 4
import os
import shutil
import datetime

def backup(source_dir, dest_dir):
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            source_file = os.path.join(root, file)
            dest_file = os.path.join(dest_dir, file)
            shutil.copy2(source_file, dest_file)

if __name__ == '__main__':
    backup_day = 3
    today = datetime.datetime.today()
    if today.weekday()==backup_day:
        source_dir = input("Enter your source directory: ")
        dest_dir = input("Enter your destination directory you want it to be backed up : ")
        backup(source_dir, dest_dir)