lookup_table = {'A' : 'Z', 'B' : 'Y', 'C' : 'X', 'D' : 'W', 'E' : 'V',
        'F' : 'U', 'G' : 'T', 'H' : 'S', 'I' : 'R', 'J' : 'Q',
        'K' : 'P', 'L' : 'O', 'M' : 'N', 'N' : 'M', 'O' : 'L',
        'P' : 'K', 'Q' : 'J', 'R' : 'I', 'S' : 'H', 'T' : 'G',
        'U' : 'F', 'V' : 'E', 'W' : 'D', 'X' : 'C', 'Y' : 'B', 'Z' : 'A'}

def atbash(message):
    cipher = ''
    for letter in message:
        # checks for space
        if(letter != ' '):
            #adds the corresponding letter from the lookup_table
            cipher += lookup_table[letter]
        else:
            # adds space
            cipher += ' '

    return cipher

# Driver function to run the program
def main():
   while True:
    print("This is a program using atbash cipher.")
    print("Press 1 to encrypt, 2 to decrypt or 3 to exit.")
    epilogi = input("Your choice: ")
    if epilogi == '1':
            message = input('Enter text for encryption: ')
            print(atbash(message.upper()))

    elif epilogi == '2':
            message = input('Enter text for decryption: ')
            print(atbash(message.upper()))

    elif epilogi == '3':
            print("Exiting...")
            break
    else:
            print("You can only choose 1,2 or 3")



# Executes the main function
if __name__ == '__main__':
    main()
