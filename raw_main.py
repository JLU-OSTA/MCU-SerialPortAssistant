
import threading
import serial
import sys
import time

global com_raw
global command

def raw_write():
    global com_raw
    global command
    command="Hello."
    while (1):
        print "\n"
        command = raw_input("$:")
        com_raw.write(command)
        print command,
        #com_raw.write("OSTA" + command + "ATSO\n")

def raw_receive():
    global com_raw
    while (1):
        wd=com_raw.read()
        sys.stdout.write(wd)

def raw_help():
    global command
    while (1):
        if command == "help":
            print "TTL Debuger. Made by OSTA. V-0.1"
            print "Insert \'stop\' to exit."
            command = "That all."

threads = []
t1 = threading.Thread(target=raw_write,args=())
threads.append(t1)
t2 = threading.Thread(target=raw_receive,args=())
threads.append(t2)
t3 = threading.Thread(target=raw_help,args=())
threads.append(t3)

def main():
    global com_raw
    global command
    com_port = raw_input("Please input a serial port num:")
    print "You choose the port com" + com_port
    speed = raw_input("Please input the speed of the port:")
    com_raw = serial.Serial('com' + com_port, speed)
    com_raw.write('Connection is completed on COM' + com_port + " and speed is " + speed + " !\n")
    print "\n"
    print "Connection is completed!"
    print "The following is the connection information:"
    print "Port: COM" + com_port
    print "Speed: " + speed
    print "That is all!\n"
    for t in threads:
        t.setDaemon(True)
        t.start()
    while (command != "stop"):
            time.sleep(0.5)
    print "Connection break."
    com_raw.write("\nConnection break.\n")

if __name__ == '__main__':
    main()