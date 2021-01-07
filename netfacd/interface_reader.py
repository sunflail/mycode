#!/usr/bin/env python3

import netifaces

print(netifaces.interfaces())

def getIP(adapter):
    return ((netifaces.ifaddresses(adapter)[netifaces.AF_INET])[0]['addr'])

def getMAC(adapter):
    return((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr']) # Prints the MAC address

for i in netifaces.interfaces():
    print('\n****** details of interface - ' + i + ' ******')
    try:
        print('MAC: ', end='') # This print statement will always print MAC without an end of line
        #print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr']) # Prints the MAC address
        print(getMAC(i))
        print('IP: ', end='')  # This print statement will always print IP without an end of line
        #print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr']) # Prints the IP address
        print(getIP(i))
    except:          # This is a new line
        print('Could not collect adapter information') # Print an error message

