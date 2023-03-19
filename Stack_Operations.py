hostk = []
def pushstack():
    while True:
        hostelno = int(input("Enter number of hostel:"))
        totstud = int(input("Enter Numeber of students: "))
        totroom = int(input("Enter number of rooms: "))
        P = [hostelno,totstud,totroom]
        hostk.append(P)
        ans = input("Enter do u want 2 add more y/n: ")
        if ans == 'n' or ans=='N':
            break
        else:
            pass
    print(hostk)
    
def popstack():
    global hostk
    if len(hostk) == 0:
        print("Stack Empty")
    else:
        end = len(hostk) - 1
        z = hostk.pop(end)
        print("Element popped was:",z)
        print(hostk)

pushstack()
popstack()