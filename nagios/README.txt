Event handler for reset a Hetzner machine throught the API when is down. 

The script must receive 5 parameters in this order:

- HOSTADDRESS
- HOSTSTATE
- HOSTSTATETYPE
- HOSTATTEMPT
- HOSTNAME

First of all, the script checks the network connectity, for discard a problem in our network. If the script receive a DOWN/SOFT state, it wait for the attempt 15 (5 minutes more or less, depends to your nagios configuration) and launch a soft reset throught the Hetzner API and send us an email If the problem persist, and the script receive a DOWN/SOFT state and the attempt 30 (10 minutes more or less), it launch a hard reset throught the Hetzner API and send us an email If the state changes to DOWN/HARD (reached the max_check_attemps nagios configuration) the script launch a manual reset and send us an email

PRE-REQUISITES: 

python 2.7+ 

sendmail


INSTALLATION 

1.- Configure the reset-hetzner.py script.

username=’’ (Hetzner's username) 

password= ‘’ (Hetzner's password) 

email=’’ (The email the alerts will sent) 

softAttempt=‘15’ (Default value for the soft reset) 

hardAttempt=‘30’ (Default value for the hard reset)


2.- Define a command on nagios configuration: 

define command { 

command_name reset-hetzner command_line $USER1$/reset-hetzner.sh $HOSTADDRESS$ $HOSTSTATE$ $HOSTSTATETYPE$ $HOSTATTEMPT$ $HOSTNAME 

}


3.- Add an event handler to your(s) Hetzner host(s): 

define host { 

address 1.1.1.1 

host_name myhost 

. 

. 

. 

event_handler reset-hetzner 

}

4.- Install the script on the nagios plugin directory ($USER1$)
