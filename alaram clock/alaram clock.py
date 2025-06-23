import datetime
import time
from playsound import playsound


def alaram_clock(set_time):
    print(f"Alaram set for {set_time}...")

    while True:
        current_time=datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == set_time:
             print("Wakey! Wakey!")
             playsound("alaram.mp3")
             break
        time.sleep(1)

alaram_time=input("Enter alaram time(HH:MM:SS):")
alaram_clock(alaram_time)