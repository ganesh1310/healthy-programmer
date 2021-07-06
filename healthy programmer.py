# healthy programmer :
# consider a emplyoee working in time 9 am to 5 pm and for his health conciousness you have to suggest some remedies
# him like water drinking,eye test and other physical activities as a healthy programmer.

# water : he should drink atleast 3.5 ltr water per day
# eye test : for eye test creat eyes.mp3 file fot check
# physical test : physical test also checked by physical.mp3 file in given directory
# here we use Pygame module to play audio (mp3 files)



from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    # musiconloop("water.mp3", "stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 40*60
    exsecs = 30*60
    eyessecs = 45*60

    while True:
        if time() - init_water > watersecs:
            print("Water Drinking time. Enter 'drank' to stop the alarm.")
            musiconloop('water.mp3', 'drank')
            init_water = time()
            log_now("Drank Water at")

        if time() - init_eyes >eyessecs:
            print("Eye exercise time. Enter 'doneeyes' to stop the alarm.")
            musiconloop('eyes.mp3', 'doneeyes')
            init_eyes = time()
            log_now("Eyes Relaxed at")

        if time() - init_exercise > exsecs:
            print("Physical Activity Time. Enter 'donephy' to stop the alarm.")
            musiconloop('physical.mp3', 'donephy')
            init_exercise = time()
            log_now("Physical Activity done at")




