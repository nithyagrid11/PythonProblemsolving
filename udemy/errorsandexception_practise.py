'''try:
    for i in ['a','b','c']:
        print(i**2)
except:
    print("An error occured, Runtime error")'''
'''try: 
    x = 5
    y = 0
    z = x/y
except:
    print("Error, runtime error")'''


def ask():
    while True:
        try:
            input1 = int(input("Enter a number: "))
            print(input1 ** 2)
        except:
            print("Runtime error")
        else:
            print("Thank you")
            break
ask()

    