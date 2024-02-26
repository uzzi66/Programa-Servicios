#importamos las guientes librerias para obtener del sistema el programa a bloquear y para realizar el bloqueo
import sys
import psutil

#debemos establecer que el programa requiere de argumentos, así que lo validamos
def check_arguments():
    if len(sys.argv) == 1:
        print('Este programa no funciona sin argumentos')
        sys.exit(0)


#definimos el programa a bloquear, tomará el que indiquemos al correr el programa en terminal
def get_targets():
    targets = sys.argv[1:]
    i = 0
    while i < len(targets):
        if not targets[i].endswith('.exe'):
    	    targets[i] = targets[i] + '.exe'
        i += 1
    return targets


#con la función lower nos aseguramos de no fallar al encontrar el programa por mayusculas o minusculas
def lock(target):
    for proc in psutil.process_iter():
    	if proc.name().lower() == target.lower():
    		proc.kill()


if __name__ == '__main__':

    check_arguments()
    targets = get_targets()

    while True:
    	for target in targets:
    		lock(target)