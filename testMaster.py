from time import sleep
import socket
import Tello
import keyboard
import sys, select, os
if os.name == 'nt':
  import msvcrt
else:
  import tty, termios

msg = """

Controls:
        z
   q    s    d
        x

"""
coords = [0,0,0,0]

def getKey():
    if os.name == 'nt':
      return msvcrt.getch()

    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

tello = Tello.Tello('192.168.36.122', 8889)
tello2 = Tello.Tello('192.168.36.159', 8889)
# tello = Tello.Tello('192.168.10.1', 8889)
tello.start()
tello2.start()

tello.getStarted()
tello2.getStarted()
sleep(1)
print(msg)

keyboard.add_hotkey("z", lambda: front())
keyboard.add_hotkey("q", lambda: left())
keyboard.add_hotkey("s", lambda: stop())
keyboard.add_hotkey("d", lambda: right())
keyboard.add_hotkey("x", lambda: back())
keyboard.add_hotkey("p", lambda: land())
keyboard.add_hotkey(" ", lambda: uptello())

def front():
    print("front")
    coords = [0,100,0,0]
    tello.move_translation( coords[1] , coords[0], coords[2], coords[3])
    tello2.move_translation( coords[1] , coords[0], coords[2], coords[3])
    sleep(1)
    tello.stop()
    tello2.stop()
def back():
    coords = [0,-100,0,0]
    tello.move_translation( coords[1] , coords[0], coords[2], coords[3])
    tello2.move_translation( coords[1] , coords[0], coords[2], coords[3])
def left():
    coords = [-100,0,0,0]
    tello.move_translation( coords[1] , coords[0], coords[2], coords[3])
    tello2.move_translation( coords[1] , coords[0], coords[2], coords[3])
    sleep(1)
    tello.stop()
    tello2.stop()
def right():
    coords = [100,0,0,0]
    tello.move_translation( coords[1] , coords[0], coords[2], coords[3])
    tello2.move_translation( coords[1] , coords[0], coords[2], coords[3])
    sleep(1)
    tello.stop()
    tello2.stop()
def stop():
    tello.stop()
    tello2.stop()
    
def land():
    tello.land()
    tello2.land()
def uptello():
    print("up")
    coords = [0,0,100,0]
    tello.move_translation( coords[1] , coords[0], coords[2], coords[3])
    tello2.move_translation( coords[1] , coords[0], coords[2], coords[3])
    sleep(1)
    tello.stop()
    tello2.stop()

def flip(direction):
    tello.flip(direction)
    #tello2.flip(direction)


socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', 9000))

while True:
        sleep(0.1)

