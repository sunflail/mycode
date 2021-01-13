#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def main():
        ## Ask user for input
        got_charToLookup = input(f"Pick a number between 1 and 2138 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        ## Decode the response
        got_dj = gotresp.json()
        pprint.pprint(got_dj)

        ## Return the houses affiliated with the char
        houses = got_dj['allegiances']
        for house in houses:
            print(house)
            house_resp = requests.get(house).json()
            pprint.pprint(house_resp['name'])

        ## List of books the character appears in
        books = got_dj['books']
        for book in books:
            book_resp = requests.get(book).json()    
            pprint.pprint(book_resp['name'])

if __name__ == "__main__":
        main()

