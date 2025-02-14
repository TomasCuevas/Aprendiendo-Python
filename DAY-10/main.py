import pygame

# Inicializar Pygame
pygame.init()

# Crear la pantalla
pantalla = pygame.display.set_mode((800, 600))

# Titulo y logo
pygame.display.set_caption("Invasión Espacial")
logo = pygame.image.load("ovni.png")
pygame.display.set_icon(logo)

# Variables del jugador
img_jugador = pygame.image.load("cohete.png")
jugador_x = 400 - 32
jugador_y = 600 - 100
jugador_x_cambio = 0

# Funcion para dibujar el jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))

# Loop del juego
se_ejecuta = True
while se_ejecuta:
    # RGB
    pantalla.fill((205, 144, 228))

    # Eventos
    for evento in pygame.event.get():
        # Cerrar el juego
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # Movimiento del jugador
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio -= 0.3
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio += 0.3

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

    # Dibujar el jugador
    jugador(jugador_x, jugador_y)

    # Actualizar la pantalla
    pygame.display.update()

# Salir del juego
pygame.quit()
