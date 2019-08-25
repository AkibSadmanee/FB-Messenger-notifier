import sys

sys.path.append("./Methods/")

from preprocess import login
from fbchat import Client
from text2speech import read
from time import sleep
from getpass import getpass
import os
    
if __name__ == "__main__":
    email = input("Enter Email: ")
    password = getpass("Enter Password: ")
    
    client = login(email,password,Client)
    if not os.path.exists('Messages'):
        os.makedirs('Messages')
    while True:
        fw = open("./Messages/Unread.txt", "a+",encoding="utf-8")
        unread_msgs = client.fetchUnread()
        for threadid in unread_msgs:
            client.markAsRead(threadid)
            thread = client.fetchThreadInfo(threadid)[threadid]
            print(thread)
            
            messages = client.fetchThreadMessages(thread_id=threadid, limit=20)
            for message in messages:
                if not message.is_read:
                    if message.text:
                        writable = message.text + "~*~" + thread.name + "~*~" + "~*~" + message.timestamp + "\n"
                        fw.writelines(writable)
                        readout_text = thread.name + "~*~" + message.text
                        lock = read(readout_text)
        fw.close()
