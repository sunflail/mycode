#!/usr/bin/env python3
""" Author: RZFeeser || Alta3 Research
Gather data returned by various APIs published on OMDB, and cache in a local SQLite DB
"""

import json
import sqlite3
import requests

# Define the base URL
OMDBURL = "http://www.omdbapi.com/?"

# search for all movies containing string
def movielookup(mykey, searchstring, option, extra):
    """Interactions with OMDB API
       mykey = omdb api key
       searchstring = string to search for"""
    try:
        # begin constructing API
        api = f"{OMDBURL}apikey={mykey}&s={searchstring}"
        if option == 1:
            ## open URL to return 200 response
            resp = requests.get(api)
        else:
            resp = requests.get(f"{api}&{extra}")
        ## read the file-like object decode JSON to Python data structure
        return resp.json()
    except:
        return False

def trackmeplease(datatotrack):
    conn = sqlite3.connect('mymovie.db')
    try:
        conn.execute('''CREATE TABLE IF NOT EXISTS MOVIES (TITLE TEXT PRIMARY KEY NOT NULL, YEAR INT  NOT NULL);''')

        # loop through the list of movies that was passed in
        for data in datatotrack:
            # in the line below, the ? are examples of "bind vars"
            # this is best practice, and prevents sql injection attacks
            # never ever use f-strings or concatenate (+) to build your executions
            conn.execute("INSERT INTO MOVIES (TITLE,YEAR) VALUES (?,?)",(data.get("Title"), data.get("Year")))
            conn.commit()

        print("Database operation done")
        conn.close()
        return True
    except:
        return False

# Read in API key for OMDB
def harvestkey():
    with open("/home/student/omdb.key") as apikeyfile:
        return apikeyfile.read().rstrip("\n") # grab the api key out of omdb.key

def printlocaldb():
    conn = sqlite3.connect('mymovie.db')
    try:
        cursor = conn.execute("SELECT * from MOVIES")
        for row in cursor:
            print("MOVIE = ", row[0])
            print("YEAR = ", row[1])
        conn.close()
        return True
    except:
        return False

def main():

    # read the API key out of a file in the home directory
    mykey = harvestkey()

    # enter a loop condition with menu prompting
    while True:
        # initialize answer
        answer = ""
        while answer == "":
            print("""\n**** Welcome to the OMDB Movie Client and DB ****
            ** Returned data will be written into the local database **
            1) Search for All Movies Containing String
            2) Search for Movies Containing String, and by Type
            3) Search for string and by year of release
            4) Search for string by year of release and type
            5) Display local database of search results
            99) Exit""")

            answer = input("> ") # collect an answer for testing

        # testing the answer
        if answer in ["1", "2", "3", "4"]:
            # All searches require a string to include in the search
            searchstring = input("Search all movies in the OMDB. Enter search string: ")
            option = int(answer)
            extra = ""
            if answer == "1":
                resp = movielookup(mykey, searchstring, option, extra)
            elif answer == "2":
                reqType = input("Add the type to search for(movie, series, episode): ")
                extra = f"&type={reqType}"
                resp = movielookup(mykey, searchstring, option, extra)
            elif answer == "3":
                reqYear = input("Add year of release: ")
                extra = f"&y={reqYear}"
                resp = movielookup(mykey, searchstring, option, extra)
            elif answer == "4":
                reqType = input("Add the type to search for(movie, series, episode): ")
                reqYear = input("Add year of release: ")
                extra = f"&type={reqType}&y={reqYear}"
                resp = movielookup(mykey, searchstring, option, extra)
            if resp:
                # display the results
                resp = resp.get("Search")
                print(resp)
                # write the results into the database
                trackmeplease(resp)
            else:
                print("That search did not return any results.")
        elif answer == "5":
            printlocaldb()
        # user wants to exit
        elif answer == "99":
            print("See you next time!")
            break

if __name__ == "__main__":
    main()
