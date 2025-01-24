import matplotlib.pyplot as mpl


def plotter(stock:str, dateList:list, rangeList:list[float], changeList:list[float], closeList:list[float]):
    ''' Purpose: To plot 3 subplots that contain different information
                 on stock exchange votality data and the daily price
                 movement of the stock exchange that the user picked in main.py.
        Parameters:
                stock: index name of the stock selected by the user in main.py.
                dateList: list of dates recorded for the stock selected by the user
                rangeList: list of differences between the high and the low price of the day
                           for the stock selected by the user.
                changeList: list of the percent change from one day to another for the stock
                            selected by the user.
                closeList: list of prices at the end of each recored day for the stock selected
                           by the user.
        Return: none
    '''

    for date in range(len(dateList)):    #converts each date in dateList to a float
        dateList[date] = float(dateList[date][:4]) + (float(dateList[date][5:7]) + float(dateList[date][8:10]) / 31) / 12

    for price in range(len(closeList)):  #converts each price in closeList from a string to a float
          closeList[price] = float(closeList[price])


    def subPlotter1(ylimStart, ylimEnd):     #creates the first subplot
        '''Purpose: To create the first subplot, displaying the data of closeList
                    over time.
           Parameters: 
                ylimStart: the lowest y-value on the y-axis
                ylimEnd: the highest y-value on the y-axis
           Return: None
        '''

        mpl.subplot(3, 1, 1)
        mpl.plot(dateList, closeList, lw = .5)     #plots data with linewidth of .5
        mpl.xlim(dateList[0], dateList[-1])
        mpl.xlabel("Years")
        mpl.ylim(ylimStart, ylimEnd)
        mpl.ylabel("Daily Price")
        mpl.title("Price Movement of " + stock)

    def subPlotter2(ylimStart, ylimEnd):        #creates the second subplot
        '''Purpose: To create the second subplot, displaying the data of rangeList
                    over time.
           Parameters: 
                ylimStart: the lowest y-value on the y-axis
                ylimEnd: the highest y-value on the y-axis
           Return: None
        '''

        mpl.subplot(3, 1, 2)
        mpl.plot(dateList, rangeList, lw = .5)
        mpl.xlim(dateList[0], dateList[-1])
        mpl.xlabel("Years")
        mpl.ylim(ylimStart, ylimEnd)
        mpl.ylabel("Daily Price Range")
        mpl.title("Daily Price Range of " + stock)

    def subPlotter3(ylimStart, ylimEnd):     #creates the third subplot
        '''Purpose: To create the third subplot, displaying the data of changeList
                    over time.
           Parameters: 
                ylimStart: the lowest y-value on the y-axis
                ylimEnd: the highest y-value on the y-axis
           Return: None
        '''

        mpl.subplot(3, 1, 3)
        mpl.plot(dateList[1:], changeList, lw = .5)
        mpl.xlim(dateList[0], dateList[-1])
        mpl.xlabel("Years")
        mpl.ylim(ylimStart, ylimEnd)
        mpl.ylabel("Percent Change")
        mpl.title("Percentage Change of " + stock)



    #Creates graphs for United States (IXIC)
    if stock == "IXIC":
            subPlotter1(0, 14500)
            subPlotter2(0, 700)
            subPlotter3(-15, 15)
            mpl.suptitle("Data for " + stock)
            mpl.show()
    
    #Creates graphs for Hong Kong (HSI)
    if stock == "HSI":
            subPlotter1(0, 35000)
            subPlotter2(0, 2150)
            subPlotter3(-35, 20)
            mpl.suptitle("Data for " + stock)
            mpl.show()

    #Creates graphs for Japan (N225)
    if stock == "N225":
            subPlotter1(0, 40000)
            subPlotter2(0, 4300)
            subPlotter3(-16, 16)
            mpl.suptitle("Data for " + stock)
            mpl.show()

    #Creates graphs for Germany (GDAXI)
    if stock == "GDAXI":
            subPlotter1(0, 17000)
            subPlotter2(0, 950)
            subPlotter3(-14, 12)
            mpl.suptitle("Data for " + stock)
            mpl.show()

    #Creates graphs for South Africa (J203.JO)
    if stock == "J203.JO":
            subPlotter1(30000, 70000)
            subPlotter2(0, 5500)
            subPlotter3(-11, 9)
            mpl.suptitle("Data for " + stock)
            mpl.show()