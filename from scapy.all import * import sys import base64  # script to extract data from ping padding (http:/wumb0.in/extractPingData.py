#credit to http://wumb0.in

from scapy.all import *
import sys
import base64

# script to extract data from ping padding (http://wumb0.in/ping-exfil.html)

try:
    config.conf.iface = sys.argv[2]
except: pass

s = sniff(lfilter=lambda x: x.haslayer(ICMP) and x[ICMP].type==8, stop_filter=lambda x: x.haslayer(ICMP) and x[ICMP].type==8 and '\n' in x[ICMP][Raw].load[8:24])

buf = ""
for i in s:
    buf += i[ICMP][Raw].load[8:24]

with open(sys.argv[1], "w") as f:
    f.write(base64.b64decode(buf[:buf.find('\n')]))
