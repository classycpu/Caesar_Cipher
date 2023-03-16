# Coursework Assessment 1
# Name: Nishka Sardar
# Student No: 2200421

import os.path

def welcome():
    print("Welcome to the Ceasar Cipher")
    print("This program encrypts and decrypts text with the Caesar Cipher")

def enter_message():  #Asks the user for the mode, message and shift number
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d): ")
        if mode == "e":
            message = input("What message would you like to encrypt: ")
            message = message.upper()
            try:
                shift = int(input("What is the shift number: "))
                return (mode, message, shift)
            except (TypeError, ValueError):
                print("Please enter a number")           
        elif mode == "d":
            message = input("What message would you like to decrypt: ")
            message = message.upper()
            try:
                shift = int(input("What is the shift number: "))
                return (mode, message, shift)
            except (TypeError, ValueError):
                print("Please enter a number")
        else:
            print("Invalid mode")

def encrypt(message,shift):
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    new_message = ""
    for ch in message:
        if ch.isalpha():  #Will encrypt characters in message if they are in alphabet
            ch = ch.upper()
            i = alphabet.index(ch) + shift
            if i > 25:
                i = i - 26
            new_message = new_message + alphabet[i]  #Adds encrypted character onto the new_message string
        else:
            new_message = new_message + ch
    print(new_message)
    return new_message

def decrypt(message,shift):
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    shift = shift * -1
    new_message = ""
    for ch in message:
        if ch.isalpha():
            ch = ch.upper()
            i = alphabet.index(ch) + shift
            if i < 0:
                i = i + 26
            new_message = new_message + alphabet[i]
        else:
            new_message = new_message + ch
    print(new_message)
    return new_message

def process_file(filename, mode, shift):  #encrypts the writing in a file
    list_messages = []
    try:
        shift = int(input("What is the shift number: "))
    except (TypeError, ValueError):
        print("Please enter a number.")
        process_file(filename,mode,shift)
    mode = input("Encrypt (e) or decrypt (d): ")
    if (mode != "e") and (mode != "d"):
        print("Invalid mode.")
        process_file(filename,mode,shift)
    filename = input("Enter a file name: ")
    if is_file(filename) == False:
        print("Invalid file name.")
        process_file(filename, mode, shift)
    else:
        file = open(filename,"r")
        for line in file:
            print(line)
            if mode == "e":
                line = encrypt(line,shift)  #Encrypts/decrypts each line of the file
            elif mode == "d":
                line = decrypt(line,shift)
            list_messages.append(line)  #Adds to list of strings to be written to results.txt
        write_messages(list_messages)
        file.close()
    return (filename, mode, shift, list_messages)


def write_messages(list_messages):  #writes a list of strings to a file called results.txt
    file = open("results.txt","w")
    for line in list_messages:
        file.write(line+"\n")
    print("Output written in results.txt")
    file.close()
    return

def is_file(filename):
    return os.path.isfile(filename)  #Checks if file exists

def message_or_file():
    mode = ''
    filename = None
    message = None
    shift = 0
    source = input("Would you like to read from a file (f) or the console (c): ")  #Calls different functions based on user input  
    if source == "c":
        mode, message, shift = enter_message()
        if mode == "e":
            new_message = encrypt(message,shift)
        if mode == "d":
            new_message = decrypt(message,shift)            
    elif source == "f":
        process_file(filename,mode,shift)
    else:
        message_or_file()
    return (mode, message, filename, shift)

"""
MAIN DRIVER FUNCTION
----------------------------------------------------------------------------------------------
Requirements:
    • Prompt users to select a mode: encrypt (e) or decrypt (d).
    • Check if the mode the user entered is valid.
    If not, continue to prompt the user until a valid mode is selected.
    • Prompt the user for the message they would like to encrypt/decrypt.
    • encrypt/decrypt the message as appropriate and print the output.
    • Prompt the user whether they would like to encrypt/decrypt another message.
        • Check if the user has entered a valid input (y/n).
          If not, continue to prompt the user until they enter a valid response.
          Depending upon the response you should either:
            • End the program if the user selects no.
            • Proceed directly to step 2 if the user says yes.
"""

def main():
    welcome()
    message_or_file()
    while True:
        choice = input("Do you want to encrypt or decrypt another message (y/n): ")
        if choice == "y":
            message_or_file()
        elif choice == "n":
            print("Thanks for using the program, Goodbye!")
            break
        else:
            print("Invalid choice")
    return

# Program execution begins here
if __name__ == "__main__":
    main()
    
