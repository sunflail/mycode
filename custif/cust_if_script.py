#!/usr/bin/env python3
import time

# Dictionary with phone number choice options
choices = {1: "General",
            2: "Specialist",
            3: "Emergent",
            4: "Safety Violation",
            5: "Operator",
            6: "Nevermind"}

#welcome message
message = "Welcome to the Python Health Alternative Co-op."
print(message)

# If statements pertaining to user input
while True:
    try:
        user_choice = int(input(f"Please select from the following options: \n {choices} \nYour choice: "))
        if choices.get(user_choice):
            break
        else:
            print("\nThat was not a valid option, please try again.\n")

    except:
        print("\nNon number detected. Please try again.")

# cheeky choices for the numbers
if user_choice == 1:
    print(f"\n{choices[1]} help is not available, thank you have a nice day!")
elif user_choice == 2:
    print(f"\n{choices[2]}s are available on the fifth Saturday of every month, please call back then.")
elif user_choice == 3:
    print(f"\nFor {choices[3]} situations, please hang up and dial 9-1-1.")
elif user_choice == 4:
    print(f"\nTo report a local {choices[4]}, please hang up and call your local law enforcement agency.")
elif user_choice == 5:
    print(f"\n{choices[5]}s are standing by to assist you, please stand by.")
    time.sleep(3)
    print("\nWe will be with you shortly.")
    time.sleep(3)
    print("\nPlease think about donating!")
    time.sleep(4)
    print("\nThank you, good bye.")
elif user_choice == 6:
    escape = 0
    while escape < 10:
        input("Would you like to take a survey about our performance? ")
        escape += 1
    print("\nThank you, your 5 star response is appreciated!")


