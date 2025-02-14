import pygame
import random
# Inicializar Pygame
pygame.init()

# Crear la pantalla
pantalla = pygame.display.set_mode((800, 600))

# Titulo y logo
pygame.display.set_caption("Invasión Espacial")
logo = pygame.image.load("ovni.png")
pygame.display.set_icon(logo)
fondo = pygame.image.load("fondo.jpg")

# Variables del jugador
img_jugador = pygame.image.load("cohete.png")
jugador_x = 400 - 32
jugador_y = 600 - 100
jugador_x_cambio = 0

# Variables del enemigo
img_enemigo = pygame.image.load("enemigo.png")
enemigo_x = random.randint(0, 736)
enemigo_y = random.randint(50, 200)
enemigo_x_cambio = 1

# Variables del proyectil
img_proyectil = pygame.image.load("proyectil.png")
proyectil_x = jugador_x
proyectil_y = jugador_y
proyectil_x_cambio = 0
proyectil_y_cambio = 1
proyectil_visible = False

# Funcion para dibujar el jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))

# Funcion para dibujar el enemigo
def enemigo(x, y):
    pantalla.blit(img_enemigo, (x, y))

# Funcion para dibujar el proyectil
def disparar_proyectil(x, y):
    global proyectil_visible
    proyectil_visible = True
    pantalla.blit(img_proyectil, (x + 16, y + 10))

# Loop del juego
se_ejecuta = True
while se_ejecuta:
    # RGB
    pantalla.blit(fondo, (0, 0))

    # Eventos
    for evento in pygame.event.get():
        # Cerrar el juego
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # Movimientos del jugador y disparo
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio -= 1
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio += 1
            if evento.key == pygame.K_SPACE:
                if proyectil_visible == False:
                    proyectil_x = jugador_x
                    disparar_proyectil(proyectil_x, proyectil_y)

        # Detener el movimiento del jugador
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    # Movimiento del jugador
    jugador_x += jugador_x_cambio

    # Limitar el movimiento del jugador
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    # Movimiento del enemigo
    enemigo_x += enemigo_x_cambio

    # Limitar el movimiento del enemigo
    if enemigo_x <= 0:
        enemigo_x_cambio = 1
        enemigo_y += 40
    elif enemigo_x >= 736:
        enemigo_x_cambio = -1
        enemigo_y += 40

    # Movimiento del proyectil
    if proyectil_y <= -64:
        proyectil_visible = False
        proyectil_y = jugador_y
    
    if proyectil_visible:
        disparar_proyectil(proyectil_x, proyectil_y)
        proyectil_y -= proyectil_y_cambio

    # Dibujar el jugador
    jugador(jugador_x, jugador_y)

    # Dibujar el enemigo
    enemigo(enemigo_x, enemigo_y)

    # Actualizar la pantalla
    pygame.display.update()

# Salir del juego
pygame.quit()
