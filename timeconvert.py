from termcolor import colored

def timeconvert():
    print(colored("----------------------------------------------------------------","magenta"))
    try:
        TS = int(input("Enter number second:"))
        h = TS // 3600
        m = (TS % 3600)//60
        s = (TS % 3600)%60
        c = h//(24*30*12*100)
        y = (h%(24*30*12*100))//(24*12*30)
        M = ((h%(24*30*12*100))%(24*12*30))//(24*30)
        d = (((h%(24*30*12*100))%(24*12*30))%(24*30))//24
        h = (((h%(24*30*12*100))%(24*12*30))%(24*30))%24
        lst = [c,y,M,d,h,m,s]
        nlst =[]
        for i in lst:
            if i == 0:
                continue
            else :
                nlst.append(str(i))
                ind=lst.index(i)
                if ind == 0:
                    inde = "c"
                elif ind == 1:
                    inde = "y"
                elif ind == 2:
                    inde = "M"
                elif ind == 3:
                    inde = "d"
                elif ind == 4:
                    inde = "h"
                elif ind == 5:
                    inde = "m"
                elif ind == 6 :
                    inde = "s"
                nlst.append(inde)
        string = " ".join(nlst)
        print(string)
    except:
        print(colored("please select the right number", "red"))
        timeconvert()

