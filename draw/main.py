# Importa todas las funciones del módulo turtle
from turtle import *

# Importa el módulo colorsys para trabajar con colores HSV
import colorsys as cs

# Acelera la animación (a mayor número, más rápido)
tracer(70)

# Establece el color de fondo de la ventana
bgcolor("black")

# Oculta la flecha (tortuga)
hideturtle()

# Define el grosor del trazo
pensize(2.5)

# Variable para controlar el tono del color (Hue) en HSV
h = 0.0

# Bucle que se repite 360 veces para crear el patrón
for i in range(360):

    # Convierte un color HSV a RGB
    # h = tono, 1 = saturación máxima, 1 = brillo máximo
    color(cs.hsv_to_rgb(h, 1, 1))

    # Incrementa ligeramente el tono para cambiar de color gradualmente
    h += 0.008

    # Gira la tortuga 40 grados a la izquierda
    left(40)

    # Avanza una distancia proporcional a i
    forward(i * 0.8)

    # Gira 80 grados a la derecha
    right(80)

    # Dibuja un arco de círculo
    # radio = i * 0.2, arco de 140 grados
    circle(i * 0.2, 140)

    # Gira 180 grados
    left(180)

    # Dibuja otro arco de círculo
    # radio = i * 0.2, arco de 160 grados
    circle(i * 0.2, 160)

    # Retrocede una distancia proporcional a i
    backward(i * 0.3)

# Mantiene la ventana abierta al finalizar el dibujo
done()