# capturing input from user
userReply = input( "Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")

# printing a different message according to the different 3 possibilities:
if userReply == "stamps":
    print("We have many stamp designs to choose from.")
elif userReply == "envelope":
    print("TWe have many envelope sizes to choose from.")
elif userReply == "copy":
    copies = input("How many copies would you like? ( Enter a number)")
    print("Here are {} copies.".format(copies)) # embedding variables with string with format()
    # print(f'Here are {copies} copies.') # another way to do the same
else:
    print("Thank you, please come again.")