#!/usr/bin/env python3
"""Alta3 Research
   Star Wars API HTTP response parsing"""

# pprint makes dictionaries a lot more human readable
from pprint import pprint

# requests is used to send HTTP requests (get it?)
import requests

# URL = "https://swapi.dev/luke/force"      # Comment out this line
charURL= "https://swapi.dev/api/people/4/"     # Uncomment this line

def main():
    """sending GET request, checking response"""

    # SWAPI response is stored in "resp" object
    char= requests.get(charURL)

    # check to see if the status is anything other than what we want, a 200 OK
    if char.status_code == 200:
        # convert the JSON content of the response into a python dictionary
        vader= char.json()
        films= vader["films"]
        first_film = requests.get(films[0]).json()
        ships= vader["starships"]
        ship = requests.get(ships[0]).json()

        pprint(vader)
        print(f'{vader["name"]} was born in the year {vader["birth_year"]}. His eyes are now {vader["eye_color"]} and his hair color is {vader["hair_color"]}.')
        print(f'He first appeared in the movie {first_film["title"]} and could be found flying around in his {ship["name"]}.')

    else:
        print("That is not a valid URL.")

if __name__ == "__main__":
    main()
