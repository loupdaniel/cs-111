"""
Purpose: Solution for project 6 (Climate Change)
Author: Chanhui Lee, Derek Howe, Will Lang
Date: November 15th, 2024
CS 111, Fall 2024
"""

import matplotlib.pyplot as pyplot

def readCSV(filePath):
    """A function that reads 2008CompilationData.csv file and creates four parallel lists containing information about 18O and 13C readings. If a row is missing either the 18O value or the 13C value, do not include that row in your lists.
    
    Parameters:
        filePath: the file path of 2008CompilationData.csv.
    
    Returns:
        siteList: a list containing the sites of the measurements.
        ageList: a list containing the ages of the measurements.
        d18OList: a list containing the 18O measurements.
        d13CList: a list containing the 13C measurements.
    """
    
    with open(filePath, "r") as file:
        lines = file.read()

    lines = lines.split("\n")

    siteList = []
    ageList = []
    d18OList = []
    d13CList = []

    for line in lines[1:]:
        elements = line.split(',')
        
        # Ensure that the case when 'Genus' is empty but d18O and d13C exists is not passed
        if len(elements) < 4 or elements[3] == '' or elements[4] == '':
            continue
        
        siteList.append(elements[0])
        ageList.append(float(elements[1]))
        d18OList.append(float(elements[3]))
        d13CList.append(float(elements[4]))

    return siteList, ageList, d18OList, d13CList


def scatterPlot(ageList, d18OList, d13CList):
    """A function that creates scatter plots using three parallel lists containing information about 18O and 13C readings.

    Parameters:
        ageList: a list containing the ages of the measurements.
        d18OList: a list containing the 18O measurements.
        d13CList: a list containing the 13C measurements.
    
    Returns:
        None
    """
    pyplot.figure(1)
    pyplot.scatter(ageList, d18OList, s=1)
    pyplot.xlabel("Age (Ma)")
    pyplot.ylabel("d18O")
    pyplot.title("d18O scatter plot")


    pyplot.figure(2)
    pyplot.scatter(ageList, d13CList, s=1)
    pyplot.xlabel("Age (Ma)")
    pyplot.ylabel("d13C")
    pyplot.title("d13C scatter plot")
    
    pyplot.show()


csvFile = "2008CompilationData.csv"

def part1():
    """The function for running Part 1: Read and plot the data.
    """

    siteList, ageList, d18OList, d13CList = readCSV(csvFile)
    scatterPlot(ageList, d18OList, d13CList)

#===========================================================================================================

def smooth(data, width):
    """A function that returns a new list of data, smoothed over windows of the given width.
    
    Parameters:
        data: a list of numbers.
        width: the width of each window.
    
    Returns:
        smoothedData: a list of smoothed data values.
    """
    smoothedData = []
    total = 0 # get sum for the first window
    
    
    if width <= 0:
        return "The width should be bigger than 0"
    
    if len(data) == 0:
        return "The given list is empty"
    
    
    for index in range(width):
        total = total + float(data[index])
    
    for index in range(len(data)):
        width = min(width, len(data) - index) # adjust width near the end
        smoothedData.append(total / width) # append the window mean
        total = total - float(data[index]) # subtract leftmost value
        
        if index + width < len(data): # if possible,
            total = total + float(data[index + width]) # add rightmost value
    
    return smoothedData


def smoothPlot(ageList, d18OList, d13CList):
    """A function that creates scatter plots using three smoothed parallel lists containing information about 18O and 13C readings.

    Parameters:
        ageList: a smoothed list containing the ages of the measurements.
        d18OList: a smoothed list containing the 18O measurements.
        d13CList: a smoothed list containing the 13C measurements.
        
    Returns:
        None
    """
    pyplot.figure(3)
    
    pyplot.subplot(2, 1, 1) # arguments are (rows, columns, subplot #)
    pyplot.scatter(ageList, d18OList, s=1)
    pyplot.xlabel("Age (Ma)")
    pyplot.ylabel("d18O")
    pyplot.title("d18O scatter plot")
    
    pyplot.subplot(2, 1, 2)
    pyplot.scatter(ageList, d13CList, s=1)
    pyplot.xlabel("Age (Ma)")
    pyplot.ylabel("d13C")
    pyplot.title("d13C scatter plot")
    
    pyplot.show()


