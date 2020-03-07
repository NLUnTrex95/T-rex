import math
import os
#os.system("mode con cols=75 lines=100")
# This is the varables call list, most varables are given here. 
clear = range(32)
thirtyonedays = [1, 3, 5, 7, 8, 10, 12]
thirtydays = [4, 6, 9, 11]
ta = [[3, 23], [2, 22,], [1, 21, 31,]]
macrsyrs = [5,7]
DictMonth = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: \
     'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
DictMeth = {1: 'Straight Line', 2: 'Double Declining Balance', 3: 'Sum of the Years\' Digits', \
     4: 'Activity Based', 5: 'MACRS'}

# This is the end of the varables call function. 

def topHeader():
    """This is tbe hedder for text type document"""
    print("_" * 69)
    line = ("Depreciation of Fixed Assets", "=" * 61, "Now with: Knowing which months have 31 days!",
            "Introuducing Bonus Depreciation!",
            "The stupid box that can do math for me, version 2.8", "Updated 2/4/2020")
    edges = ["|*x*", "*x*|"]
    for i in range(0, 6):
        new_line = line[i].center(61, " ")
        print(edges[0] + new_line + edges[1])
    print("=" * 69)

def header():
    """this is a recap of all of your entered imputs so you can keep track of them. """
    print("_" * 69)
    print("Cost is $",cost, "| Salvage Value is $",salv, "| Useful life is", years, "years.")
    print("We are using the", DictMeth[method], "method.")
    print("The date of purchase is", DictMonth[date], str(day) + th,"| The depreciable base is $",DepBase)
    if method == 5:
        print("The property class is", years, "year property. Tables from IRS publication 946")
    print("_" * 69)
    print("|  Year  |  Amount of DEP  |  NBV amount  |  Accumulated amount is  |")
    print("=" * 69)


def tablerow():  
    ''' This prints the output if useing methods 1-3 '''
    yr = len(str(yrspass))
    aod = len(str(dep))
    nb = len(str(nbv))
    ad = len(str(AccumDep))
    pyr = " " * (6 - int(yr))
    paod = " " * (16 - int(aod))
    pnb = " " * (9 - int(nb))
    pad = " " * (12 - int(ad))
    print("|" + str(pyr) + str(yrspass) + "  |" + str(paod) + "$" + str(dep) + "|" + str(pnb) + "$" + str(
        nbv) + "    |" + str(pad) + "$" + str(AccumDep) + "            |")

def tablerowam(): 
    ''' This is the print function for methods 4-5 '''
    yr = len(str(yrspass))
    aod = len(str(DEPR[z]))
    nb = len(str(NBV[z]))
    ad = len(str(AD[z]))
    pyr = " " * (6 - int(yr))
    paod = " " * (16 - int(aod))
    pnb = " " * (9 - int(nb))
    pad = " " * (12 - int(ad))
    print("|" + str(pyr) + str(YRS[z]) + "  |" + str(paod) + "$" + str(DEPR[z]) + "|" + str(pnb) + "$" + str(
            NBV[z]) + "    |" + str(pad) + "$" + str(AD[z]) + "            |")


topHeader()  # This prints the header for the text baised output. 


# This is messy input cleaning and needds to be fixed.
##User inputs start here
date = int(input("Month of Purchase? 1-Jan, 2-Feb, 3-Mar, 4-Apr... > "))
##Month Checker


while date not in clear[1:13]:
    print("Invalid Month.")
    print("Please enter a valid month using code 1-Jan, 2-Feb, 3-Mar, 4-Apr...")
    date = int(input("Month: > "))
day = int(input("Date of Purchase? > "))
##Day checker

while date in thirtydays and day > 30 or day < 1:
    print("Invalid day. Please enter a valid day.")
    day = int(input("Day: > "))
while date in thirtyonedays and day > 31 or day < 1:
    print("Invalid day. Please enter a valid day.")
    day = int(input("Day: > "))
while day > 28 or day < 1:
    print("Invalid day. Please enter a valid day.")
    day = int(input("Day: > "))
# This is messy input cleaning and needds to be fixed.

# This needs to be placed into a function, and cleaned up. 
# This checks to see how many days are in a month. 
if date in thirtyonedays:
    fday = (32 - day) / 31
elif date in thirtydays:
    fday = (31 - day) / 31
else:
    fday = (29 - day) / 30
##Suffix Checker
# This needs to be placed into a ajoining function, or its own function. 
if day in ta[0]:
    th = "rd"
elif day in ta[1]:
    th = "nd"
elif day in ta[2]:
    th = "st"
else:
    th = "th"

