#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

animals = ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]
plants = ["carrots", "celery"]

for i in range(len(farms)):
    print(farms[i]["name"])
user_choice = input("\nPlease choose a farm for more info: ")

for i in range(len(farms)):
    if farms[i]["name"] == user_choice:
        print(farms[i]["agriculture"])

animals_only = []
plants_only = []
for i in range(len(farms)):
    if farms[i]["name"] == user_choice:
        for j in (farms[i]["agriculture"]):
            print(j)
            if j in plants:
                plants_only.append(j)
            else:
                animals_only.append(j)
print(animals_only)
