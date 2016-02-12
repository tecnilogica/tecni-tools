#!/usr/bin/python
import sys, commands, os


def main():
     global ip, state, stateType, attempt, name, output, network, email
     global expectedAttempt, user, password

     # Own configuration
     user = ''
     password = ''
     email = ''
     softAttempt = '15'
     hardAttempt = '30'

     # Parameters from nagios
     ip = str(sys.argv[1])
     state = str(sys.argv[2])
     stateType = str(sys.argv[3])
     attempt = str(sys.argv[4])
     name = str(sys.argv[5])
     network = checkNetwork()
 
     # If state is down, type is SOFT and reached softAttempt (default 15), the host is 5 minutes down, soft reset 
     if network == ' 0% packet loss':
     	if state == 'DOWN':
            if stateType == "SOFT":
            	if attempt == softAttempt:
                    soft()
     # If state is down, type is SOFT and reached hardAttempt (default 30), the host is 10 minutes down, hard reset
     if network == ' 0% packet loss':
        if state == 'DOWN':
            if stateType == "SOFT":
                if attempt == hardAttempt:
                    hard()
     # If state is down and type is HARD	
     if network == ' 0% packet loss':
     	if state == 'DOWN':
            if stateType == "HARD":
                manual()
  
def soft():
    print ("Soft reset for: "+ name)
    reset("soft", name)
 
def hard():
    print ("Hard reset for: " + name)
    reset("hard", name)
 
def manual():
    print ("Manual reset for: " + name)
    reset("manual", name)

def checkNetwork():
   output = commands.getoutput('ping -q -c 2 google.com | grep packets | cut -f 3 -d","')
   return output


def reset(typ, name):
   if typ == "soft":
	reset = "sw"
   elif typ == "hard":
	reset = "hw"
   elif typ == "manual":
        reset = "man"

   os.system('curl -u %s:%s https://robot-ws.your-server.de/reset/%s -d type=%s' % (user, password, ip, reset))
   os.system('echo  ""  | mail -s "%s reset for %s" "%s"' % (typ, name, email))



if __name__ == '__main__':
  main()
