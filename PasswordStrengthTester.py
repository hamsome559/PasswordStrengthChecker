import re

common_passwords = set()

#reads the first file line by line
with open("rockyou_1.txt","r", encoding="latin-1") as file:
    common_passwords.update(line.strip() for line in file)
#same with the second one
with open("rockyou_2.txt","r", encoding="latin-1") as file:
    common_passwords.update(line.strip() for line in file)

#user input for password checker
password = input("Enter your password to be checked:")
#password has to be 8 lengths or more, Upper & Lower case, number and a special character
pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[_@$])[A-Za-z\d_@$]{8,}$"

if password in common_passwords:
    print("Password in common password list!! Not safe!")
elif re.fullmatch(pattern, password):
    print("Valid Password")
else:
    print("Invalid Passwords")


