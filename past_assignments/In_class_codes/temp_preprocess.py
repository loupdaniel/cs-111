
# Purpose: Create environment for plotting temperatures
# Authors: Dr. David M. Kahn, heavily modified from code by Dr. Stacey Truex
# Date: Sept. 7, 2024
# CS 111

def average(temps, days):
    count = 0
    actual = 0
    tTotal = 0
    aves = []
    for t in temps:
        count = (count + 1) % days
        if t != None:
            tTotal = tTotal + t
            actual = actual + 1
        if count == 0:
            assert actual != 0
            ave = tTotal/actual
            aves.append(ave)
            tTotal = 0
            actual = 0
    return aves

def set_up():
    with open('newarkWaterWorksTemp.csv', 'r') as infile:
        lines = infile.readlines()[1:]
    minTemps = []
    maxT = -100
    minT = 100
    for line in lines:
        splitLine = line.split(",")
        minTStr = splitLine[5]  # min temp is index 4, but there is a comma in Newark, OH
        if minTStr == "":
            minTemps.append(None)
        else:
            t = int(minTStr[1:-1])
            minTemps.append(t)
            minT = min(minT,t)
            maxT = max(maxT,t)
    minD = min(1.1*minT, 0.9*minT) 
    maxD = max(1.1*maxT, 0.9*maxT) 
    dims = (0,minD,len(minTemps),maxD)
    aveMinMonthly = average(minTemps,30)
    aveMinYearly = average(minTemps,365)
    aveMin = average(minTemps,len(minTemps))[0]
    days = len(minTemps)
    return days,aveMinMonthly,aveMinYearly,aveMin,dims