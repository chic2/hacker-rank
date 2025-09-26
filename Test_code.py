while True: 
    
    
    try:
        number = int(input("number you like: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue
    print("i love " + str(number))
    if number == 3:
        print("me too")
    else:
        print("let try again")
    try:
        number = int(input("number you like: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue
    print("i love " + str(number))
    try:
        for i in range(number):
            print("i love " + str(number))
    except ValueError:
        print("Invalid number for loop.")
        
        
        

    print("loop finished")
    break
