def menu():
    options = ["Exit", "Add an option", "Remove an option"]
    
    while (True):
        print("Here is your menu!")
        print("Pick a number 0-2")

        i = 0
        for option in options:
            print(str(i) + ". " + option)
            i += 1

        print("")
        
        userInput = int(input("Your choice >>> "))

        if (userInput == 0):
            break
        elif (userInput == 1):
            options.append(input("New option: "))
        elif (userInput == 2):
            optionToPop = input("Option to remove: ")
            if (not optionToPop.isdigit() or int(optionToPop) <= 2 or
                int(optionToPop) >= len(options)):
                print("Invalid option!\n")
            else:
                options.pop(int(optionToPop))
        else:
            print("Invalid option")
            
        
    print("Goodbye!")
