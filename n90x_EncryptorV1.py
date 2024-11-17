# N90X v1. Encryptor 
# NetScalerTrainer
# www.n90x.info
#
import os
import random
import string
import sys
from cryptography.fernet import Fernet
from datetime import date


# This function generates a new key, saves it to a file, and returns the filename
def generate_key():
    # Generate Fernet key
    key = Fernet.generate_key()
    fernet = Fernet(key)

    # Save the key to a file
    today = date.today()
    filename = 'key.' + str(today)
    with open(filename, 'wb') as f:
        f.write(key)
    print(f"Key saved to file: {filename}")
    print(
        "Rename and BACK UP THIS KEY - as you will need it to ENCRYPT/DECRYPT")
    return (filename)


# This function encrypts a file using the specified key
def encrypt_file(key):
    # Encrypt the plain text
    fernet = Fernet(key)
    # SELECT FILE TO ENCRYPT
    # Prompt user for file path *if it exists*
    file_name = input("Enter filename to be ENCRYPTED: ")
    if os.path.exists(file_name):
        with open(file_name, "rb") as file_to_encrypt:
            encrypted_data = fernet.encrypt(file_to_encrypt.read())
    else:
        print("File not found")
        #sys.exit()
        return ()
        # Save the encrypted file with a new suffix
        encrypted_file_name = file_name + ".encrypted"
        with open(encrypted_file_name, "wb") as encrypted_file:
            encrypted_file.write(encrypted_data)
        print(
            f"File '{file_name}' successfully encrypted as '{encrypted_file_name}'"
        )


# This function decrypts a file using the specified key
def decrypt_file(key):
    # Decrypt the file
    # SELECT FILE TO DECRYPT
    file_name = input("Enter filename to be DECRYPTED: ")
    # Read in the encrypted text file *if it exists*
    if os.path.exists(file_name):
        with open(file_name, "rb") as file:
            encrypted_text = file.read()
    else:
        print("File '{}' does not exist".format(file_name))
        #sys.exit()
        return ()
        #Get the KEY back
    fernet = Fernet(key)
    # Decrypt the encrypted text
    plain_text = fernet.decrypt(encrypted_text)

    # Save the decrypted file with a new suffix
    decrypted_file_name = file_name + ".clear"
    with open(decrypted_file_name, "wb") as decrypted_file:
        decrypted_file.write(plain_text)
    print(
        f"File '{file_name}' successfully encrypted as '{decrypted_file_name}'"
    )
    # Display the decrypted text on the screen in notepad (Windows) or textedit (macOS)
    #if sys.platform == "win32":
    #    os.system("notepad.exe {}".format(plain_text))
    #elif sys.platform == "darwin":
    #    os.system("open -e {}".format(plain_text))


def main():
    # Print a menu
    print('1) Generate a new key')
    print('2) Encrypt a file')
    print('3) Decrypt a file')
    print('Enter a number to select an option:')

    # Read the user's choice
    choice = input()

    # Generate a new key
    if choice == '1':
        filename = generate_key()
        print(f'Generated new key and saved it to {filename}')

    # Encrypt a file
    elif choice == '2':
        # Prompt user for file path
        file_name = input("Enter file path to key to use for encryption: ")
        if os.path.exists(file_name):
            # Get the key to encrypt
            with open(file_name, "rb") as key_file:
                key = key_file.read()
                encrypt_file(key)
        else:
            print(f"Key Filename {file_name} is not valid, or not found.")

    # Decrypt a file
    elif choice == '3':
        # Prompt user for file path
        file_name = input("Enter file path to KEY to use for DECRYPTION: ")
        if os.path.exists(file_name):
            #get key to decrypt
            with open(file_name, "rb") as key_file:
                key = key_file.read()
                decrypt_file(key)
        else:
            print(f"Key Filename {file_name} is not valid, or not found.")


main()
