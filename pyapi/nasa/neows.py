#!/usr/bin/python3
import requests
import datetime
## Define NEOW URL 
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

def main():
    ## grab start date from input
    startdate = input('Please enter your start date(YYYY-MM-DD): ')
    ## turn input into datetime object, add 7 days to it, and turn into properly formatted enddate (no access to isoformat() and fromisoformat() until python 3.7+
    start_date = datetime.datetime.strptime(startdate, "%Y-%m-%d")
    end = start_date + datetime.timedelta(days=7)
    enddate = end.date().strftime("%Y-%m-%d")

    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")        

    # make a request with the request library
    print(f'{NEOURL}start_date={startdate}&end_date={enddate}&{nasacreds}')
    neowrequest = requests.get(f'{NEOURL}start_date={startdate}&end_date={enddate}&{nasacreds}')
    # strip off json attachment from our response
    neodata = neowrequest.json()

    ## display NASAs NEOW data
    print(type(neodata['near_earth_objects']))

    #loop over and create a list of the asteroid sizes in the range
    sizes = []
    hazards = []
    for day in neodata['near_earth_objects']:
        for x in neodata['near_earth_objects'][day]:
            sizes.append(x['estimated_diameter']['kilometers']['estimated_diameter_max'])
            if x['is_potentially_hazardous_asteroid']:
                hazards.append(f"{x['name']} on {day}")

    print(f'The biggest NEO was {max(sizes)} in kilometers wide.')
    print(f'{len(hazards)} potentially hazardous asteroids included:\n{hazards}.')

if __name__ == "__main__":
    main()

