#!/usr/bin/python3

import requests

TIMEURL = "http://date.jsontest.com"
IPURL = "http://ip.jsontest.com"
VALIDURL = "http://validate.jsontest.com"

def main():
    ## A - pull time
    resp = requests.get(TIMEURL)
    mytime = resp.json()
    print(mytime)
    mytime = mytime["time"]
    print(mytime)

    ## B - pull ip
    resp = requests.get(IPURL)
    myip = resp.json()
    print(myip)
    myip = myip["ip"]

    ## C - read list of servers from myservers.txt
    with open("./jsontest/myservers.txt") as f:
        myservers = f.readlines()
        print(myservers)

    ## D - format as  {"json": "time: <<PART A>>, ip: <<PARTB>>, mysvrs: [ <<PARTC>> ]"}
    jsonInfo = {
        "time": mytime,
        "ip":myip,
        "myservers" :myservers
    }

    jsonReq = {
        "json": str(jsonInfo)
    }
    print(jsonInfo)
    print(jsonReq)
    ## E - validate json with POST
    resp = requests.post(VALIDURL, data=jsonReq)
    respjson = resp.json()
    print(respjson)
if __name__ == "__main__":
    main()