def part2():
    """The function for running Part 2: Smooth and plot the data.
    """
    siteList, ageList, d18OList, d13CList = readCSV(csvFile)
    ageList = smooth(ageList, 5)
    d18OList = smooth(d18OList, 5)
    d13CList = smooth(d13CList, 5)
    
    smoothPlot(ageList, d18OList, d13CList)

#===========================================================================================================

def petm(siteList, ageList, d18OList, d13CList):
    """A function that creates three new lists, one of ages and the other two of measurements, that contain data only for ages between 53 and 57 ma and only for sites 527, 690, and 865.

    Parameters:
        siteList: a list containing the sites of the measurements.
        ageList: a list containing the ages of the measurements.
        d18OList: a list containing the 18O measurements.
        d13CList: a list containing the 13C measurements.

    Returns:
        newAgeList: a list of ages containing data only for ages between 53 and 57 ma and only for sites 527, 690, and 865.
        newD18OList: a list of the 18O measurements containing data only for ages between 53 and 57 ma and only for sites 527, 690, and 865.
        newD13CList: a list of the 13C measurements containing data only for ages between 53 and 57 ma and only for sites 527, 690, and 865.
    """
    
    a = len(siteList)
    b = len(ageList)
    c = len(d18OList)
    d = len(d13CList)
    
    if len(siteList) == 0 or len(ageList) == 0 or len(d18OList) == 0 or len(d13CList) == 0:
        return "One or more given lists are empty"
    
    if a != b or b != c or c != d:
        return "All lists are not having the same length"
    
    siteListIndex = []
    newD18OList = []
    newD13CList = []
    newAgeList = []
    
    for i in range(len(siteList)):
        if siteList[i] in ['527', '690', '865']:
            # newSiteList.append(siteList[i])
            siteListIndex.append(i)
            
    for i in siteListIndex:
        if float(ageList[i]) >= 53 and float(ageList[i]) <= 57:
            newD18OList.append(d18OList[i]) 
            newD13CList.append(d13CList[i]) 
            newAgeList.append(ageList[i])
            
    return newAgeList, newD18OList, newD13CList


def petmPlot(newAgeList, newD18OList, newD13CList):
    """A function that creates scatter plots using three lists, one of ages and the other two of measurements, that contain data only for ages between 53 and 57 ma and only for sites 527, 690, and 865.

    Parameters:
        newAgeList: a list of ages containing data only for ages between 53 and 57 ma and only for sites 527, 690, and 865.
        newD18OList: a list of the 18O measurements containing data only for ages between 53 and 57 ma and only for sites 527, 690, and 865.
        newD13CList: a list of the 13C measurements containing data only for ages between 53 and 57 ma and only for sites 527, 690, and 865.
        
    Returns:
        None
    """
    pyplot.figure(4)
    
    pyplot.subplot(2, 1, 1) # arguments are (rows, columns, subplot #)
    pyplot.scatter(newAgeList, newD18OList, s=1)
    pyplot.xlabel("Age (Ma)")
    pyplot.ylabel("d18O")
    pyplot.title("d18O scatter plot")
    
    pyplot.subplot(2, 1, 2)
    pyplot.scatter(newAgeList, newD13CList, s=1)
    pyplot.xlabel("Age (Ma)")
    pyplot.ylabel("d13C")
    pyplot.title("d13C scatter plot")
    
    pyplot.show()


def part3():
    """The function for running Part 3: The PETM.
    """
    siteList, ageList, d18OList, d13CList = readCSV(csvFile)
    newAgeList, newD18OList, newD13CList = petm(siteList, ageList, d18OList, d13CList)
    petmPlot(newAgeList, newD18OList, newD13CList)

#===========================================================================================================

