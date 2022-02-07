from asyncio import sleep
import threading 
import socket
import sys
import time

class Tello(threading.Thread):
    def __init__(self, ip, port):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.host = "127.0.0.1"
        self.tello_address = (self.ip, self.port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        self.recvThread = threading.Thread(target=self.recv)
        self.recvThread.start()

        

    def recv(self):
        count = 0
        while True: 
            try:
                data, server = self.sock.recvfrom(1518)
                return (data.decode(encoding="utf-8"))
            except Exception:
                print ('\nExit . . .\n')
                break

    def send(self, msg):
        msg = msg.encode(encoding="utf-8") 
        sent = self.sock.sendto(msg, self.tello_address)

    def stop(self):
        self.send("stop")
        
    def move_translation(self, x, y, z, yaw):

        self.send("rc "+ str(y)+" "+str(x)+" "+str(z)+" "+str(yaw))

#        if(x > 0):
#            self.send("forward "+ str(abs(x)))
#        elif(x < 0):
#            self.send("back " +str(abs(x)))
#        if(y > 0):
#            self.send("right "+ str(y))
#        elif(y < 0):
#            self.send("left "+ str(abs(y)))
#        if( z > 0):
#            self.send("up "+str(z))
#        elif(z < 0):
#            self.send("down "+str(abs(z)))

    def getStarted(self): #init sdk mode + takeoff
        self.send("command")
        if (self.recv() == "ok"):
            self.send("takeoff")
    
    def land(self):
        self.send("land")

    def flip(self, direction): #lrfb
        self.send("flip "+direction)
    
