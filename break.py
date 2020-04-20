#Example 1:
#while True:
#    command = input("Type 'exit' to exit: ")
#    if (command == "exit"):
#        break


#Example2:
times = int(input("How many times do I have to tell you? "))

for time in range(times):
    print("CLEAN UP YOUR ROOM!")
    if time >= 3:
        print("Do you even listen anymore?")
        break
