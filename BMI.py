from termcolor import colored

def bmi():
    print(colored("----------------------------------------------------------------", "magenta"))
    try :
            x = input("Enter your height please (m)(\"inch)('foot):")
            y = input("Enter your weight please (kg)(lbs): ")
            x = x.lower()
            y = y.lower()
            keywordbmih = ["\"", "\'", "m", "\"inch", "\'foot"]
            for i in keywordbmih:
                if i in x:
                    height = x.split(i)[0]
                    height = float(height.strip())
                    unit = i.strip()
                else:
                    continue
            if unit == "m":
                height = height
            elif unit == "\"inch" or unit == "\"":
                height = height * 0.0254
            elif unit == "\'foot" or unit == "\'":
                height = height * 0.3048
            keywordbmiw = ["kg", "lbs"]
            for i in keywordbmiw:
                if i in y:
                    weight = y.split(i)[0]
                    weight = float(weight.strip())
                    unit = i.strip()
                else:
                    continue
            if unit == "kg" or unit =="":
                weight = weight
            elif unit == "lbs":
                weight = weight * 0.45359237
            s=weight/height**2
            print ("     Your BMI is  "+str(s))
            x = height
            y = weight
            if 16<=s<=18.5:
                sa=(21*(x**2))-y
                print("""You are slim :(
                You must add """+str(sa)+"kg")
            elif 18.5<s<24 :
                print(colored("You have normal weight ! :)","green"))
            elif 24<s<=30 :
                sa=y-(25*(x**2))
                print(colored("*************************************************","red"))
                print("You are fat :(","\nYou must Decrease ",sa,"kg (over weight be ware !)")
                print(colored("*************************************************","red"))
            elif 30<s<=35 :
                sa=y-(25*(x**2))
                print(colored("*************************************************","red"))
                print("You are fat :(","\nYou must Decrease ",sa,"kg (over weight degree 1)")
                print(colored("*************************************************","red"))
            elif 35 < s <= 40:
                sa = y - (25 * (x ** 2))
                print(colored("*************************************************","red"))
                print("You are fat :(","\nYou must Decrease ",sa,"kg (over weight degree 2)")
                print(colored("*************************************************","red"))
            elif s<40 :
                sa=y-(25*(x**2))
                print(colored("*************************************************", "red"))
                print("You are fat :(", "\nYou must Decrease ", sa, "kg (over weight degree 4)")
                print(colored("*************************************************", "red"))
            elif int(s)==24 :
                print(colored("You are equiponderant ","yellow"))
    except:
        print(colored("Please enter right values !","red"))
        bmi()