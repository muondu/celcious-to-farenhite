print("Hi. I am a program which changes farenhite to celcious or vise versa")
what_temperature = input("""
These are the options available
a Farenhite to celcious
b Celious to Farenhite

""")
def logic():
    if what_temperature == "a":
        def farenhite_to_celcious():
            x = int(input("Insert a value in Farenhite:  "))
            if x != int() or x != float():
                print("Must be a number or a decimal")
            else:
                x = round(x - 32 * (5/9))
                print(str(x) +  "C")
        farenhite_to_celcious()
    elif what_temperature == "b":
        def celcious_to_farenhite():
            x = int(input("Insert a value in Farenhite:  "))
            if x != int() or x != float():
                print("Must be a number or a decimal")
            else:
                x = round(x * (9/5) + 32)
                print(str(x) +  "F")
        celcious_to_farenhite()
                
    else:
        print("Wrong input")
        logic()
logic()    