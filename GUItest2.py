import gui 
test_dict = (gui.gui_run())
print(test_dict)


def checker(test_dict):
    for key, value in test_dict.items():
        if value in type_of_accounting_selected:
            c = 1
        else:
            c = value
        if isinstance(c, int) == False:
            print(c, "Bad!") #this will be an error popup.

def converter(test_dict):
    i = 0
    convlist = [0] * int(len(test_dict))
    converting = True
    while converting:
        if test_dict[stats_tracking_list[i]] in type_of_accounting_selected:
            convlist[i] = test_dict[stats_tracking_list[i]]
            break
        test_dict[stats_tracking_list[i]] = int(test_dict[stats_tracking_list[i]])
        convlist[i] = test_dict[stats_tracking_list[i]]
        i += 1
    return convlist
## Possible include in class


def MonthDayNumbers(month):
    thirtyone = [1, 3, 5, 7, 8, 10, 12]
    thirty = [4, 6, 9, 11]
    if month in thirtyone:
        output = 31
    elif month in thirty:
        output = 30
    else:
        output = 28
    return output

  
def FractionalYears():
  
  
    def append():
        yearsout.append(round((deplist[2] + 1), 2))
        nbvout.append(round(deplist[1], 2))
        adout.append(round((deplist[0] - deplist[1]), 2))
        if deplist[5] == "SOYD":
            depout.append(round(((1 / ((deplist[2] * (deplist[2] + 1)) / 2)) * deplist[0]),2))  
    yearmult = (13 - deplist[3])
    if deplist[4] != 1:
        yearmult -= round((MonthDayNumbers(deplist[3]) - deplist[4]) / MonthDayNumbers(deplist[3]),2) ##Check whether it's += or -=...?
    yearmult /= 12
    yearmult = round(yearmult, 2)
    if deplist[5] == "Straight Line" or deplist[5] == "SOYD":
        append()
    return yearmult

  
def LastYear(s):  ## Possible class usage.
    yearsout[s] += 1
    yearsout[s] += yearsout[s - 1]
    nbvout[s] += nbvout[s - 1]
    adout[s] += adout[s - 1]

## Possible class usage, used in every method.    
def Increment(s):
    nbvout[s] -= round(depout[s],2)
    adout[s] += round(depout[s],2)

## Possible class distinction    
def stop(s):
    adout[s] = deplist[0] - deplist[1]
    depout[s] = adout[s]-adout[s-1]
    nbvout[s] = deplist[1]
    for y in range(s+1, deplist[2]):
        yearsout[y] += 1
        yearsout[y] += yearsout[y - 1]
        
## Possible class distinction
def astop(s):
    depout[s] = deplist[1] - nbvout[s]
    nbvout[s] = deplist[1]
    adout[s] = deplist[0] - deplist[1]

##This area creates all the column heading lists (data), which needed for all methods.
deplist = converter(test_dict)  #Line 119
checker(test_dict)  #Line 109
yearsp = deplist[2]
## yearsout = depout = nbvout = adout = ([0] * deplist[2])
yearsout = [0] * yearsp #Possible for loop spot.
depout = [0] * yearsp
nbvout = [0] * yearsp
nbvout[0] = deplist[0]  #Setting the initial NBV to the Cost.
adout = [0] * yearsp
## may need relocation.
activity = [100, 200, 300, 250, 150]  #Only for activity basis. Filler values in lieu of user inputs


def StraightLine():
    depbase = deplist[0] - deplist[1]
    for s in range(0, deplist[2]):
        LastYear(s)
        depout[s] = round((depbase / deplist[2]), 2)
        if s == 0 and (deplist[3] != 1 or deplist[4] != 1):
            depout[s] *= FractionalYears()
            depout.append(round((depbase / deplist[2]) - depout[0], 2))
        Increment(s)
    output = {"Year": yearsout, "Depreciation": depout, "NBV": nbvout, "A/D": adout,}
    return output


