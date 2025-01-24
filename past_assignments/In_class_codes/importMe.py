'''
    This module is here to show off how 
    __name__ checking can affect import behaviour
'''

def fun():
    print("\nI'm what is actually supposed to be doing things!\n")


def main():
    print("\nI'm printing and making a mess!\n")


if __name__ == "__main__": 
    main()