def readTXT(filePath):
    """A function that reads co2nat.txt file and extracts the data into two parallel lists — a list of ages and a list of corresponding CO2 concentrations.

    Parameters:
        filePath: the file path of co2nat.txt.

    Returns:
        ageList: a list of ages.
        co2List: a list of corresponding CO2 concentrations.
    """
    
    with open(filePath, "r") as file:
        lines = file.read()

    lines = lines.split("\n")
    
    sample = []
    
    for i in range(1, len(lines)):
        sample.append(lines[i].split("\t"))
    
    #print(sample)
    
    ageList = []
    co2List = []
    
    for i in range(len(sample)):
        ageList.append(int(sample[i][0]))
        co2List.append(float(sample[i][1]))
    
        
    return ageList, co2List
    
    
def recentD18O(filePath):
    """A function that reads 2008CompilationData.csv file and creates two new parallel lists — one containing the 18O readings from sites 607, 659, and 849 for the last 420,000 years, and the other containing the corresponding ages. 

    Parameters:
        filePath: the file path of 2008CompilationData.csv.

    Returns:
        recentAgeList: a list of corresponding ages of recentD18OList.
        recentD18OList: a list of 18O readings from sites 607, 659, and 849 for the last 420,000 years.
    """
    
    with open(filePath, "r") as file:
        lines = file.read()

    lines = lines.split("\n")

    siteList = []
    ageList = []
    d18OList = []

    for line in lines[1:]:
        elements = line.split(',')
        
        siteList.append(elements[0])
        ageList.append(elements[1])
        d18OList.append(elements[3])
        

    siteListIndex = []
    recentAgeList = []
    recentD18OList = []
    
    for i in range(len(siteList)):
        if siteList[i] in ['607', '659', '849']:
            # newSiteList.append(siteList[i])
            siteListIndex.append(i)
                
    
    for i in siteListIndex:
        if float(ageList[i]) <= 0.42:
            recentAgeList.append(float(ageList[i]))
            recentD18OList.append(float(d18OList[i]))
            
    return recentAgeList, recentD18OList


def recentHistoryPlot(ageList, co2List, recentAgeList, recentD18OList):
    """A function that creates two subplots using four lists to plot the most recent 420,000 years of d18O readings and the CO2 concentrations.

    Parameters:
        ageList: a list of ages.
        co2List: a list of corresponding CO2 concentrations.
        recentAgeList: a list of corresponding ages of recentD18OList.
        recentD18OList: a list of 18O readings from sites 607, 659, and 849 for the last 420,000 years.
        
    Returns:
        None
    """
    pyplot.figure(5)
    
    pyplot.subplot(2, 1, 1) # arguments are (rows, columns, subplot #)
    pyplot.scatter(ageList, co2List, s=1)
    pyplot.xlabel("Age (years)")
    pyplot.ylabel("CO2 concentrations (ppmv)")
    pyplot.title("CO2 concentrations")
    
    pyplot.subplot(2, 1, 2)
    pyplot.scatter(recentAgeList, recentD18OList, s=1)
    pyplot.xlabel("Age (Ma)")
    pyplot.ylabel("d18O")
    pyplot.title("Recent d18O")
    
    pyplot.show()


co2File = "co2nat.txt"

def part4():
    """The function for running Part 4: Recent history.
    """
    ageList, co2List = readTXT(co2File)
    recentAgeList, recentD18OList = recentD18O(csvFile)
    recentHistoryPlot(ageList, co2List, recentAgeList, recentD18OList)

#===========================================================================================================

def readMLOCSV(filePath):
    """A function that reads weekly_in_situ_co2_mlo.csv file and creates two parallel lists, one containing the CO2 concentration readings and the other containing the dates of the readings.

    Parameters:
        filePath: the file path of weekly_in_situ_co2_mlo.csv.

    Returns:
        dateList: a list of corresponding dates of co2List.
        co2List: a list of CO2 concentration readings.
    """
    
    with open(filePath, "r") as file:
        lines = file.read()

    lines = lines.split("\n")

    co2List = []
    dateList = []

    for line in lines[44:]:
        line = line.split(",")
        
        if len(line) <= 1:
            continue
        
        dateList.append(float(line[0][:4]) + (float(line[0][5:7]) + float(line[0][8:10])/31) / 12)
        co2List.append(float(line[1].strip()))
        
    return dateList, co2List


