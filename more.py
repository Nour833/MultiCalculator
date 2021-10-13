from termcolor import colored


def more():
    while True:
        print(colored("\n----------------------------------------------------------------", "magenta"))
        print(colored("1 ", "green"), colored(".", "red"), colored("GCD", "yellow"))
        print(colored("2 ", "green"), colored(".", "red"), colored("LCM", "yellow"))
        print(colored("3 ", "green"), colored(".", "red"), colored("IF", "yellow"))
        print(colored("98", "green"), colored(".", "red"), colored("return to home menu", "yellow"))
        print(colored("99", "green"), colored(".", "red"), colored("exit", "yellow"))
        try:
            x = int(input(colored("Enter your input here please -----> ", 'blue')))
            if x in [1, 2, 3, 98, 99]:
                break
            else:
                raise Exception
        except:
            print(colored("please select the right number", "red"))

    if x == 1 or x == 2:
        while True:
            try:
                a = int(input(colored("Please enter your first number : ", "green")))
                b = int(input(colored("Please enter your second number : ", "green")))
                break
            except:
                print(colored("please select the right number", "red"))
        if x == 1:
            gcd = 0
            for i in range(1, b + 1)[::-1]:
                if b % i == 0 and a % i == 0:
                    gcd = i
                    break
            print(colored(str(gcd) + " is the GCD", "blue"))
        else:
            i = 1
            if b < a:
                a, b = b, a
            while True:
                A = a * i
                B = b
                while A > B:
                    B += B
                if B == A:
                    break
                i += 1
            print(colored(str(a * i) + " is the LCM", "blue"))
    elif x == 3:
        while True:
            try:
                a = int(input(colored("Please enter a number : ", "green")))
                break
            except:
                print(colored("please select the right number", "red"))
        A = a
        list = []
        for i in range(1, a + 1)[::-1]:
            is_prime = 0
            for y in range(1, i + 1):
                if i % y == 0: is_prime += 1
            if is_prime <= 2 and a % i == 0:
                list.append(i)
                a = a / i
        print(colored(str(A), 'blue') + " = " + colored(str(list[0]), 'blue'), end='')
        for i in list[1:]:
            print(" * ", end=colored(i, 'blue'))
    elif x == 98:
        eq = 1
        return eq
    elif x == 99:
        exit()
