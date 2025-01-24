import os
import pandas as pd

filePath = 'ADe La CruzCLeeIWall_cs111_final_indexData.csv'

def readCSV(filePath):
    """A function that reads indexData.csv file and creates six parallel lists containing information of daily stock exchange performances.
    
    Parameters:
        filePath: the file path of indexData.csv
    
    Returns:
        A tuple of six lists containing information of daily stock exchange performances.
    """
    
    with open(filePath, "r") as file:
        lines = file.read()

    lines = lines.split("\n")

    indexList = []
    dateList = []
    openList = []
    highList = []
    lowList = []
    closeList = []

    for line in lines[1:]:
        elements = line.split(',')
        
        if len(elements) < 8:
            continue
        
        indexList.append(elements[0])
        dateList.append(elements[1])
        openList.append(elements[2])
        highList.append(elements[3])
        lowList.append(elements[4])
        closeList.append(elements[5])

    return indexList, dateList, openList, highList, lowList, closeList


# print(readCSV(filePath))

def preprocessing(indexList, dateList, openList, highList, lowList, closeList):
    """A function for preprocessing to deal with rows that include null. If a null exists in the row, it will copy the data from the previous row.
    
    Parameters:
        indexList: the list containing stock exchange index.
        dateList: the list containing dates of observation.
        openList: the list containing the opening price during each trading days.
        highList: the list containing the highest price during each trading days.
        lowList: the list containing the lowest price during each trading days.
        closeList: the list containing the close price during each trading days.
    
    Returns:
        A tuple of six lists where any 'null' values in price lists are replaced with valid data.
    """
    
    if openList[0] == 'null' or highList[0] == 'null' or lowList[0] == 'null' or closeList[0] == 'null':
        openList[0] = 0
        highList[0] = 0
        lowList[0] = 0
        closeList[0] = 0
    
    
    for i in range(len(indexList)):
        
        if openList[i] == 'null' or highList[i] == 'null' or lowList[i] == 'null' or closeList[i] == 'null':
            openList[i] = openList[i - 1]
            highList[i] = highList[i - 1]
            lowList[i] = lowList[i - 1]
            closeList[i] = closeList[i - 1]
    
    return indexList, dateList, openList, highList, lowList, closeList



def selectedIndex(indexName):
    """A function that creates a tuple of six lists containing information of preprocessed daily performances of selected stock exchange.
    
    Parameters:
        indexName: selected stock exchange index
    
    Returns:
        A tuple of six lists containing information of preprocessed daily performances of selected stock exchange.
    """
    
    indexList, dateList, openList, highList, lowList, closeList = readCSV(filePath)
    
    lineNumList = []
    
    
    for i in range(len(indexList)):
        if indexList[i] == indexName:
            lineNumList.append(i)
            
    start = lineNumList[0]
    end = lineNumList[-1]

    indexList, dateList, openList, highList, lowList, closeList = preprocessing(indexList[start:end+1], dateList[start:end+1], openList[start:end+1], highList[start:end+1], lowList[start:end+1], closeList[start:end+1])
    
    return indexList, dateList, openList, highList, lowList, closeList
    


# Source: https://www.w3schools.com/python/pandas/pandas_dataframes.asp
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.insert.html

def writeCSV(resFileName, rangeList, pctChangeList):
    """A function that writes volatility.csv file for storing two volatility measurements data; daily price range and percent change.
    
    Parameters:
        rangeList: the list containing daily price range for each trading days.
        pctChangeList: the list containing percent change for each trading days except the very first day.
    
    Returns:
        None
    """
    
    df = pd.DataFrame()

    pctChangeList = [None] + pctChangeList
    
    df.insert(0, 'Daily Price Range', rangeList)
    df.insert(1, 'Percentage Change', pctChangeList)


    df.to_csv(resFileName + ".csv", index=False)




#=======================================================

