#!/usr/bin/env python3
#list of 3 items
my_list = [ "192.168.0.5", 5060, "UP" ]
#show the 1st item
print("The first item in the list (IP): " + my_list[0] )
#show the 2nd item
print("The second item in the list (port): " + str(my_list[1]) )
#shot the 3rd item
print("The last item in the list (state): " + my_list[2] )

new_list = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

print(f"When I {new_list[-1]} into IP addresses {new_list[3]} or {new_list[4]} I am unable to ping ports {new_list[0]}, {new_list[1]}, or {new_list[2]}.")

