#!/usr/bin/python
#coding: utf-8

import urllib2
import bluetooth
import time

users = ['user1', 'user2']
addrs = ["11:11:11:!1:11:11", "22:22:22:22:22:22"]
statuses = [False, False]

url = 'https://hooks.slack.com/services/xxxxxxxxxxxxxx/xxxxxx'

time.sleep(10)

def send_msg(text):
    req = urllib2.Request(url, '{"text": "'+text+'"}', {'Content-Type': 'application/json'})
    f = urllib2.urlopen(req)
    f.close()
    return

send_msg("labKeeper start!")
print "LabKeeper Start!!!"

while True:
    print "Checking " + time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())

    statusChanged = False

    for index in range(0, len(users)):
        result = bluetooth.lookup_name(addrs[index], timeout=5)
        if (result != None and statuses[index] == False):
            print users[index] + " 來了！！"
            statuses[index] = True
            statusChanged = True           
            send_msg(users[index]+' 來社窩囉:smile:')

        elif (result == None and statuses[index] == True):
            print users[index] + " 走了 QQ"
            statuses[index] = False
            statusChanged = True           
            send_msg(users[index]+' 離開社窩了:sleeping:')
    if (statusChanged == True):
        activeUsers = []
        for index in range(0, len(users)):
            if (statuses[index] == True):
                activeUsers.append(users[index])
        if (len(activeUsers) > 0):
            send_msg("[:heart:社窩開放中] 目前人員有: "+" ".join(activeUsers))
        else:
            send_msg("[:u7a7a:社窩關閉] 目前社窩沒有人哦")

    time.sleep(120)

