# INET4031 Module 1
#
# User List Processing Program
#
# Created: Nov 11, 2024
# Updated: Jan 6, 2025


def main():
    # Open the user list file
    try:
        userFile = open("list-of-users.txt", "r")  # <-- Spelling error here ("sers" instead of "users")
    except:
        print("\nCould not read the file specified.\n")
        exit()

    # Load the lines of the file into a list
    listOfUsers = userFile.readlines()
    print("\nlist-of-users was read.")

    # Ask the user to proceed
    answer = input("\nDo you want to print out the list of users? (Y or N)")

    if answer == "Y" or answer == "y":
        for userline in listOfUsers:
            print("\n", userline)
    else:
        print("\nOk not printing, ending program.")

    print("\nEnd of User Processing\n")

main()



