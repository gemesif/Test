#!/usr/bin/python3

from datetime import datetime
import re
import netifaces
import ipaddress

# *************************************************************************************************************

def myDate():
    pass
    now = datetime.now()
    s1 = now.strftime("%Y%m%d %H%M%S")
    return(s1)

# *************************************************************************************************************

