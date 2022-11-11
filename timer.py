import time
print("WELCOME TO TIMER WATCH")
t = int(input("enter the timer in seconds : "))
while t != 0:

    print(f'{str(t//60).zfill(2)}:{str(t%60).zfill(2)}', end="\r")
    time.sleep(1)
    t = t-1
