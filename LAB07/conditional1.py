# getting info from user and saving it in this variable
userReply = input("Do you need to ship a package? (Enter yes or no) ")

# cheking the affirmative response and printing a message
if userReply == "yes": # == ->equal to
    print("We can help you ship that package!")
else: # if user enters 'no' the program prints another message
    print("Please come back when you need to ship a package. Thank you.")

