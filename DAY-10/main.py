import pygame

# Inicializar Pygame
pygame.init()

# Crear la pantalla
pantalla = pygame.display.set_mode((800, 600))

# Titulo y logo
pygame.display.set_caption("Invasión Espacial")
logo = pygame.image.load("ovni.png")
pygame.display.set_icon(logo)

# Jugador
img_jugador = pygame.image.load("cohete.png")
jugador_x = 400 - 32
jugador_y = 600 - 100

def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))

# Loop del juego
se_ejecuta = True
while se_ejecuta:
    # RGB
    pantalla.fill((205, 144, 228))
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False

    jugador(jugador_x, jugador_y)

    pygame.display.update()

pygame.quit()
