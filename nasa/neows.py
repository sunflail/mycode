#!/usr/bin/python3
import requests

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# this function grabs our credentials
# it is easily recycled from our previous script
def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()

    ## update the date below, if you like
    # challenge 1 - accept input
    startdate = input("start_date(YYYY-MM-DD)=")
    startdate = "start_date=" + startdate

    enddate = input("end_date(YYYY-MM-DD)=")
    if enddate:
        enddate = "end_date=" + enddate

    if enddate:
        dateRange = startdate + "&" + enddate
        print(dateRange)
    else:
        dateRange = startdate

    # make a request with the request library
    neowrequest = requests.get(NEOURL + dateRange + "&" + nasacreds)

    # strip off json attachment from our response
    neodata = neowrequest.json()

    ## display NASAs NEOW data
    print(neodata)

if __name__ == "__main__":
    main()