# We gather more inputs at this stage. 
cost = int(input("Cost: $"))
salv = int(input("Salvage Value: $"))
while salv > cost:
    print("The salvage value must be less than cost. Please enter a valid salvage value.")
    salv = int(input("Salvage Value: $"))
years = int(input("Useful Life (Years): "))
while years < 1:
    print("Please enter a valid number of years for the useful life: ")
    years = int(input("Years: "))
method = int(input("Method? 1-SL, 2-DDB, 3-SOYD, 4-ABC 5-MACRS > "))
while method not in clear[1:6]:
    print("Invalid Method. Please enter a valid method using code 1-SL, 2-DDB, 3-SOYD, 4-ABC 5-MACRS")
    method = int(input("Method: "))
while method == 5 and years not in macrsyrs:
    print("MACRS only supports", macrsyrs, "year property. Please select a different method.")
    method = int(input("Method: "))

# This is unknown messy code, needs a home. 
DepBase = cost - salv
rounding = mult = runout = False

## This is if the method is Straight Line
# We need this in a function, and needs to be cleaned up. 
if method == 1:
    dep = int(DepBase / years)
    header()
    if fday != 1:
        date += fday
    yrspass = 1
    AccumDep = 0
    if date != 1:
        dep = math.ceil(((13 - date) / 12) * (DepBase / years))
        AccumDep = dep
        nbv = cost - dep
        tablerow()
        yrspass += 1
    dep = math.ceil((int((DepBase) / (years))))
    nbv = cost - AccumDep
    while int(yrspass) <= int(years):
        if date == 1 and int(yrspass) == int(years + 1):
            break
        nbv -= dep
        AccumDep += dep
        tablerow()
        yrspass += 1
    if date != 1:
        dep = math.floor(((12 - (13 - date)) / 12) * (DepBase / years))
        nbv = salv
        AccumDep = cost - salv
        tablerow()
    print("=" * 69)

##This is the method is Double Declining Balance
# We need this in a function, and needs to be cleaned up. 
elif int(method) == 2:
    DepBase = cost
    if date != 1:
        mult = True
    yrspass = 1
    AccumDep = dep = 0
    nbv = cost
    header()
    if fday != 1:
        date += fday
    while (yrspass) <= (years):
        if (yrspass) == int(years + 1) and date == 1:
            break
        rate = 2 / (years)
        dep = int((rate) * (nbv))
        if mult is True:
            dep *= ((13 - date) / 12)
            mult = False
        dep = math.ceil(dep)
        AccumDep += int(dep)
        nbv = int(cost - AccumDep)
        if (nbv) <= (salv):
            AccumDep = cost - salv
            nbv = int(cost - AccumDep)
            tablerow()
            print("The Book Value has dropped below the Salvage Value using DDB.")
            print("Remainder of Depreciable Base Depreciated")
            yrspass += 1
            dep = cost - salv
            nbv = int(cost - AccumDep)
            break
        tablerow()
        yrspass += 1
    print("=" * 69)

##This is the method of Sum of the Years' Digits. 
# We need this in a function, and needs to be cleaned up. 
elif int(method) == 3:
    header()
    if fday != 1:
        day += fday
    mult = rounding = False
    if date != 1:
        mult = True
    yrspass = numerator = denominator = 1
    AccumDep = soydlast = soydthis = 0
    nbv = cost

    while (yrspass) <= (years + 1):
        if yrspass == int(years + 1) and date == 1:
            break
        numerator = (years - yrspass + 1)
        numprime = (years - yrspass + 2)
        denominator = (int(years) * int(years + 1)) / 2
        dep = int((numerator / denominator) * DepBase)
        if mult is True and yrspass == 1:
            dep *= ((13 - date) / 12)
        if mult is True and yrspass != 1:
            denomfun2 = (12 - (date - 1)) / 12
            denomfun1 = (12 - (13 - date)) / 12
            soydlast = math.ceil(int(((numprime / denominator) * DepBase) * denomfun1))
            soydthis = math.ceil(int(((numerator / denominator) * DepBase)) * (denomfun2))
            dep = int(soydlast + soydthis)
        dep = math.ceil(dep)
        if yrspass == years + 1 and date != 1:
            dep = (nbv - salv)
            rounding = True
        elif yrspass == years and date == 1:
            dep = (nbv - salv)
            rounding = True
        AccumDep += int(dep)
        nbv -= dep
        tablerow()
        yrspass += 1
    print("=" * 69)
    if rounding is True:
        print("Due to rounding, full amount of depreciation taken in year", yrspass - 1)

