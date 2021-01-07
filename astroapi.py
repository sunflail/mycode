#!/usr/bin/env python3

import requests

def main():
    '''Run time code'''

    r = requests.get('http://api.open-notify.org/astros.json')

    # output should look like this
    # People in space: 3
    # Chris Cassidy on the ISS
    # Anatoly Ivanishin on the ISS
    # Ivan Vagner on the ISS
    # update from the api, loop over json, return all members on the ISS

    # number of people on the station is at key "number"
    number_on_ISS = r.json().get('number')
    print(f'People in space: {number_on_ISS}')

    # get people information - r.json.get('people')['craft] and ['name']
    for person in r.json().get('people'):
        print(f'{person["name"]} on the {person["craft"]}')


if __name__ == '__main__':
    main()
