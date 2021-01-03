from win10toast import ToastNotifier
import schedule
import time
from gtts import gTTS
from playsound import playsound
import os

toaster = ToastNotifier()
language = "en"


def water_reminder():
    print("Please Drink Water")
    message = "Hello Sir, Jarvis is at your service. It's time for you to drink a glass of water."
    my_speech_obj = gTTS(text=message, lang=language, slow=False)
    my_speech_obj.save("water_msg.mp3")
    toaster.show_toast("Water Reminder", message, duration=0)
    playsound("water_msg.mp3")
    os.remove("water_msg.mp3")


def break_reminder():
    print("It's Break time")
    message = "Hello Sir, Jarvis is again at your service. I think you should take a short break"
    my_speech_obj = gTTS(text=message, lang=language, slow=False)
    my_speech_obj.save("break_msg.mp3")
    toaster.show_toast("Break Reminder", message, duration=0)
    playsound("break_msg.mp3")
    os.remove("break_msg.mp3")


if __name__ == '__main__':
    schedule.every().hour.do(water_reminder)
    schedule.every(30).minutes.do(break_reminder)
    while True:
        schedule.run_pending()
        time.sleep(1)
