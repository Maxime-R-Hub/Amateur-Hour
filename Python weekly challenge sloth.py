# Thanks for reading my submission !

#First we'll define t1 and t2 and we put value errors in case someone tries putting letters... I see you here that tried...

try:
    t1=int(input("Take a time you start at : "))
except ValueError:
    print("That's not a time, try again...")
    exit()

try:
    t2=int(input("Take a time to finish at : "))
except ValueError:
    print("That's not a time, try again...")
    exit()

#Then we check for any incorrect values of times

if t1>12 or t1<1 or t2>12 or t2<1 or t1>t2:
    print("The value(s) entered are not valid, try again...")
    exit()

#And finally we check if the time passed is greater than 0 to choose the right phrase

if t2-t1 > 0 :
    print("There has been " + str(t2-t1) + " hours betwenn the two you entered")
else :
    print("No time passed")
