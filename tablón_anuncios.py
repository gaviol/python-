def mostrar_menu():
    print('Seleccione el proceso que desea aplicar')
    print('1: Ingresar puntuación y comentario')
    print('2: Comprobar los resultados obtenidos hasta ahora.')
    print('3: Finalizar')
    return input()

def ingresar_puntuacion_comentario():
    while True:
        print('Por favor, introduzca una puntuación en una escala de 1 a 5')
        point = input()
        
        if point.isdecimal():
            point = int(point)
            if point < 1 or point > 5:  # Validar que esté entre 1 y 5
                print('Por favor, introduzca un valor entre el 1 y 5')
            else:
                print('Por favor, introduzca un comentario')
                comment = input()
                guardar_puntuacion_comentario(point, comment)
                break  # Salir del bucle al ingresar correctamente
        else:
            print('Por favor, introduzca la puntuación en números')

def guardar_puntuacion_comentario(point, comment):
    post = f'punto: {point} comentario: {comment}'
    with open("data.txt", 'a') as file_pc:  # Usar with para asegurar el cierre correcto
        file_pc.write(f'{post}\n')

def mostrar_resultados():
    try:
        with open("data.txt", "r") as read_file:
            contenido = read_file.read()
            if contenido:
                print(contenido)
            else:
                print("No hay resultados disponibles.")
    except FileNotFoundError:
        print("No hay resultados disponibles.")

def validar_opcion_menu():
    while True:
        num = mostrar_menu()
        if num.isdecimal():
            num = int(num)
            if num == 1:
                ingresar_puntuacion_comentario()
            elif num == 2:
                mostrar_resultados()
            elif num == 3:
                print('Finalizando')
                break
            else:
                print('Por favor, introduzca un número del 1 al 3')
        else:
            print('Por favor, intro11duzca un número del 1 al 3')

# Llamada principal
if __name__ == "__main__":
    validar_opcion_menu()
