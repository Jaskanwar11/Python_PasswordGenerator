import random
import string

pass_len = int(input("Enter password length: "))

def password():
    rand_num = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for n in 
    range(pass_len)])

    print(rand_num)

password()

while True:
    choice = input("Do you want to change password(Y/N)? ").lower()
    if choice in "y":
        password()

    elif choice in "n":
        break

    else:
        print("Invalid input!!")