##This is the method of Activity Based Costing. 
# We need this in a function, and needs to be cleaned up. 
elif int(method) == 4:
    yrspass = 1
    AccumDep = a = adu = 0  ##Setting all variables to 0
    albase = int(input("Total Allocation Base: "))
    runout = 0
    ##Creating lists to store inputs and outputs for each year, filled with zeroes
    Activity = [0] * years
    DEPR = [0] * years
    AD = [0] * years
    YRS = [0] * years
    NBV = [0] * years
    NBV[0] = cost
    while yrspass <= years:
        Activity[a] = int(input("Activity in year " + str(yrspass) + ": "))
        DEPR[a] = math.floor((Activity[a] / albase) * DepBase)
        AD[a] += DEPR[a]
        AD[a] += AD[a - 1]
        NBV[a] -= DEPR[a]
        NBV[a] += NBV[a - 1]
        YRS[a] = yrspass
        adu += Activity[a]
        if adu > albase:
            DEPR[a] = "*" + str(salv - NBV[a]) + "*"
            NBV[a] = "*" + str(salv) + "*"
            AD[a] = "*" + str(DepBase) + "*"
            runout += 1
            break
        a += 1
        yrspass += 1
    header()
    for z in range(0, years):
        tablerowam()
    print("=" * 69)
    if runout == 1:
        print("The Allocation Base has run out")
        print("Excess: ", adu - albase)
##This is if the method is MACRS
# We need this in a function, and needs to be cleaned up. 
elif method == 5:
    DepBase = cost
    MACRS = [.2, .32, .192, .1152, .1152, .0576, .1429, .2449, .1749, .1249, .0893, .0892, .0893, .0446, ##Half Year
             .35, .26, .156, .1101, .1101, .0138, .25, .2143, .1531, .1093, .0875, .0874, .0875, .0109, ##MQ, Q1
             .25, .3, .18, .1137, .1137, .0426, .1785, .2347, .1676, .1197, .0887, .0887, .0887, .0334, ##MQ, Q2
             .15, .34, .204, .1224, .1130, .0706, .1071, .2551, .1822, .1302, .0930, .0885, .0886, .0553, ##MQ, Q3
             .05, .038, .228, .1368, .1094, .0958, .0357, .2755, .1968, .1406, .1004, .0873, .0873, .0764] ##MQ, Q4
    yearspl = years + 1
    yrspass = 1
    DEPR = [0] * yearspl
    NBV = [0] * yearspl
    NBV[0] = cost
    AD = [0] * yearspl
    YRS = [0] * yearspl
    rounding = False
    conv = int(input("Convention? 1-Half Year, 2-Mid Quarter > "))
    while conv > 2 or conv < 1:
        print("Please input a valid convention, where 1-Half year, 2-Mid Quarter")    
        conv = int(input("Convention: > "))
    bon = int(input("Elect Bonus? Bonus is mandatory. 1-Yes, 2-No. > "))
    while bon > 2 or bon < 1:
        print("Please input a valid response, where 1-Yes, 2-No.")
        bon = int(input("Take Bonus? > "))
    quart = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    if conv == 1:
        if years == 5:
            m = 0
        elif years == 7:
            m = 6
    elif conv == 2:
        if years == 5:
            if date in quart[0]:
                m = 14
            elif date in quart[1]:
                m = 28
            elif date in quart[2]:
                m = 42
            elif date in quart[3]:
                m = 56
        elif years == 7:
            if date in quart[0]:
                m = 20
            elif date in quart[1]:
                m = 34
            elif date in quart[2]:
                m = 48
            elif date in quart[3]:
                m = 62
    if bon == 1:
        header()
        z = 0
        DEPR[0] = cost
        NBV[0] = 0
        AD[0] = cost
        tablerowam()
        for z in range (1, yearspl):
            DEPR[z] = 0
            NBV[z] = 0
            AD[z] = cost
            tablerowam()
        print("Fully depreciated in Year 1.")
        print("No more depreciation deduction allowable for years 2 -", yearspl)
    else:
        header()
        for z in range(0, yearspl):
            DEPR[z] = math.floor(MACRS[m] * cost)
            NBV[z] -= DEPR[z]
            NBV[z] += NBV[z-1]
            if z == years and NBV != 0:
                DEPR[z] += NBV[z]
                NBV[z] = 0
                rounding = True
            YRS[z] = yrspass
            AD[z] += DEPR[z]
            AD[z] += AD[z - 1]
            yrspass += 1
            m += 1
            tablerowam()
    print("=" * 69)
    if rounding is True:
        print("Due to rounding, remaining depreciation taken in year", yrspass - 1)
end = input("Press enter to exit")
