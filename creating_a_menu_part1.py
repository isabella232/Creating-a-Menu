def menu():
     # declare list
     options = ["Watch tv", "Go to the park", "Take out the trash"]

     # loop forever until user types "exit"
     while (True):
          # print messages and menu
          print("Here is your list of options! Type \"exit\" to exit")

          for option in options:
               print(option)

          # get user input
          userResponse = input()

          # handle user input
          if (userResponse == "exit"):
               break

     # print exit message
     print("Goodbye!")
