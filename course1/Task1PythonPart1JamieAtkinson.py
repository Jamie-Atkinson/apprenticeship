"""
Task1 Part 1

collect data and allow choices from menu

Jamie Atkinson

2018-09-07
"""
import numpy as np
from statistics import mode
#prompt user to input numbers until done is typed
def collect_numbers():
    data= []
    while True:
        user_input=raw_input("please enter a number, if you have finished entering numbers please type done: ")
        if user_input== 'done':
            break
        else:
            data.append(int(user_input))
    print('\n\ncount of numbers entered is: '+str(len(data)))
    return(data)
while True:
    while True:
        inputed_data=[]
        inputed_data= inputed_data+ (collect_numbers())
        print('\n\nPlease select one of the following options:\n1. Print the mean of the numbers\n2. print the median of the numbers\n3. Print the mode of the numbers\n4. Go back and enter a NEW set of numbers\n5. Exit the application')
        menu_selection = input("Selection: ")
        if menu_selection==1:
            print(np.mean(inputed_data))
            exit()
        elif menu_selection==2:
            print(np.median(inputed_data))
            exit()
        elif menu_selection==3:
            print(mode(inputed_data))
            exit()
        elif menu_selection==4:
            break
        elif menu_selection==5:
            exit()

