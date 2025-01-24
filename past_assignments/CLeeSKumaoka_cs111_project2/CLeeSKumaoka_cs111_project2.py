# DO NOT EDIT FOLLOWING SECTION
import turtle
from temp_preprocess import set_up

days,aveMinMonthly,aveMinYearly,aveMin,dims = set_up()
screen = turtle.Screen()
screen.title('Temperature Visualization')
screen.setup(1000, 1000)
llx, lly, urx, ury = dims
screen.setworldcoordinates(llx, lly, urx, ury)
turtle.speed(0)
# DO NOT EDIT ABOVE SECTION

# Iterate through the iterables named aveMinMonthly and aveMinYearly
# to plot average temperature readings as described in the project writeup.
# Also plot aveMin, the average minimum temperature across all data.
# Note that you already have a turtle for these purposes---its name is "turtle".

# PUT YOUR CODE BELOW THIS LINE

green = turtle.Turtle()
green.speed(0)

green.pensize(3)
green.pencolor("navy")
green.penup()
green.goto(0, aveMin)
green.pendown()
green.forward(days)


# To mark these data points, draw a line of the appropriate color
# and pensize from the previous data point to the new one. (Note that **the initial
# turtle position** is not a data point, so do not connect it to the data with a line.)

# Turtle not disappearing after plotting

green.pensize(1)
green.pencolor("sky blue")
monthCor = 0
green.penup()
for i in aveMinMonthly:
    monthCor = monthCor + 30 #31
    green.goto(monthCor, i)
    green.pendown()
    

green.pensize(2)
green.pencolor("blue")
yearCor = 0
green.penup()
for i in aveMinYearly:
    yearCor = yearCor + 365
    green.goto(yearCor, i)
    green.pendown()
    if i >= 0.5 + aveMin:
        green.dot(7, "red")


# print(str(days) + "\n") # giving the total number of days in the whole data set
# print(str(aveMinMonthly) + "\n") # containing the 30-day averages of minumum daily temperatures—this is the “monthly” data
# print(str(aveMinYearly) + "\n") # containing the 365-day averages of minumum daily temperatures—this is the “yearly” data
# print(str(aveMin) + "\n") # containing the average of minimum daily temperatures taken across the whole 90-ish year data set—this is the “century” data
# print(str(aveMin + 0.5) + "\n")
# print(str(dims) + "\n")

green.hideturtle()
turtle.hideturtle()
turtle.mainloop()
