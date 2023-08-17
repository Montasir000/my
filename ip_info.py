import ipinfo
import sys
black="\033[0;30m"        # Black
red="\033[0;31m"          # Red
green="\033[0;32m"        # Green
yellow="\033[0;33m"       # Yellow
blue="\033[0;34m"         # Blue
purple="\033[0;35m"       # Purple
cyan="\033[0;36m"         # Cyan
white="\033[0;37m"        # white

try:
  ip_address = sys.argv[1]
except IndexError:
  ip_address = None
  
access_token = ("d519c063eb21ef")

handler = ipinfo.getHandler(access_token)
details = handler.getDetails(ip_address )
for key,value in details.all.items():
 print(cyan+f"{key}:{value}")