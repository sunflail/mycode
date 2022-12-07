#!/usr/bin/python3

import time
import requests

URI = "http://localhost:2224/"

def main():
    start = time.time()
    count = 0
    #lookup 50 times, the 51st will fail from the limiter
    while True:
        print(count)
        r = requests.get(f'{URI}fast')
        count += 1
        if r.status_code != 200:
            count += 1
            end = time.time()
            break

    print(f"Calling localhost/fast with a limit of 50/hour, ran from {start} until {end} and took {end - start} seconds")

if __name__ == "__main__":
    main()