def dailyPriceRange(highList, lowList):
    """A function that calculates Daily Price Range for each trading days with using highList and lowList and returns a list containing Daily Price Range for each trading days.
    
    Parameters:
        highList: the list containing the highest price during each trading days.
        lowList: the list containing the lowest price during each trading days.
    
    Returns:
        rangeList: the list containing daily price range for each trading days.
    """

    rangeList = []

    for i in range(len(highList)):
        rangeList.append(round(float(highList[i]) - float(lowList[i]), 6))
        
    return rangeList


def percentageChange(closeList):
    """A function that calculates percent change for each trading days with using closeList and returns a list containing percent change for each trading days. The percent change could not be extracted from the very first day within the data.
    
    Parameters:
        closeList: the list containing the close price during each trading days.
    
    Returns:
        pctChangeList: the list containing percent change for each trading days except the very first day.
    """
    
    pctChangeList = []
    
    for i in range(1, len(closeList)):
        pctChangeList.append((float(closeList[i]) - float(closeList[i - 1])) * 100 / float(closeList[i - 1])) #! i should start with 1 because the percent change could not be extracted from the very first day.
        
    return pctChangeList


#=======================================================

# Source: https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals

def dailyPriceRange_test():

    highList = ["13299.92969", "13303.63965", "13776.51953"]
    lowList = ["13303.63965", "13742.58984", "13701.62988"]
    
    rangeList = dailyPriceRange(highList, lowList)
    
    assert len(rangeList) == 3, "dailyPriceRange should return a list length or three"
    assert rangeList != None, "The returned list from dailyPriceRange should be None"
    
    
    highList = ["10", "20", "30"]
    lowList = ["5", "15", "25"]
    result = dailyPriceRange(highList, lowList)
    answer = [5.0, 5.0, 5.0]
    assert result == answer, f"The result should be {answer}, but got {result}"

    highList = ["10"]
    lowList = ["5"]
    result = dailyPriceRange(highList, lowList)
    answer = [5.0]
    assert result == answer, f"The result should be {answer}, but got {result}"

    highList = ["110.5", "120.3", "130.9"]
    lowList = ["110.0", "120.0", "130.0"]
    result = dailyPriceRange(highList, lowList)
    answer = [0.5, 0.3, 0.9]
    assert result == answer, f"The result should be {answer}, but got {result}"

    highList = []
    lowList = []
    result = dailyPriceRange(highList, lowList)
    answer = []
    assert result == answer, f"The result should be {answer}, but got {result}"
    

    print("dailyPriceRange passes all tests.")
    
    
def percentageChange_test():

    closeList = ["13776.51953", "13701.62988", "13299.92969"]
    
    pctChangeList = percentageChange(closeList)
    
    assert len(pctChangeList) == 2, "pctChangeList should return a list length or two"
    assert pctChangeList != None, "The returned list from pctChangeList should be None"
    
    
    closeList = ["100", "110", "121"]
    result = percentageChange(closeList)
    answer = [10.0, 10.0]
    assert result == answer, f"The result should be {answer}, but got {result}"

    closeList = ["100"]
    result = percentageChange(closeList)
    answer = []
    assert result == answer, f"The result should be {answer}, but got {result}"

    closeList = ["100.0", "105.0", "110.25"]
    result = percentageChange(closeList)
    answer = [5.0, 5.0]
    assert result[0] == 5.0, f"The result should be {answer[0]}, but got {result[0]}"
    assert result[1] == 5.0, f"The result should be {answer[1]}, but got {result[1]}"

    closeList = []
    result = percentageChange(closeList)
    answer = []
    assert result == answer, f"The result should be {answer}, but got {result}"

    
    print("percentageChange passes all tests.")
    


if __name__ == "__main__":
    dailyPriceRange_test()
    percentageChange_test()