def keelingCurvePlot(dateList, co2List):
    """A function that plots the Keeling curve using a list of CO2 concentration readings and a list of corresponding dates.

    Parameters:
        dateList: a list of corresponding dates of co2List.
        co2List: a list of CO2 concentration readings.
        
    Returns:
        None
    """
    
    pyplot.scatter(dateList, co2List, s=1)
    pyplot.xlabel("Date")
    pyplot.ylabel("CO2 concentrations (ppmv)")
    pyplot.title("Keeling curve")
    
    pyplot.show()


fileMLO = "weekly_in_situ_co2_mlo.csv"

def part5():
    """The function for running Part 5: Very recent history.
    """
    dateList, co2List = readMLOCSV(fileMLO)
    keelingCurvePlot(dateList, co2List)

#=======================================================

def readCSV_test():
    a,b,c,d = readCSV(csvFile)
    
    assert len(readCSV(csvFile)) == 4, "readCSV should return four elements"
    assert a != None or b != None or c != None or d != None, "Neither of the returned elements from readCSV should be None"
    assert len(a) == len(b) and len(b) == len(c) and len(c) == len(d), "All four returned elements from readCSV should have the same length"
    
    
    print("readCSV passes all tests.")


def readTXT_test():
    ageList, co2List = readTXT(co2File)
    
    assert len(readTXT(co2File)) == 2, "readTXT should return two elements"
    assert len(ageList) == 283 and len(co2List) == 283, "All returned elements' length from readTXT should be 283"
    assert ageList != None or co2List != None, "Neither of the returned elements from readTXT should be None"
    assert len(ageList) == len(co2List), "All returned elements from readTXT should have the same length"
    
    
    print("readTXT passes all tests.")


def recentD18O_test():
    recentAgeList, recentD18OList = recentD18O(csvFile)
    
    assert len(recentD18O(csvFile)) == 2, "recentD18O should return two elements"
    assert len(recentAgeList) == 359 and len(recentD18OList) == 359, "All returned elements' length from recentD18O should be 359"
    assert recentAgeList != None or recentD18OList != None, "Neither of the returned elements from recentD18O should be None"
    assert len(recentAgeList) == len(recentD18OList), "All returned elements from recentD18O should have the same length"
    
    
    print("recentD18O passes all tests.")

    
def readMLOCSV_test():
    dateList, co2List = readMLOCSV(fileMLO)
    
    assert len(readMLOCSV(fileMLO)) == 2, "readMLOCSV should return two elements"
    assert len(dateList) == 3347 and len(co2List) == 3347, "All returned elements' length from readMLOCSV should be 3347"
    assert dateList != None or co2List != None, "Neither of the returned elements from readMLOCSV should be None"
    assert len(dateList) == len(co2List), "All returned elements from readMLOCSV should have the same length"
    
    
    print("readMLOCSV passes all tests.")
    

def smooth_test():
    
    # Common cases
    assert smooth([21,9,3,0,-3],3) == [11,4,0,-1.5, -3], "The Smooth function does not return the correct list for ([21,9,3,0,-3],3)"
    
    # Edge cases
    assert smooth([21,9,3,0,-3], -1) == "The width should be bigger than 0", "The Smooth function should not have fully ran since the width was 0 or less."
    assert smooth([],4) == "The given list is empty", "The given list is empty"
    
    print("smooth passes all tests.")
    
    
def petm_test():
    
    # Common cases
    assert petm(['527','999','865'],[54, 54, 60],[3.16, 0.28, 3.14],[0.96, 0.22, 0.17]) == ([54],[3.16],[0.96]), "Petm does not work as intended"
    
    # Edge cases
    assert petm([],[],[],[]) == "One or more given lists are empty", "One or more given lists are empty"
    assert petm(['527','999','865'],[54, 54, 60],[3.16, 0.28],[0.96, 0.22, 0.17]) == "All lists are not having the same length", "All lists are not having the same length"
    
    print("petm passes all tests.")
    



if __name__ == "__main__":
    readCSV_test()
    readTXT_test()
    recentD18O_test()
    readMLOCSV_test()
    smooth_test()
    petm_test()
