from termcolor import colored

def unit():
    print(colored("----------------------------------------------------------------","magenta"))
    print(colored("1 ", "green"), colored(".", "red"), colored("Height", "yellow"))
    print(colored("2 ", "green"), colored(".", "red"), colored("Weight", "yellow"))
    print(colored("3 ", "green"), colored(".", "red"), colored("Temperature", "yellow"))
    print(colored("98", "green"), colored(".", "red"), colored("Return To Home Menu", "yellow"))
    print(colored("99", "green"), colored(".", "red"), colored("Exit", "yellow"))
    try:
        a = int(input(colored("==>","blue")))
    except:
        print(colored("please select the right number", "red"))
        unit()
    if a == 1:
        print(colored("Please use unit from this box : ","red"))
        print(colored("""[mm(millimeter), cm(centimeter), dm(decameter), 
        meter( not m !), dcm(decameter), hm(hectometer), km(kilometer), mile,inch(\" , \"inch), foot(\' , \'foot)]""","cyan"))
        keywords = ["\"", "\'", "\"inch", "\'foot","millimeter","km","mile","centimeter","cm","meter","mm","dm","decimeter","dcm","decameter","kilometer","hectometer","hm"]
        data = input(colored("Please enter number to convert (with unit): "))
        data = data.lower()
        toconvert = input(colored("Please enter unit to convert to : "))
        toconvert = toconvert.lower()
        def datatest():
            for i in keywords:
                if i in data:
                    return 1
                else:
                    continue
        hh = datatest()
        if hh == 1 :
            pass
        else :
            print(colored("Enter right number !", "red"))
            unit()
        def contest():
            for i in keywords:
                if i in toconvert:
                    return 1
                else:
                    continue
        hhh = contest()
        if hhh == 1:
            pass
        else:
            print(colored("Enter right number !", "red"))
            unit()
        def ffun():
            if ("mm" or "millimeter") in data:
                if "mm" in data:
                    numl = data.split("mm")
                    num=numl[0]
                else:
                    numl = data.split("millimeter")
                    num = numl[0]
                num = float(num) * 0.001
            elif ("cm" or "centimeter") in data:
                if "cm" in data:
                    numl = data.split("cm")
                    num = numl[0]
                else:
                    numl = data.split("centimeter")
                    num = numl[0]
                num = float(num) * 0.01
            elif ("dm" or "decimeter") in data:
                if "dm" in data:
                    numl = data.split("dm")
                    num=numl[0]
                else:
                    numl = data.split("decimeter")
                    num = numl[0]
                num = float(num) * 0.1
            elif "meter" in data:
                    numl = data.split("meter")
                    num = numl[0]
                    num = float(num)
            elif ("dcm" or "decameter") in data:
                if "mm" in data:
                    numl = data.split("dcm")
                    num=numl[0]
                else:
                    numl = data.split("decameter")
                    num = numl[0]
                num = float(num) * 10
            elif ("hm" or "hectometer") in data:
                if "mm" in data:
                    numl = data.split("hm")
                    num=numl[0]
                else:
                    numl = data.split("hectometer")
                    num = numl[0]
                num = float(num) * 100
            elif ("km" or "kilometer") in data:
                if "km" in data:
                    numl = data.split("km")
                    num=numl[0]
                else:
                    numl = data.split("kilometer")
                    num = numl[0]
                print(num)
                num = float(num) * 1000
            elif ("inch" or "\"" or "\"inch") in data:
                if "inch" in data:
                    numl = data.split("inch")
                    num=numl[0]
                elif "\"inch" in data:
                    numl = data.split("\"inch")
                    num = numl[0]
                else:
                    numl = data.split("\"")
                    num = numl[0]
                num = float(num) * 0.0254
            elif ("foot" or "\'" or "\'foot") in data:
                if "foot" in data:
                    numl = data.split("foot")
                    num=numl[0]
                elif "\'foot" in data:
                    numl = data.split("\'foot")
                    num = numl[0]
                else:
                    numl = data.split("\'")
                    num = numl[0]
                num = float(num) * 0.3048
            elif "mile" in data:
                numl = data.split("mile")
                num = numl[0]
                num = float(num) * 1609.34
            else:
                print(colored("Enter right number !", "red"))
                unit()
            return num
        def sfun(num):
            if ("mm" or "millimeter") in toconvert:
                numn = num * 1000
            elif ("cm" or "centimeter") in toconvert:
                numn = num * 100
            elif ("dm" or "decimeter") in toconvert:
                numn = num * 10
            elif  "meter" in toconvert:
                numn = num
            elif ("dcm" or "decameter") in toconvert:
                numn = num * 0.1
            elif ("hm" or "hectometer") in toconvert:
                numn = num * 0.01
            elif ("km" or "kilometer") in toconvert:
                numn = num * 0.001
            elif ("mile") in toconvert:
                numn = num * 0.000621371192
            elif ("inch" or "\"" or "\"inch") in toconvert:
                numn = num * 39.3700787
            elif ("foot" or "\'" or "\'foot") in toconvert:
                numn = num * 3.2808399
            return numn
        try:
            num = ffun()
            numn = sfun(num)
        except:
            print(colored("please select the right number", "red"))
            unit()
        print(colored(str(data)+" = "+str(numn)+" "+toconvert,"green"))
    if a == 2:
        print(colored("Please use unit from this box : ","red"))
        print(colored("""[mg(milligram), cg(centigram), dg(decagram), 
        gram( not g !), dcg(decagram), hg(hectogram), kg(kilogram), quintal, ton, pound(lb or lbs)]""","cyan"))
        keywordz = ["pound","lb","kg","centigram","cg","gram","mg","milligram","dg"," decigram","dcg","decagram","kilogram","hectogram","hg","quintal","ton"]
        data = input(colored("Please enter number to convert (with unit): "))
        data = data.lower()
        oconvert = input(colored("Please enter unit to convert to : "))
        oconvert = oconvert.lower()
        def datatest():
            for i in keywordz:
                if i in data:
                    return 1
                else:
                    continue
        hh = datatest()
        if hh == 1 :
            pass
        else :
            print(colored("Enter right number !", "red"))
            unit()
        def contest():
            for i in keywordz:
                if i in oconvert:
                    return 1
                else:
                    continue
        hhh = contest()
        if hhh == 1:
            pass
        else:
            print(colored("Enter right number !", "red"))
            unit()
        def gfun(data,oconvert):
            if ("mg" or "milligram") in data:
                if "mg" in data:
                    numl = data.split("mg")
                    num=numl[0]
                else:
                    numl = data.split("milligram")
                    num = numl[0]
                num = float(num) * 0.001
            elif ("cg" or "centigram") in data:
                if "cm" in data:
                    numl = data.split("cg")
                    num = numl[0]
                else:
                    numl = data.split("centigram")
                    num = numl[0]
                num = float(num) * 0.01
            elif ("dg" or "decigram") in data:
                if "dg" in data:
                    numl = data.split("dg")
                    num=numl[0]
                else:
                    numl = data.split("decigram")
                    num = numl[0]
                num = float(num) * 0.1
            elif "gram" in data:
                    numl = data.split("gram")
                    num = numl[0]
                    num = float(num)
            elif ("dcg" or "decagram") in data:
                if "mg" in data:
                    numl = data.split("dcg")
                    num=numl[0]
                else:
                    numl = data.split("decagram")
                    num = numl[0]
                num = float(num) * 10
            elif ("hg" or "hectogram") in data:
                if "mg" in data:
                    numl = data.split("hg")
                    num=numl[0]
                else:
                    numl = data.split("hectogram")
                    num = numl[0]
                num = float(num) * 100
            elif ("kg" or "kilogram") in data:
                if "kg" in data:
                    numl = data.split("kg")
                    num=numl[0]
                else:
                    numl = data.split("kilogram")
                    num = numl[0]
                num = float(num) * 1000
            elif "quintal" in data:
                numl = data.split("quintal")
                num = numl[0]
                num = float(num) * 100000
            elif "ton" in data:
                numl = data.split("ton")
                num = numl[0]
                num = float(num) * 1000000
            elif ("pound" or "lb") in data:
                if "lb" in data:
                    numl = data.split("lb")
                    num = numl[0]
                elif "lbs" in data:
                    numl = data.split("lbs")
                    num = numl[0]
                else:
                    numl = data.split("pound")
                    num = numl[0]
                num = float(num) * 453.59237
            else:
                print(colored("Enter right number !", "red"))
                unit()
            return num
        def sfun(num,oconvert):
            if ("mg" or "milligram") in oconvert:
                numn = num * 1000
            elif ("cg" or "centigram") in oconvert:
                numn = num * 100
            elif ("dg" or "decigram") in oconvert:
                numn = num * 10
            elif  "gram" in oconvert:
                numn = num
            elif ("dcg" or "decagram") in oconvert:
                numn = num * 0.1
            elif ("hg" or "hectogram") in oconvert:
                numn = num * 0.01
            elif ("kg" or "kilogram") in oconvert:
                numn = num * 0.001
            elif "quintal" in oconvert:
                numn = num * 0.00001
            elif "ton" in oconvert:
                numn = num * 0.000001
            elif ("pound" or "lb") in oconvert:
                numn = num * 0.00220462262
            return numn
        try:
            num = gfun(data,oconvert)
            numn = sfun(num,oconvert)
        except:
            print(colored("please select the right number", "red"))
            unit()
        print(colored(str(data)+" = "+str(numn)+" "+oconvert,"green"))
    elif a == 3:
        print(colored("1 ", "green"), colored(".", "red"), colored("C to F", "yellow"))
        print(colored("2 ", "green"), colored(".", "red"), colored("F to C", "yellow"))
        try:
            cc = int(input(colored("==>", "blue")))
        except:
            print(colored("please select the right number", "red"))
            unit()
        try:
            if cc == 1:
                c = float(input(colored("Please enter value : ","cyan")))
                c2f = (c * 1.8)+32
                print(colored(str(c)+" °C = "+str(c2f)+" °F","green"))
            elif cc == 2:
                f = float(input(colored("Please enter value : ","cyan")))
                f2c = (f/32)*5556
                print(colored(str(f)+" °F = "+str(f2c)+" °C","green"))
        except:
            print(colored("please select the right number", "red"))
            unit()
    elif a == 98:
        t = 1
        return t
    elif a == 99:
        exit()
    else:
        print(colored("please select the right number", "red"))
        unit()


