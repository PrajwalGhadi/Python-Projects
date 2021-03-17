from pygame import mixer
from time import time
from datetime import datetime
def music_on_loop(file, stopper):

    mixer.init()
    mixer.music.load(file)
    mixer.music.play()

    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break

def log_msg(msg):

    with open('MyLog.txt', 'a') as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':

    # music_on_loop('Struggle.mp3', 'stop')
    init_Water = time()
    init_eye = time()
    init_exercise = time()

    watermin = 5
    eyemin = 30 * 60
    exercise = 45 * 60

    while True:

        if time() - init_Water > watermin:

            music_on_loop('Struggle.mp3', 'Drank')
            init_Water = time()
            log_msg('Drank Water at: ')

        if time() - init_eye > eyemin:

            music_on_loop('Struggle.mp3', 'EyDone')
            init_eye = time()
            log_msg('EyDone At: ')

        if time() - init_exercise > exercise:

            music_on_loop('Struggle.mp3', 'ExDone')
            init_exercise = time()
            log_msg('ExDone')

