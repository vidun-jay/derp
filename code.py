#!/usr/bin/env python3
import random
from os import system, name


# Make a class of colors to call later
class colors:
    red = '\033[1;31;1m'
    green = '\033[1;32;1m'
    cyan = '\033[0;36;1m'
    end = '\033[0m'

# Defines a clear() function that replicates cleared screen after y/n selection
def clear():
        #  for windows
    if name == 'nt':
        l = system('cls')

    #  for mac and linux(here, os.name is 'posix')
    else:
        l = system('clear')

clear()

# Displays the DERP title
print(colors.cyan + r"""
██████╗    ███████╗   ██████╗    ██████╗ 3.0
██╔══██╗   ██╔════╝   ██╔══██╗   ██╔══██╗
██║  ██║   █████╗     ██████╔╝   ██████╔╝
██║  ██║   ██╔══╝     ██╔══██╗   ██╔═══╝ 
██████╔╝██╗███████╗██╗██║  ██║██╗██║██╗  
╚═════╝ ╚═╝╚══════╝╚═╝╚═╝  ╚═╝╚═╝╚═╝╚═╝""" + colors.end)
# Displays subtext and prompts user for continue
print("Decision & Evaluation Review Protocol")
print(colors.red + 'Copyright © 2020 Vidun Jayakody. All rights reserved.\n' + colors.end)
print("\n")
print('*Following the recent tragedy of Vidun wiping his hard drive, D.E.R.P. has death\n')
print("*From it's ashes was born the new and improved D.E.R.P. written in Python 3!\n")
print("*Enjoy all of D.E.R.P.'s original features, PLUS \nbrand new DERP title, and" + colors.cyan + " fancy" + colors.green + " new" + colors.red + " colors!" + colors.end + "\n")
# Sets checkpoint for if user does not input valid y/n value
while True:
    answer = input(colors.green + 'Would you like to continue? (y/n) ' + colors.end)

# If user inputs y continue with derp script
    if answer == "y" or answer == "Y":
        #  !/usr/bin/env python

        class colors:
            red = '\033[1;31;1m'
            green = '\033[1;32;1m'
            cyan = '\033[0;36;1m'
            end = '\033[0m'

# Clears screen
        clear()

# 
        print(colors.cyan + r"""
██████╗    ███████╗   ██████╗    ██████╗ 3.0
██╔══██╗   ██╔════╝   ██╔══██╗   ██╔══██╗   
██║  ██║   █████╗     ██████╔╝   ██████╔╝
██║  ██║   ██╔══╝     ██╔══██╗   ██╔═══╝ 
██████╔╝██╗███████╗██╗██║  ██║██╗██║██╗  
╚═════╝ ╚═╝╚══════╝╚═╝╚═╝  ╚═╝╚═╝╚═╝╚═╝""" + colors.end)
        print("Decision & Evaluation Review Protocol")
        print(colors.red + 'Copyright © 2020 Vidun Jayakody. All rights reserved.\n' + colors.end)
        print("\n")
#  Sets it to reset after question is asked
        while True:
            q = input('Question: Should I ')
            if " or " not in q:
                #  Generates random integer between 0 and 1
                i = random.randint(0, 1)
                #  If the number is 0, display yes you should
                if i == 0 and ' or ' not in q:
                    print(colors.green + 'Answer: Yes you should.' + colors.end)

                #  If the number is 1, display no you shouldn't
                if i == 1 and ' or ' not in q:
                    print(colors.red + 'Answer: No you should not.' + colors.end)

            # If the string contains the word or
            elif " or " in q:
                # Split the phrase into words and make a list
                i1 = random.randint(0,1)
                y = q.split(" ")
                m = y.index('or')
                list = []
                # Add the word before and after 'or' into list called list ^
                list.append(y[m + 1])
                list.append(y[m - 1])
                print(colors.green + 'Answer: ' + list[i1] + colors.end)

    # If user selects n, quit the script
    if answer == "n" or answer == 'N':
        exit()

    # If the user inputs something other than y/n (capitilization inclusive), then prompt them to enter a valid selection
    if answer != 'y' or answer != 'Y' and answer != 'n' or answer != 'N':
        print(colors.red + 'Please enter "y" or "n"!' + colors.end)
