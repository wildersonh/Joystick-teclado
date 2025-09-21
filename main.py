import pygame
import time
import keyboard
import tkinter as tk
import time
import threading

# Variable global para controlar el estado de la función
is_running = False

def my_function():
    """Función que queremos iniciar o detener."""
    global is_running
    while is_running:
        # Inicializar el módulo de joystick de Pygame
        pygame.init()
        pygame.joystick.init()
        if pygame.joystick.get_count() == 0:
            print("No hay joysticks conectados. Conecta uno para continuar.")
            time.sleep(3)
            # Aquí podrías salir del programa
        else:
            # Obtener el primer joystick
            joystick = pygame.joystick.Joystick(0)
            joystick.init()
            print(f"Joystick '{joystick.get_name()}' detectado. Presiona un botón.")

            # Bucle principal de eventos
            while True:
                # Procesar los eventos del joystick
                for event in pygame.event.get():
                    # Evento para cuando se presiona un botón
                    if event.type == pygame.JOYBUTTONDOWN:
                        print(f"¡Botón {event.button} presionado!")
                        if(event.button == 0):  
                            keyboard.press_and_release('space') 
                            # es A en un mando Xbox
                        if(event.button == 1): 
                            # es B en un mando Xbox
                            keyboard.press_and_release('w')
                        if(event.button == 2):  
                            # es X en un mando Xbox
                            keyboard.press_and_release('q')
                        if(event.button == 3): 
                            # es Y en un mando Xbox
                            keyboard.press_and_release('z')
                        if(event.button == 4): 
                            # es LB en un mando Xbox
                            keyboard.press_and_release('x')
                        if(event.button == 5): 
                            # es RB en un mando Xbox
                            keyboard.press_and_release('d')
                        if(event.button == 6): 
                            # es Back en un mando Xbox
                            keyboard.press_and_release('alt+tab')
                        if(event.button == 7): 
                            # es Start en un mando Xbox
                            keyboard.press_and_release('shift+n')

                    if event.type == pygame.JOYHATMOTION:
                        # El event.hat te dice qué "hat" (D-pad) se movió (0, 1, ...)
                        # El event.value te da la dirección del hat (tupla)
                        if event.hat == 0:
                            if event.value == (1, 0):
                                keyboard.press_and_release('f3')
                            if event.value == (-1, 0):
                                keyboard.press_and_release('f2')
                            if event.value == (0, 1):
                                keyboard.press_and_release('f5')
                            if event.value == (0, -1):
                                keyboard.press_and_release('f6')
                    # Evento para cuando se suelta un botón (opcional, pero útil)
                    if event.type == pygame.JOYAXISMOTION:
                        # El event.axis te dice qué eje se movió (0, 1, 2, ...)
                        # El event.value te da la posición del eje (-1.0 a 1.0)
                        if event.axis == 1:  # Eje Y del joystick izquierdo
                            if event.value < -0.5:
                                keyboard.press_and_release('up')
                            elif event.value > 0.5:
                                keyboard.press_and_release('down')
                        if event.axis == 0:  # Eje X del joystick izquierdo
                            if event.value < -0.5:
                                keyboard.press_and_release('left')
                            elif event.value > 0.5:
                                keyboard.press_and_release('right')

                    if event.type == pygame.JOYBUTTONUP:
                        print(f"Botón {event.button} soltado.")

                # Pausa para no saturar la CPU
                time.sleep(0.1)


def toggle_function():
    """Alterna el estado de la función y actualiza la interfaz."""
    global is_running
    if not is_running:
        # Si la función no está en ejecución, la iniciamos
        is_running = True
        btn_toggle.config(text="Detener Función", bg="red")
        lbl_status.config(text="Estado: En ejecución", fg="green")
        # Iniciar la función en un hilo separado para no bloquear la interfaz
        thread = threading.Thread(target=my_function)
        thread.daemon = True # El hilo terminará cuando el programa principal lo haga
        thread.start()
    else:
        # Si la función está en ejecución, la detenemos
        is_running = False
        btn_toggle.config(text="Iniciar Función", bg="green")
        lbl_status.config(text="Estado: Detenida", fg="red")
        
# Configurar la ventana principal
root = tk.Tk()
root.title("Control de Función")
root.geometry("300x150")
root.config(bg="#f0f0f0")

# Crear los widgets
lbl_status = tk.Label(root, text="Estado: Detenida", fg="red", bg="#f0f0f0", font=("Helvetica", 12, "bold"))
lbl_status.pack(pady=20)

btn_toggle = tk.Button(root, text="Iniciar Función", command=toggle_function, bg="green", fg="white", font=("Helvetica", 10, "bold"), relief="raised")
btn_toggle.pack(pady=10)

# Iniciar el bucle principal de Tkinter
root.mainloop()








