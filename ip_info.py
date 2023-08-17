import ipinfo
import sys
green = "\33[0;32m" #green

try:
  ip_address = sys.argv[1]
except IndexError:
  ip_address = None
  
access_token = ("d519c063eb21ef")

handler = ipinfo.getHandler(access_token)
details = handler.getDetails(ip_address )
for key,value in details.all.items():
 print(green+f"{key}:{value}")