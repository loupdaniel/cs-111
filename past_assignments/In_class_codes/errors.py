x = 0
print()

try:
    #print(5/x)

    #print(y)

    #print(x(5))

    #print(int("5.0"))

    #assert x != 0, "Uh oh!"

    #print(x.append(5))

    #import y

    print("No exceptions happened!\n")


except ZeroDivisionError:
    print("Tried to divide by zero!")


except NameError:
    print("Tried to use a variable before it was defined!")


except TypeError:
    print("Tried to use some data in a way inconsistent with its type!")


except ValueError:
    print("Tried to use a disallowed input!")


except AssertionError:
    print("Failed an assertion check!")


except AttributeError:
    print("Tried to access some attribute/method that an object does not have!")


except ModuleNotFoundError:
    print("Tried to import a module that isn't accessible!")


else:
    print("I'm in an else block! I only print when no exceptions happen!")


finally:
    print()
    print("I'm in a finally block! I always print.")

print() 
print("I'm after the exception handling!")
print()