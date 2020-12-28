from termcolor import colored
import string
def equation():
    print(colored("----------------------------------------------------------------", "magenta"))
    print(colored("1 ", "green"), colored(".", "red"), colored("1 dgree", "yellow"))
    print(colored("2 ", "green"), colored(".", "red"), colored("2 degree", "yellow"))
    print(colored("98", "green"), colored(".", "red"), colored("return to home menu", "yellow"))
    print(colored("99", "green"), colored(".", "red"), colored("exit", "yellow"))
    try :
       aq = int(input(colored("""Enter your selected number here
        ==>""", "blue")))
    except :
        print(colored("please select the right number", "red"))
        equation()
    try :
        if aq == 1:
            print(colored("Exemple : ax+b ", "red"))
            b = int(input(colored("Enter b : ", "green")))
            a = int(input(colored("Enter a : ", "green")))
            x = -b/a
            if type(x) == float:
                print(colored("x = " + str(x), "magenta"),colored("or (another form) x = " + str(-b) + "/ "+str(a), "magenta"))
            else:
                print(colored("x = "+str(x),"magenta"))
        elif aq == 2:
            a = int(input(colored("Enter a : ","green")))
            b = int(input(colored("Enter b : ", "green")))
            c = int(input(colored("Enter c : ","green")))
            Delta = b ** 2 - 4 * a * c
            rdelta = Delta**(1/2)
            if type(rdelta)==float:
                rDelta= "√"+str(Delta)
            else:
                rDelta = rdelta
            if Delta == 0:
                x = -b / (2 * a)
                if type(x)==float:
                    print(colored("x = "+str(x),"cyan")," or ",colored("x = "+str(-b)+"/ "+str(2*a),"cyan"))
            elif Delta < 0:
                print("X hasn't solution")
            else:
               x1 = (-b + rdelta) / (2 * a)
               x2 = (-b - rdelta) / (2 * a)
               if type(x1) == float:
                  x1 = str(x1)+" or/or "+"( "+str(-b)+"+"+str(rDelta)+" ) "+"/ "+str(a*2)
               else:
                    x1 = x1
               if type(x2) == float:
                    x2 = str(x2)+" or/or "+"( "+str(-b)+"-"+str(rDelta)+" ) "+"/ "+str(a*2)
               else:
                    x2=x2
               print(colored("x1 = "+x1,"cyan"),"and",colored("x2 = "+x2,"cyan"))


        elif aq == 98:
            eq=1
            return eq
        elif aq == 99:
            exit()
    except:
        print(colored("please select the right number", "red"))
        equation()
