from datetime import datetime, timedelta
import os
from pathlib import Path
from textwrap import indent
from zmq import NULL

# Build paths inside the project like this: BASE_DIR / 'subdir'.


# screen clear function
def screenClean():
    # For Windows
    if os.name == "nt":
        _ = os.system("cls")
    # for Linux and Mac
    else:
        _ = os.system("clear")


# start time
start_time = datetime.now()
origen_time = datetime(1, 1, 1, 0, 0, 0)
dte = start_time.strftime("%Y%m%d")
pauseDelta = NULL
tabla_speed = {
    "a": 1,
    "b": 1.25,
    "c": 1.5,
    "d": 2,
}
while True:
    spSelection = input(
        "a) speed 1x\nb) speed 1.25x\nc) speed 1.5x\nd) speed 2x\n\nSpeed video reproduction: "
    )
    if tabla_speed.get(spSelection):
        speedVideo = tabla_speed[spSelection]
        break
    else:
        screenClean()
        print("speed not valid")

screenClean()

# creation of a file and writing first lines
with open(f"rec_{dte}.txt", "a+") as f:
    f.write(f'Recording date: {start_time.strftime("%Y-%m-%d %H:%M:%S")}\n\n')
    f.write("00:00:00 Inicio de la clase\n")

# variable with current directory's path
BASE_DIR = Path("rec_{dte}.txt").resolve().parent

# while (infinity loop)
while True:
    """
        file creation or write a line if file exist
        file's name has format: 'rec_yyyymmdd.txt\' 
    """
    with open(f"rec_{dte}.txt", "a+") as f:
        # note or exit
        note = input("Write your section's name ('e' for exit or 'p' for pause):\n")
        lap = datetime.now()
        delta = lap - start_time
        if delta > timedelta(seconds=10):
            delta -= timedelta(seconds=10)

        lastTime = origen_time + (delta * speedVideo)

        # after a paused
        if pauseDelta != NULL:
            pauseTime = delta - pauseDelta
            start_time += pauseTime
            lastTime -= pauseTime
            pauseDelta = NULL
            newLine = f"{note}\n"
        # whitout pause
        else:
            newLine = f'{lastTime.strftime("%H:%M:%S")} {note}\n'

        # exit option
        if note == "e" or note == "E":
            f.write(f"\nThe file's path is: {BASE_DIR}/rec_{dte}.txt")
            f.seek(0)
            content = f.read()
            screenClean()
            print(content)
            break

        # pause option
        elif note == "p" or note == "P":
            pauseDelta = delta
            newLine = f'{lastTime.strftime("%H:%M:%S")} Recording Paused... '
            f.write(newLine)

        # note option
        else:
            # print to file
            f.write(newLine)

        # clear the screen and show the file content for each  of the iterations
        # with open(f"rec_{dte}.txt", "r") as f:
        f.seek(0)
        content = f.read()
        screenClean()
        print(content)

# final display the content of the file on the screen
with open(f"rec_{dte}.txt", "r") as f:
    content = f.read()
    screenClean()
    print(content)