def readCSV_test():
    
    a,b,c,d,e,f = readCSV(filePath)
    
    assert len(readCSV(filePath)) == 6, "readCSV should return a tuple containing six elements"
    assert a != None or b != None or c != None or d != None or e != None or f != None, "Neither of the elements in the returned tuple from readCSV should be None"
    assert len(a) == len(b) and len(b) == len(c) and len(c) == len(d), "All six elements in the returned tuple from readCSV should have the same length"
    
    
    print("readCSV passes all tests.")


def preprocessing_test():
    
    indexList = ["IXIC", "IXIC", "HSI", "HSI"]
    dateList = ["2024-05-12", "2024-05-13", "2024-05-14", "2024-05-15"]
    openList = ["null", "13416.90039", "null", "13485.33984"]
    highList = ["null", "13299.92969", "null", "13303.63965"]
    lowList = ["null", "13303.63965", "null", "13742.58984"]
    closeList = ["null", "13776.51953", "null", "13701.62988"]
    
    a, b, c, d, e, f = preprocessing(indexList, dateList, openList, highList, lowList, closeList)
    
    assert len(preprocessing(indexList, dateList, openList, highList, lowList, closeList)) == 6, "preprocessing should return a tuple containing six elements"
    assert a != None or b != None or c != None or d != None or e != None or f != None, "Neither of the elements in the returned tuple from preprocessing should be None"
    assert len(a) == len(b) and len(b) == len(c) and len(c) == len(d), "All six elements in the returned tuple from preprocessing should have the same length"
    
    
    assert c[0] == 0 or d[0] == 0 or e[0] == 0 or f[0] == 0, "If the very first data in one of the price lists is null, it should be changed to 0"
    assert c[2] == '13416.90039' or d[2] == '13299.92969' or e[2] == '13303.63965' or f[2] == '13776.51953', "If a 'null' price is encountered, all corresponding price lists should use the most recent valid data."
    
    
    print("preprocessing passes all tests.")


def selectedIndex_test():
    
    indexName = "HSI"
    
    a, b, c, d, e, f = selectedIndex(indexName)
    
    assert len(selectedIndex(indexName)) == 6, "selectedIndex should return a tuple containing six elements"
    assert a != None or b != None or c != None or d != None or e != None or f != None, "Neither of the elements in the returned tuple from selectedIndex should be None"
    assert len(a) == len(b) and len(b) == len(c) and len(c) == len(d), "All six elements in the returned tuple from preprocessing should have the same length"
    
    
    assert ["a different index detected"] != ["a different index detected" for data in a if data != "HSI"], "The indexList should not contain a different index from the stock exchange index that the user selected"
    
    assert ["null data detected"] != ["null data detected" for data in a if data == "null"], "The indexList should not contain null data"
    
    
    print("selectedIndex passes all tests.")


# Source: https://docs.python.org/3/library/os.path.html#os.path.exists

def writeCSV_test():
    
    resFileName = "unittest"
    
    rangeList = [1, 2, 3]
    pctChangeList = [0.15, -0.05]
    
    testSampleA = []
    testSampleB = []

    writeCSV(resFileName, rangeList, pctChangeList)
    
    with open(resFileName+".csv", "r") as file:
        lines = file.read()

    lines = lines.split("\n")
    
    for line in lines[:len(lines)-1]:
        elements = line.split(',')
        
        testSampleA.append(elements[0])
        testSampleB.append(elements[1])
    

    assert os.path.exists(resFileName+".csv"), "result CSV file was not created"
    
    assert testSampleA[0] == 'Daily Price Range' and testSampleB[0] == 'Percentage Change', "Columns do not match with the format. The order of the columns should be formated as Daily Price Range, Percentage Change"
        
    assert testSampleB[1] == '', "The first percentage change should be None"
    
    assert len(testSampleA) == len(testSampleB), "Each columns in the result file should have a same number of rows"
    assert testSampleA != None or testSampleB != None, "Neither of the data in the result file should be None"
    
    print("writeCSV passes all tests.")



if __name__ == "__main__":
    readCSV_test()
    preprocessing_test()
    selectedIndex_test()
    writeCSV_test()
