import os
import socket
import sys

def retbanner(ip,port):
    try:
        socket.setdefaulttimeout(5)
        s = socket.socket()
        #s.bind((ip,port))
        s.connect((ip,port))
        banner = s.recv(1024)
        s.close()
        return banner
    except Exception as e:
        print(e)
def checkvulns(banner,filename):
    f = open(filename,"r")
    for line in f.readlines():
        if line.strip('\n') in banner:
            print ("{}服务可用".format(banner.strip("\n")))
def main():
    if len(sys.argv) ==2:
        filename = sys.argv[1]
        if not os.path.isfile(filename):
            print("{}不存在".format(filename))
            exit(0)
        if not os.access(filename,os.R_OK):
            print("{}拒绝访问".format(filename))
            exit(0)
        portlist = [21,22,25,80,110,443,8080]
        for x in range(0,12):
            ip = '192.168.1.'+str(x)
            for port in portlist:
                banner = retbanner(ip,port)
                if banner:
                    print("ip:{0},消息:{1}".format(ip,banner))
                    checkvulns(banner,filename)
    else:
        print(str(sys.argv[0]))
        exit(0)

if __name__=="__main__":
    main()