def DoubleDeclining():
    for s in range(0, deplist[2]): ## class posibly. In all formats.
        LastYear(s)
        depout[s] = nbvout[s] * (2 / deplist[2]) ##Moved this to below the previous phrase. We can't multiply nothing ;D
        if s == 0 and (deplist[3] != 1 or deplist[4] != 1):
            depout[s] *= FractionalYears()
        Increment(s)
        if nbvout[s] < deplist[1]:
            stop(s)
            break
    output = {"Year": yearsout, "Depreciation": depout, "NBV": nbvout, "A/D": adout}
    return output

  
def SumOfYears():
    for s in range(0, deplist[2]):
        LastYear(s)
        denominator = ((deplist[2] * (deplist[2] + 1))/2)
        depout[s] = round(((deplist[2] - yearsout[s] + 1) / denominator) * (deplist[0] - deplist[1]),2)
        if s == 0 and (deplist[3] != 1 or deplist[4] != 1):
            mult = FractionalYears()
        else: mult = 1
        depout[s] *= mult
        if s != 0:
            depout[s] += round((depout[s-1] / mult - (depout[s-1])),2)
        Increment(s)
    output = {"Year": yearsout, "Depreciation": depout, "NBV": nbvout, "A/D": adout}
    return output

  
def ActivityBased():
    albase = 1000 #Temporary variable in lieu of user input.
    ucost = (deplist[0] - deplist[1]) / albase
    for s in range(0, deplist[2]):
        LastYear(s)
        depout[s] = activity[s] * ucost
        albase -= activity[s]
        Increment(s)
        if albase < 0:
            astop(s)
            break
    output = {"Year": yearsout, "Depreciation": depout, "NBV": nbvout, "A/D": adout}
    return output

  
def MACRS():
    MACRS = [.2, .32, .192, .1152, .1152, .0576, .1429, .2449, .1749, .1249, .0893, .0892, .0893, .0446,  ##Half Year
               .35, .26, .156, .1101, .1101, .0138, .25, .2143, .1531, .1093, .0875, .0874, .0875, .0109,  ##MQ, Q1
               .25, .3, .18, .1137, .1137, .0426, .1785, .2347, .1676, .1197, .0887, .0887, .0887, .0334,  ##MQ, Q2
               .15, .34, .204, .1224, .1130, .0706, .1071, .2551, .1822, .1302, .0930, .0885, .0886, .0553,  ##MQ, Q3
               .05, .038, .228, .1368, .1094, .0958, .0357, .2755, .1968, .1406, .1004, .0873, .0873, .0764]  ##MQ, Q4
    conv = "Half Year" #Convention auto-filled in lieu of user input.
    quart = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    MList = [[20,34,48,62],[14,28,42,56]]
    if conv == "Half Year":
    	m = 0 if deplist[2] == 5 else 6 
    elif conv == "Mid Quarter":
      if deplist[2] == 5:
        for x in range(0,3)
          if deplist[2] in quart[x]:
            m = MList[0[x]]
      elif deplist[2] == 7:
          for x in range(0,3)
          if deplist[2] in quart[x]:
              m = MList[1[x]]
    else:
        root.mainloop
    for s in range(0, deplist[2]):
        LastYear(s)
        depout[s] = MACRS[m] * deplist[0]
        Increment(s)
        m += 1
    output = {"Year": yearsout, "Depreciation": depout, "NBV": nbvout, "A/D": adout}
    return output

running = True ## Relocate this.
##The Main Program Area
while running:
    if deplist[5] == "Straight Line":
        backout = StraightLine()
    elif deplist[5] == "DDB":
        backout = DoubleDeclining()
    elif deplist[5] == "SOYD":
        backout = SumOfYears()
    elif deplist[5] == "ABC":
        backout = ActivityBased()
    elif deplist[5] == "MACRS":
        backout = MACRS()
    print(backout) ## this will post to new screen. Table.
    end = input("Press Enter")
'''
This is a sample backout list.
{"Year": [1,2,3,4,5], "Depreciation": [20000,20000,20000,20000,20000], "NBV": [100000,80000,60000,40000,20000], "A/D": [20000,40000,60000,80000,100000]}    
'''
