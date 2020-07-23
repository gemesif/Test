#!/bin/bash

set -x

SCRIPT=/home/gemesif/socket/EchoServerUDP_IPV6.py
PID=/var/run/EchoServerUDP_IPV6.pid
LOG=/var/log/EchoServerUDP_IPV6

case "$1" in 
start)
   $SCRIPT &
   echo $!>/var/run/EchoServerUDP_IPV6.pid
   ;;
stop)
   kill `cat /var/run/EchoServerUDP_IPV6.pid`
   rm /var/run/EchoServerUDP_IPV6.pid
   ;;
restart)
   $0 stop
   $0 start
   ;;
status)
   if [ -e /var/run/EchoServerUDP_IPV6.pid ]; then
      echo EchoServerUDP_IPV6.py is running, pid=`cat /var/run/EchoServerUDP_IPV6.pid`
   else
      echo EchoServerUDP_IPV6.py is NOT running
      exit 1
   fi
   ;;
*)
   echo "Usage: $0 {start|stop|status|restart}"
esac

exit 0 
