from ADeLaCruzCLeeIWall_cs111_final_fileUtils import selectedIndex
from ADeLaCruzCLeeIWall_cs111_final_fileUtils import writeCSV
from ADeLaCruzCLeeIWall_cs111_final_analysis import dailyPriceRange
from ADeLaCruzCLeeIWall_cs111_final_analysis import percentageChange
from ADeLaCruzCLeeIWall_cs111_final_plot import plotter

exchanges = ["IXIC", "HSI", "GDAXI", "J203.JO", "N225"]

while True:
    
    # Source: https://www.w3schools.com/python/python_user_input.asp
    indexName = input("Select one stock exchange by typing the index (IXIC, HSI, GDAXI, J203.JO, N225): ")
    
    if indexName in exchanges:
        break

resFileName = input("Type your desired file name for the volatility result file.\nYou do not need to specify the file format as the default file type would be .csv: ")


indexList, dateList, openList, highList, lowList, closeList = selectedIndex(indexName)


rangeList = dailyPriceRange(highList, lowList)
pctChangeList = percentageChange(closeList)

writeCSV(resFileName, rangeList, pctChangeList)

plotter(indexName, dateList, rangeList, pctChangeList, closeList)