import secrets
import string

pwQuestion = input("Do you want to generate a password? Yes (Y) or No (N): ")
def main():
    if (pwQuestion == "Y" or pwQuestion == "y"):
        lenPassword = int(input("Enter the password length you want: "))
        alphabet = string.ascii_letters + string.digits + "!@#$%^&*()"
        password = ''.join(secrets.choice(alphabet) for i in range(lenPassword))
        print("Here's your password: " , password)
    elif (pwQuestion == "N" or pwQuestion == "n"):
        exit()
    else:
        print("Please enter right response")

