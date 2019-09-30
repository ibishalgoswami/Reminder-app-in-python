import time
from win10toast import ToastNotifier
import re

#myFile = 'C:/Users/Desktop/New folder/containerfile'

URL = 'https://www.way2sms.com/api/v1/sendCampaign'

def checkTodaysBirthdays():
    while True:
        fileName = open(myFile, 'r')
        today = time.strftime('%H:%M')
        flag = 0
        for line in fileName:
            if today in line:
                result = re.sub(r'[:]', r'', line)
                result2 = ''.join(i for i in result if not i.isdigit())
                flag = 1
        if flag == 1:
            notifier = ToastNotifier()
            notifier.show_toast("To Do", result2, duration=16)
        else:
            print("Nothing to show")
            break

checkTodaysBirthdays()
