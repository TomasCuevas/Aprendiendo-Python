import pygame
import random
import math
from pygame import mixer

# Inicializar Pygame
pygame.init()

# Configuración de pantalla
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Invasión Espacial")
pantalla_icono = pygame.image.load("ovni.png")
pygame.display.set_icon(pantalla_icono)
fondo = pygame.image.load("fondo.jpg")

# Sonido de fondo
mixer.music.load("musica-fondo.mp3")
mixer.music.set_volume(0.1)
mixer.music.play(-1)

class Jugador:
    def __init__(self):
        self.imagen = pygame.image.load("cohete.png")
        self.x = ANCHO // 2 - 32
        self.y = ALTO - 100
        self.velocidad = 1
        self.movimiento = 0
    
    def mover(self):
        self.x += self.movimiento
        self.x = max(0, min(self.x, ANCHO - 64))
    
    def dibujar(self):
        pantalla.blit(self.imagen, (self.x, self.y))

class Enemigo:
    def __init__(self):
        self.imagen = pygame.image.load("enemigo.png")
        self.x = random.randint(0, ANCHO - 64)
        self.y = random.randint(50, 200)
        self.velocidad = 0.7

    def mover(self):
        self.x += self.velocidad
        if self.x <= 0 or self.x >= ANCHO - 64:
            self.velocidad *= -1
            self.y += 40

    def dibujar(self):
        pantalla.blit(self.imagen, (self.x, self.y))

class Proyectil:
    def __init__(self):
        self.imagen = pygame.image.load("proyectil.png")
        self.x = 0
        self.y = 0
        self.velocidad = 3
        self.visible = False
    
    def disparar(self, x, y):
        if not self.visible:
            self.x = x
            self.y = y
            self.visible = True
            sonido_disparo = mixer.Sound("disparo.mp3")
            sonido_disparo.set_volume(0.5)
            sonido_disparo.play()
    
    def mover(self):
        if self.visible:
            self.y -= self.velocidad
            if self.y < -64:
                self.visible = False
    
    def dibujar(self):
        if self.visible:
            pantalla.blit(self.imagen, (self.x + 16, self.y + 10))

class Juego:
    def __init__(self):
        self.jugador = Jugador()
        self.enemigos = [Enemigo() for _ in range(8)]
        self.proyectil = Proyectil()
        self.puntaje = 0
        self.fuente = pygame.font.Font("freesansbold.ttf", 32)
        self.en_juego = True
    
    def detectar_colision(self, x1, y1, x2, y2):
        return math.dist((x1, y1), (x2, y2)) < 27
    
    def mostrar_puntaje(self):
        texto = self.fuente.render(f"Puntaje: {self.puntaje}", True, (255, 255, 255))
        pantalla.blit(texto, (10, 10))
    
    def game_over(self):
        texto_final = pygame.font.Font("freesansbold.ttf", 50).render("¡Juego terminado!", True, (255, 255, 255))
        pantalla.blit(texto_final, (180, 200))
        self.en_juego = False
        mixer.music.stop()
    
    def ejecutar(self):
        corriendo = True
        while corriendo:
            pantalla.blit(fondo, (0, 0))
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    corriendo = False
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_LEFT:
                        self.jugador.movimiento = -self.jugador.velocidad
                    if evento.key == pygame.K_RIGHT:
                        self.jugador.movimiento = self.jugador.velocidad
                    if evento.key == pygame.K_SPACE:
                        self.proyectil.disparar(self.jugador.x, self.jugador.y)
                if evento.type == pygame.KEYUP:
                    if evento.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                        self.jugador.movimiento = 0
            
            self.jugador.mover()
            self.proyectil.mover()
            
            for enemigo in self.enemigos:
                enemigo.mover()
                if enemigo.y >= 500:
                    for e in self.enemigos:
                        e.y = 2000

                    self.game_over()
                    break
                if self.proyectil.visible and self.detectar_colision(enemigo.x, enemigo.y, self.proyectil.x, self.proyectil.y):
                    mixer.Sound("colision.mp3").play()
                    self.proyectil.visible = False
                    enemigo.x, enemigo.y = random.randint(0, ANCHO - 64), random.randint(50, 200)
                    self.puntaje += 1
                enemigo.dibujar()
            
            self.jugador.dibujar()
            self.proyectil.dibujar()
            self.mostrar_puntaje()
            pygame.display.update()
        pygame.quit()

if __name__ == "__main__":
    Juego().ejecutar()
