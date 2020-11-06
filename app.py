command = ""
started = False
while True :
    command = input("> ").lower()
    if command == "start":
        if started:
            print("The car is already started")
        else:
            started = True
            print("Car started and ready to go !!!")
    elif command == "stop":
        if not started:
            print("Car has already stopped ! ! !")
        else:
            started = False
        print("Car has stopped.")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit the game""")
    elif command == "quit":
        print("You quit the game.")
        break
    else:
        print("Sorry, I don't understand that !")

