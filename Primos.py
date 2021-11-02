var=0
l=False
for var in range(101):
    if var==2 or var==3 or var==5 or var==7 or var==11 or var==13:
        print(var)
    if var%2!=0:
        if var%3!=0:
            if var%5!=0:
                if var%7!=0:
                    if var%11!=0:
                        if var%13!=0:
                            l=True
                            print (var)
    



