from datetime import datetime
import os


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

screenClean()

# creation of a file
with open(f"rec_{dte}.txt", "w") as f:
    f.write(f'Recording date: {start_time.strftime("%Y-%m-%d %H:%M:%S")}\n\n')
    f.write("00:00:00 Inicio de la clase\n")


# while
while True:
    with open(f"rec_{dte}.txt", "a") as f:
        # note or exit
        note = input("Write your note (e for exit):\n")
        lap = datetime.now()
        delta = lap - start_time
        lastTime = origen_time + delta
        newLine = f'{lastTime.strftime("%H:%M:%S")} {note}\n'

        if note == "e" or note == "E":
            break
        else:
            # print to file
            f.write(newLine)

    with open(f"rec_{dte}.txt", "r") as f:
        content = f.read()
        screenClean()
        print(content)


# inicio de la clase en el delta tiempo = 00:00:00
# bucle con input con nota para el lap(opciones: nota, pausa, exit)
# carga del tiempo y nota a un archivo y pantalla
# salida del bucle
