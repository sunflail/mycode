#!/usr/bin/python3

# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # counter for fails
falsefail = 0 # counter for false fail flags

# open the file for reading
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:

    # loop over the file
    ip = ""
    for line in kfile:
        # if this 'fail pattern' appears in the line...
        if "- - - - -] Authorization failed" in line:
            loginfail += 1 # this is the same as loginfail = loginfail + 1
            print("Failed login from: " + line.split(" ")[-1].rstrip("\n"))
        elif "-] Authorization failed" in line:
            falsefail +=1

print("The number of failed log in attempts is", loginfail)
print("The number of false flag successful logins is", falsefail)

