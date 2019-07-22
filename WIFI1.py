from scapy.all import *
def pktprint(pkt):
    if pkt.haslayer(DotllBeacon):
        print("detected 802.11 beacon frame")
    elif pkt.haslayer(DotllProbeReq):
        print("detected 802.11 probe request frame")
    elif pkt.haslayer(TCP):
        print("detected a tcp packet")
    elif pkt.haslayer(DNS):
        print("detected a dns packet")
conf.iface = "wlan0mon"
sniff(prn=pktprint)