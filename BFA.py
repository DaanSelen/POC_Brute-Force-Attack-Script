import random
import pyautogui
import string
import time

chars = string.printable
guesses = ""
chars_list = list(chars)
guesses_list = list(guesses)

def timeCalc(startTime):
    endTime = time.time()
    elapsedTime = endTime - startTime
    print("Cracking your password took: ", elapsedTime, " seconds")

password = pyautogui.password("Enter a password: ")

startTime = time.time()

guess_password = ""


while(guess_password != password):
    guess_password = random.choices(chars_list, k=len(password))
    if guess_password != guesses_list:
        print("<="+ str(guess_password)+ "=>")

    if guess_password != list(password):
        guess_password += guesses_list


    if(guess_password == list(password)):
        print("Your password is: "+ "".join(guess_password))
        timeCalc(startTime)
        break
input()
