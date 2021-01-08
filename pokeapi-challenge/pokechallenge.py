#!/usr/bin/env python3

# imports always go at the top of your code
import requests
import wget
'''
Change the Pokemon in the URL to a Pokemon of your choice!

Print the URL to "front_default", which is a link to an image of your Pokemon!

Return a count of how many "game_indices" the selected Pokemon has been in!

Print out the "name"s of ALL the selected Pokemon's "moves".
'''

def main():
    print("Welcome to the text version of PokeAPI.")
    user_choice = input('\nWhat pokemon would you like to know more about? ')

    pokeapi = requests.get(f"https://pokeapi.co/api/v2/pokemon/{user_choice}").json()
    pokename = pokeapi['name'].capitalize()

    #front_default pic is under pokeapi['sprites']['front_default']
    download_option = input(f"\nThe front pic can be found here: {pokeapi['sprites']['front_default']} - would you like to download the picture? (y to download) ").strip().lower()
    if download_option == "y":
        url = pokeapi['sprites']['front_default']
        filename = f'{pokename}-front-default.png'
        wget.download(url, out=filename)
        print(f"\nFile saved as {filename}")

    #count of the game_indices
    print(f"\n{pokename} is found in {len(pokeapi['game_indices'])} games!")

    #moves are pokeapi['moves'], list of dictionaries
    for x in pokeapi['moves']:
        move = x['move']['name']
        print(f"\n{pokename} has a move called {move}")
        while True:
            know_more = input(f"Would you like to know more about {move}? (y/n/q)").strip().lower()
            if know_more == "y":
                version = x['version_group_details']
                for detail in version:
                    print(f"In pokemon {detail['version_group']['name']}, {move} is learned at level {detail['level_learned_at']} via {detail['move_learn_method']['name']}.")
                break
            elif know_more == "n":
                break
            elif know_more == "q":
                print("\nThank you for using the PokeAPI, text version!")
                exit(0)

    print("\nThank you for using the PokeAPI, text version!")

if __name__ == "__main__":
    main()
