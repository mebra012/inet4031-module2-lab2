# INET4031 Module 1
#
# User List Processing Program
#
# Created: Nov 11, 2024
# Updated: Jan 6, 2025
#

import os

def main():
    expected_filename = "list-of-users.txt"

    # Check if the file exists before trying to open it
    if not os.path.exists(expected_filename):
        print(f"\nError: Expected file '{expected_filename}' not found.")
        print("\nFiles in the directory:")
        print("\n".join(os.listdir()))  # Print all files in the directory for debugging
        return

    try:
        with open(expected_filename, "r") as userFile:
            listOfUsers = userFile.readlines()
            print("\nFile opened successfully!\n")
    except Exception as e:
        print(f"\nUnexpected error: {e}\n")
        return

    answer = input("\nDo you want to print out the list of users? (Y or N) ")

    if answer.lower() == "y":
        for userline in listOfUsers:
            print("\n", userline)
    else:
        print("\nOk, not printing. Ending program.")

    print("\nEnd of User Processing\n")

main()



