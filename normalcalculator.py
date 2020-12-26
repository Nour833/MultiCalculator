from termcolor import colored

def normalcalculator():
    print(colored("----------------------------------------------------------------","magenta"))
    print(colored("1 ", "green"), colored(".", "red"), colored("Addition", "yellow"))
    print(colored("2 ", "green"), colored(".", "red"), colored("Soustraction", "yellow"))
    print(colored("3 ", "green"), colored(".", "red"), colored("Multiplication", "yellow"))
    print(colored("4 ", "green"), colored(".", "red"), colored("Division", "yellow"))
    print(colored("5 ", "green"), colored(".", "red"), colored("Power", "yellow"))
    print(colored("6 ", "green"), colored(".", "red"), colored("Modulo", "yellow"))
    print(colored("7 ", "green"), colored(".", "red"), colored("remainder", "yellow"))
    print(colored("98", "green"), colored(".", "red"), colored("return to home menu", "yellow"))
    print(colored("99", "green"), colored(".", "red"), colored("exit", "yellow"))
    try :
       b = int(input(colored("""Enter your selected number here
        ==>""", "blue")))
    except :
        print(colored("please select the right number", "red"))
        normalcalculator()
    if b in range(1,8):
        try :
            if b == 1:
                A=int(input("please select number of numbers to somme : "))
                SO = 0
                for i in range(A):
                    h = int(input("Enter Number : "))
                    SO += h
                print("=",colored(SO,"cyan"))
            elif b == 2:
                A = int(input("please select number of numbers to soustract : "))
                B = int(input("First Number : "))
                SO = B
                for i in range(A-1):
                    h = int(input("Enter Number : "))
                    SO -= h
                print("=", colored(SO, "cyan"))
            elif b == 3:
                A = int(input("please select number of numbers to multiply : "))
                SO = 1
                for i in range(A):
                    h = int(input("Enter Number : "))
                    SO *= h
                print("=", colored(SO, "cyan"))
            elif b == 4:
                x = int(input("x = "))
                y = int(input("y = "))
                s = x / y
                print(x, "/", y, "=", s)
            elif b == 5:
                x = int(input("x = "))
                y = int(input("power = "))
                s = x ** y
                print(x, "^", y, "=", s)
            elif b == 6:
                s = x % y
                print("the rest of ", x, "/", y, "is ", s)
            elif b == 7:
                s = x // y
                print(x, "/", y, "=", s, " without the rest")
        except:
            print(colored("please select the right number", "red"))
            normalcalculator()


    elif b == 98:
        t=1
        return t
    elif b == 99:
        exit()
    else:
        print(colored("please select the right number","red"))
        normalcalculator()