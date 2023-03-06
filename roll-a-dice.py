import random
response = "y"
while response == "y":
    no = random.randint(1,6)
    if no==1:
        print("[0]")
        
    elif no==2:
        print("[0 0]")
        
    elif no==3:
        print("[0 0 0]")
        
    elif no==4:
        print("[0 0 0 0]")
        
    elif no==5:
        print("[0 0 0 0 0]")
        
    else:
        print("[0 0 0 0 0 0]")

    response= input("press y to roll again and press n to exit: ")
    print("\n")


