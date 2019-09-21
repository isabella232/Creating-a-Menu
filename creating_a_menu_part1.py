def menu():
     options = ["Watch tv", "Go to the park", "Take out the trash"]
     while (True):
        print("Here is your list of options! Type \"exit\" to exit")

        for option in options:
            print(option)

        userResponse = input()
        
        if (userResponse == "exit"):
            break
        
    print("Goodbye!")
