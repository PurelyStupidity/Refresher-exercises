"""
You will be given a series of integer numbers that you must add together. Each line will contain one number
between 1 and 100 and the series will be terminated with a #.
Your program must output the sum of all the numbers.
"""
input_list = input("enter your inputs").split()

for i in range(len(input_list)):
    input_list[i] = int(input_list[i])
    if input_list[i] == "#":
        break
    else
    
