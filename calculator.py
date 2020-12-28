import time
from termcolor import colored
from normalcalculator import normalcalculator
from BMI import bmi
from timeconvert import timeconvert
from tallf import tallf
from equation import equation

print(colored("""

 _____         _               _         _                
/  __ \       | |             | |       | |               
| /  \/  __ _ | |  ___  _   _ | |  __ _ | |_   ___   _ __ 
| |     / _` || | / __|| | | || | / _` || __| / _ \ | '__|
| \__/\| (_| || || (__ | |_| || || (_| || |_ | (_) || |   
 \____/ \__,_||_| \___| \__,_||_| \__,_| \__| \___/ |_|   
                                                
""", "red"))
time.sleep(1)
print(colored("Loading ...","blue"))
time.sleep(1)
print(colored("20%","blue"))
time.sleep(1)
print(colored("40%","blue"))
time.sleep(1)
print(colored("60%","blue"))
time.sleep(1)
print(colored("80%","blue"))
time.sleep(2)
print(colored("100%","blue"))
def calculator():
    print(colored("----------------------------------------------------------------", "magenta"))
    print("""Select number form list please :""")
    print(colored("1 ", "green"), colored(".", "red"), colored("Normal calculator", "yellow"))
    print(colored("2 ", "green"), colored(".", "red"), colored("BMI", "yellow"))
    print(colored("3 ", "green"), colored(".", "red"), colored("Time calculator(converter)", "yellow"))
    print(colored("4 ", "green"), colored(".", "red"), colored("Future height calculator", "yellow"))
    print(colored("5 ", "green"), colored(".", "red"), colored("Equation", "yellow"))
    print(colored("99", "green"), colored(".", "red"), colored("exit", "yellow"))

    try:
        a = int(input(colored("""Enter your selected number here please
    ==>""", "blue")))
    except:
        print(colored("please select the right number", "red"))
        calculator()
    print(colored("----------------------------------------------------------------", "magenta"))
    if a == 1:
        t = normalcalculator()
        if t == 1:
            calculator()
        else:
            t = normalcalculator()
            if t == 1:
                calculator()
    elif a == 2:
        bmi()
        calculator()
    elif a == 3:
        timeconvert()
        calculator()
    elif a == 4:
        tallf()
        calculator()
    elif a == 5:
        eq = equation()
        if eq == 1:
            calculator()
        else:
            eq = equation()
            if eq == 1:
                calculator()
    elif a == 99:
        exit()
    else:
        print("please select the right number")


calculator()
