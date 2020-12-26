from termcolor import colored
import string
def equation():
    print(colored("----------------------------------------------------------------", "magenta"))
    print(colored("1 ", "green"), colored(".", "red"), colored("1 dgree", "yellow"))
    print(colored("2 ", "green"), colored(".", "red"), colored("2 degree", "yellow"))
    print(colored("3 ", "green"), colored(".", "red"), colored("3 degree", "yellow"))
    print(colored("4 ", "green"), colored(".", "red"), colored("4 degree", "yellow"))
    print(colored("98", "green"), colored(".", "red"), colored("return to home menu", "yellow"))
    print(colored("99", "green"), colored(".", "red"), colored("exit", "yellow"))
    try :
       aq = int(input(colored("""Enter your selected number here
        ==>""", "blue")))
    except :
        print(colored("please select the right number", "red"))
        equation()
    if aq == 1:
        x=input(colored("Enter the equation :","yellow"))
        x=x.lower()
        print(x)
        print(string.punctuation)
        lst=x.split(string.punctuation)
        print(lst)
        for i in lst:
            if "x" in i:
                b = i.split("x")
                b=b[0]
                bx=b+"x"
                xb="x"+b
            else:
                continue
        if bx in x:
            others = x.split(bx)
        elif xb in x:
            others = x.split(xb)
        print(others)
    elif aq == 98:
        eq=1
        return eq
    elif aq == 99:
        exit()