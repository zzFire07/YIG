import pygame, os, turtle, sys, pygame.display

pygame.init()
CONT_PASOS = 0


def collide_DOWN(jugador):
    choque = False
    for i in range (1, largo_jugador):
        pixeles_fondo = pygame.Surface.get_at(fondo, (jugador.x + i, jugador.y + 20))
        if pixeles_fondo == (0, 0, 0, 255):
            choque = True
    return choque

def collide_UP(jugador):
    choque = False
    for i in range (1, largo_jugador):
        pixeles_fondo = pygame.Surface.get_at(fondo, (jugador.x + i, jugador.y))
        if pixeles_fondo == (0, 0, 0, 255):
            choque = True
    return choque

def collide_RIGHT(jugador):
    choque = False
    for i in range (1, largo_jugador):
        pixeles_fondo = pygame.Surface.get_at(fondo, (jugador.x + 20, jugador.y + i))
        if pixeles_fondo == (0, 0, 0, 255):
            choque = True
    return choque

def collide_LEFT(jugador):
    choque = False
    for i in range (1, largo_jugador):
        pixeles_fondo = pygame.Surface.get_at(fondo, (jugador.x, jugador.y + i))
        if pixeles_fondo == (0, 0, 0, 255):
            choque = True
    return choque


def movimiento_jugador(keys_pressed, jugador): #Funcion para el movimiento del jugador
    global CONT_PASOS
    if keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]: #SI SE APRETA A O FLECHA IZQUIERDA SE MUEVE 1 PIXELES HACÍA LA IZQUIERDA
        if collide_LEFT(jugador) == False:
            jugador.x -= vel
            CONT_PASOS += 1
    if keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]: #SI SE APRETA D O FLECHA DERECHA SE MUEVE 1 PIXELES HACÍA LA DERECHA
        if collide_RIGHT(jugador) == False:
            jugador.x += vel
            CONT_PASOS += 1
    if keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP]: #SI SE APRETA W O FLECHA SUPERIOR SE MUEVE 1 PIXELES HACÍA ARRIBA
        if collide_UP(jugador) == False:
            jugador.y -= vel
            CONT_PASOS += 1
    if keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN]: #SI SE APRETA S O FLECHA INFERIOR SE MUEVE 1 PIXELES HACÍA ABAJO
        if collide_DOWN(jugador) == False:
            jugador.y += vel
            CONT_PASOS += 1
         

def mov_imagenes(jugador): #Funcion para las imagenes en el juego
    ventana.fill(blanco)
    ventana.blit(fondo, (0, 0))
    ventana.blit(imagen_jugador, (jugador.x, jugador.y))
   
    
    pygame.display.update()

def main():
    jugador = pygame.Rect(ancho/2, alto/2, largo_jugador, alto_jugador)

    clock = pygame.time.Clock()
    run = True

    #PROGRAMA MAIN
    while run == True:

        clock.tick(FPS) #Se limitan los fotogramas a "FPS"

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Se terminara el bucle si se cierra la ventana.
                run = False

        keys_pressed = pygame.key.get_pressed()
        movimiento_jugador(keys_pressed, jugador)
        mov_imagenes(jugador)
        collide_DOWN(jugador)
        print(CONT_PASOS)

#COLORES
blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (255, 0, 0)
azul = (0, 0, 255)

#CONSTANTES
vel = 1 #Velocidad del jugador
FPS = 60 #Fotogramas por segundo que tendra el programa
ancho, alto = 800, 600 #Dimensiones de la ventana del juego



#TEXTO PARA TIMER

#texto= turtle.Turtle()
#texto.speed(0) #El juego ya abra con esto en pantalla escrito
#texto.color(negro) #Color del texto
#texto.penup() #Para que no aparezca la pluma
#texto.hideturtle() #Esconder pluma
#texto.goto(0,500) #Lugar en donde aparece
#texto.write("Time: 0", align="center", font=("Courier", 24, "normal"))

#PANTALLA
ventana = pygame.display.set_mode((ancho, alto+50))
pygame.display.set_caption("Laberinto del fauno") #NOMBRE DEL JUEGO

fondo = pygame.image.load("laberinto.svg") #Cargamos la imagen que representara al jugador
fondo = pygame.transform.rotate(pygame.transform.scale(fondo, (ancho, alto)), 180)

largo_jugador, alto_jugador = 20, 20 #Dimensiones del jugador
imagen_jugador = pygame.transform.scale(pygame.image.load("circulo.png"), (largo_jugador, alto_jugador))

main()
    
pygame.init()
ven= pygame.display.set_mode((800,600))
pygame.display.set_caption("Juego terminado")
Fuente= pygame.font.SysFont("Arial", 80)
while True:
     ven.fill((255, 255, 255))  #color de fondo
     for event in pygame.event.get():
        if event.type==pygame.QUIT:
        pygame.quit()
        sys.exit()
     texto=Fuente.render("¡YOU WIN!",0,(255,0,0))
     ven.blit(texto,(230,230))
     pygame.display.update()


