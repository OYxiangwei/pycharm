import zipfile
import optparse
from threading import Thread

def extraallf(zfile,passwords):
    try:
        zfile.extractall(pwd=passwords)
        print("密码是:{0}".format(passwords))
    except Exception as e:
        print(e)

def main():
    parseer = optparse.OptionParser("usage%prog"+"-f <zipfile> -d <dictionary>")
    parseer.add_option("-f",dest="zname",type="string")
    parseer.add_option("-d",dest="dname",type="string")
    (options,args) = parseer.parse_args()
    if (options.zname == None) or (options.dname == None):
        print(parseer.usage)
        exit(0)
    else:
        zname = options.zname
        dname = options.dname
    zfile = zipfile.ZipFile(zname)
    passfile = open(dname,"r")
    for line in passfile.readlines():
        passwords = line.strip("\n")
        t = Thread(target=extraallf,args=(zfile,passwords.encode()))
        t.start()
if __name__=="__main__":
    main()

