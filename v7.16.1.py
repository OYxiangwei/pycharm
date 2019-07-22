import pycrypt

def kpass(cryptpass):
    salt = cryptpass[0:2]
    dictfile = open("pass.txt","r")
    for word in dictfile.readlines():
        word = word.strip("\n")
        cryptword = crypt.crypt(word,salt)
    if cryptpass == cryptword:
        print("找到密码{}".format(word))
        return
    else:
        print("密码没有找到")
        return
def main():
    passfile = open("pass.txt")
    for line in passfile.readlines():
        if ":" in line:
            user = line.split(":")[0]
            cryptpass = line.split(":")[1].strip(" ")
            print("解{}的密码".format(user))
            kpass(cryptpass)
if __name__=="__main__":
    main()