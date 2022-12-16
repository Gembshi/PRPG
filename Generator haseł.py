import random

print("Welcome to Python password generator!")
l = int(input("Input the lenght of you password: "))


lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPRQSTUVWXYZ"
number = "0123456789"
symbols = "!@#$%^&*()."

string = lower+upper+number+symbols

password = "".join(random.sample(string,l))


print("Your password is: " + str(password))