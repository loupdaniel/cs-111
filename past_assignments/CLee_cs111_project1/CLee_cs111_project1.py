g = -1.62

u = input("Which quantity is unkown? ")

if u == "t":
    h = float(input("Which is h? "))
    v = float(input("Which is v? "))
    a = float(input("Which is a? "))
    res_1 = ((-1)*v+((v**2-4*((g+a)/2)*h)**0.5))/(2*((g+a)/2)) # Bug fixed by wrapping the denominator with parenthesis
    res_2 = ((-1)*v-((v**2-4*((g+a)/2)*h)**0.5))/(2*((g+a)/2))
    if res_1 < 0 and res_2 < 0:
        print("Given inputs are not valid.")
    if res_1 > 0 and res_2 < 0:
        if (g+a)>=-49 and (v+(g+a)*res_1)>=-10 and (v+(g+a)*res_1) <= 0:
            res_1 = str(res_1)
            print("The value of t is "+ res_1)
            print("The landing is safe.")
        else:
            res_1 = str(res_1)
            print("The value of t is "+ res_1)
            print("The landing is unsafe.")
    if res_1 < 0 and res_2 > 0:
        if (g+a)>=-49 and (v+(g+a)*res_1)>=-10 and (v+(g+a)*res_1) <= 0:
            res_2 = str(res_2)
            print("The value of t is "+ res_2)
            print("The landing is safe.")
        else:
            res_2 = str(res_2)
            print("The value of t is "+ res_2)
            print("The landing is unsafe.")
    if res_1 > 0 and res_2 > 0:
        if (g+a)>=-49 and (v+(g+a)*res_1)>=-10 and (v+(g+a)*res_1)<=0:
            res_1 = str(res_1)
            print("The value of t is "+ res_1)
            print("The landing is safe.")
        else:
            if (g+a)>=-49 and (v+(g+a)*res_2)>=-10 and (v+(g+a)*res_2)<=0:
                res_2 = str(res_2)
                print("The value of t is "+ res_2)
                print("The landing is safe.")
            else:
                res_1 = str(res_1)
                res_2 = str(res_2)
                print("The value of t is either "+ res_1 + " or " + res_2)
                print("The landing is unsafe.")


if u == "h":
    v = float(input("Which is v?"))
    a = float(input("Which is a?"))
    t = float(input("Which is t?"))
    res=(-1)*(v*t + ((g+a)/2)*t**2)
    if (g+a)>=-49 and (v+(g+a)*t)>=-10 and (v+(g+a)*t)<=0:
        res = str(res)
        print("The value of h is " + res)
        print("The landing is safe.")
    else:
        res = str(res)
        print("The value of h is " + res)
        print("The landing is unsafe.")
    
if u == "v":
    h = float(input("Which is h?"))
    a = float(input("Which is a?"))
    t = float(input("Which is t?"))
    if t == "0":
        print("0 for the value of t is not allowed!")
    res=((-1)*(h+((g+a)/2)*t**2))/t
    if (g+a)>=-49 and (res+(g+a)*t)>=-10 and (res+(g+a)*t)<= 0:
        res = str(res)
        print("The value of v is " + res)
        print("The landing is safe.")
    else:
        res = str(res)
        print("The value of v is " + res)
        print("The landing is unsafe.")
    
if u == "a":
    h = float(input("Which is h?"))
    v = float(input("Which is v?"))
    t = float(input("Which is t?"))
    res=(-1)*(2*h+2*v*t+g*t**2)/t**2
    if (g+res)>=-49 and (v+(g+res)*t)>=-10 and (v+(g+res)*t)<=0:
        res = str(res)
        print("The value of a is " + res)
        print("The landing is safe.")
    else:
        res = str(res)
        print("The value of a is " + res)
        print("The landing is unsafe.")
