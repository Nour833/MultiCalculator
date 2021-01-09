from termcolor import colored

def tallf():
    h = int(input("""
         1.Girl
         2.Boy
         ==>"""))
    try:
        if h == 1:
            x = float(input("Enter your father height please(cm) : "))
            y = float(input("Enter your mother height please (cm): "))
            s = ((x - 13) + y) / 2
            print("Your future height will be : " + str(s) + "cm")
        elif h == 2:
            x = float(input("Enter your father height please(cm) : "))
            y = float(input("Enter your mother height please (cm): "))
            s = ((x + 13) + y) / 2
            print("Your future height will be : " + str(s) + "cm")
    except:
        print(colored("please select the right number", "red"))
        tallf()
