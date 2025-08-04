import string

def encrypt_decrypt(keimeno, mode, kleidi):
    grammata = string.ascii_lowercase
    num_letters = len(grammata)
    apotelesma = ''
    kleidi = kleidi % num_letters
    if mode == 'd':
        kleidi = -kleidi

    for char in keimeno:
        if char.isalpha():
            if char.isupper():
                start = ord('A')
            else:
                start = ord('a')

            new_position = (ord(char) - start + kleidi) % 26
            apotelesma += chr(start + new_position)
        else:
            apotelesma += char

    return apotelesma
def get_valid_key():
    while True:
        try:
            key = int(input('Enter a key (1 through 25): '))
            if 1 <= key <= 25:
                return key
            else:
                print("Key must be between 1 and 25. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 25.")
def main():
    while True:
        print("1. Kryptografhsh mhnymatos")
        print("2. Apokryptografhsh mhnymatos")
        print("3. Exodos")

        epilogi = input("Pliktrologiste 1,2 h 3 ")

        if epilogi == '1':
            kleidi = get_valid_key()
            keimeno = input('Eisagete to keimeno pros kryptografhsh ')
            ciphertext = encrypt_decrypt(keimeno, 'e', kleidi)
            print(f'Kryptografhmeno mhnyma: {ciphertext}')

        elif epilogi == '2':
            kleidi = get_valid_key()
            keimeno = input('Eisagete to keimeno pros apokryptografhsh ')
            plaintext = encrypt_decrypt(keimeno, 'd', kleidi)
            print(f'Apokryptografhmeno mhnyma: {plaintext}')

        elif epilogi == '3':
            print("Ginetai exodos...")
            break

        else:
            print("Mporeite na epilexete mono 1,2 h 3")

if __name__ == "__main__":
    main()