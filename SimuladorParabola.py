#jogo desenvolvido para amostragem de estudos de fisica
import pygame, sys
from pygame.locals import *
from math import *

pygame.init()

#primeiro Largura, segundo Altura
tela=pygame.display.set_mode((900,550))

#carrega e convert todas imagens a serem utilizadas no jogo
pygame.mixer.music.load("Beatles-Love_Me_do.MID")
formula=pygame.image.load("Formulas.png")#.convert()
back=pygame.image.load("Background.jpg").convert()
bola=pygame.image.load("ball.png").convert_alpha()
caixa=pygame.image.load("caixa.png").convert_alpha()
seta=pygame.image.load("seta.png").convert_alpha()
arvore=pygame.image.load("arvore.png").convert_alpha()
catapultaT=pygame.image.load("Catapult-Armada3.png").convert_alpha()

#----------------------------------------------------------------------------

tela.blit(back, (0,0)) # desenha o fundo

#------------------------------------------------------------------------------

#definição e valores de variaveis

sy=360 #definição do valor da variavel sy = responsavel pelo valor inicial da seta em cima da caixa(que fica se movimentando)
sx = 840 #definição do valor da variavel sx = responsavel pelo valor inicial da seta em cima da caixa(que fica se movimentando)
veloSeta=1
ind = True #definição da variavel ind = responsavel por controlar a animação da seta em cima da caixa
func=True #definição da variavel func = responsavel por manter o jogo rodando ( se variavel false = jogo para stop () )
pygame.display.flip() #responsavel por limpar o cach da tela, para não correr tarjas prestas da framerate, e atualizar as telas.
pontoX=0 #valor de X utilizado como referencia para calculo da parabola
pontoY=0 # valor de Y utilizado como referencia para calculo da parabola
pontoYant = 0
pontoXant = 0
i = 0
fx=20 #seta posição incial da bola de arremesso em X
fy=375 # seta posição inciial da bola de arremesso em Y
vx=fx # atribui a = vx o mesmo valor de fx ( para que o mesmo possa ser utilizado como ponto de referencia apos o arremesso ( para desenhar a bola para um novo arremesso)
vy=fy #atribui a = vy o mesmo valor de fy ( para que o mesmo possa ser utilizado como ponto de referencia apos o arremesso ( para desenhar a bola para um novo arremesso)
t = 0 # definição variavel T= tempo em que esta ocorrendo a animação do movimento da parabola
v = 30 #definição da variavel v= velocidade inciial
ang= 70 #definição da variavel ang = responsavel por representar o angulo incial
gra = - 9.8 # definição da variavel gra = representa gravidade aplicada a formula de fisica
yellow = (255, 255, 0) #definição da variavel Yellow = ganhando valores RGB que definiem a cor amarelo que é utilizada para mostrar valores das formulas na tela.
black = (0, 0, 0) #definição da variavel Yellow = ganhando valores RGB que definiem a cor PRETA, que é utilizada para mostrar valores das formulas na tela.
setCaixa = 830

# definições e valores de Objetos ------
myfont = pygame.font.SysFont("Comic Sans MS", 17) # definição da fonte e tamanho utilizados nos textos que serão exibidos
velocidade = myfont.render( "%0.1f M/s" % (v), 1, yellow) #atribuindo ao Objeto Velocidade = seu tipo como texto, sua cor Yellow, e seu valor V(velocidade)
angulo = myfont.render( "%0.1f G/s" % (ang), 1, yellow) #atribuindo ao Objeto Angulo = seu tipo(texto), sua cor (Amarelo), e seu valor ang (angulo)
gravidade = myfont.render( "Gravidad: %0.1f" % (gra), 1, yellow) #atribuindo ao Objeto Angulo = seu tipo(texto), sua cor (Amarelo), e seu valor gra (gravidade
msg = myfont.render("Parabens Acertou e Passou para o proximo Level", 20, black) #atribuindo ao Objeto Angulo = seu tipo(texto), sua cor (black = Preto), e seu valor Mensagem de Acerto ao alvo
setXmsg = 0 # seta posição inicial de X da mensagem de acerto a caixa
setYmsg = -30 # seta posição inicial de Y da mensagem de acerto a caixa
altArvo = 320 # seta posição inicial da arvore = level 1


setDisMxX = - 80

setAltMxY = - 120                

pygame.mixer.music.play(-10) # inicia o som do jogo

while 1==1: # laço principal de execução do jogo
    
    pygame.event.pump() # carrega propriedades de entradas de dispositivos
    key = pygame.key.get_pressed() #carrega eventos de teclado pressionados
    #------------------------------------------------
    #Desenha todos os objetos na tela 
    tela.blit(back, (0,0))
    tela.blit(formula, (20,70))
    tela.blit(velocidade, (10, 10))
    tela.blit(angulo, (10, 30))
    tela.blit(gravidade, (450, 20))
    tela.blit(caixa, (setCaixa,430))
    tela.blit(seta, (sx,sy))
    tela.blit(catapultaT, (15,410))
    tela.blit(bola, (vx,vy))
    tela.blit(arvore, (350,altArvo))
    tela.blit(msg, (setXmsg, setYmsg))
    disMx = myfont.render("%0.1f Distancia " % (pontoXant), 20, black) #atribuindo ao Objeto
    tela.blit(disMx, (480, setDisMxX))
    altMx = myfont.render("%0.1f Altura" % (pontoYant), 20, black) #atribuindo ao Objeto 
    tela.blit(altMx, (480, setAltMxY))

    #------------------------------------------------------------------------------
#-------------------------------If de comandos Que alterão valores de Angulo e Força 
    if key[pygame.K_RIGHT]:
        setXmsg = 0
        setYmsg = -30
        setAltMxY = - 120                
        setDisMxX = - 80
        v=v+0.1
        velocidade = myfont.render( "%0.1f m/s" % (v), 1, yellow)
    if key[pygame.K_LEFT]:
        setXmsg = 0
        setYmsg = -30
        setAltMxY = - 120                
        setDisMxX = - 80
        v=v-0.1
        velocidade = myfont.render( "%0.1f m/s" % (v), 1, yellow)
    if key[pygame.K_UP]:
        setXmsg = 0
        setYmsg = -30
        setAltMxY = - 120                
        setDisMxX = - 80
        ang=ang+1
        angulo = myfont.render( "%0.1f G/s" % (ang), 1, yellow)
    if key[pygame.K_DOWN]:
        setXmsg = 0
        setYmsg = -30
        setAltMxY = - 120                
        setDisMxX = - 80
        ang=ang-1
        angulo = myfont.render( "%0.1f G/s" % (ang), 1, yellow)

        #---------------------------------------------------
#----------------------------if de Calculos da posição na animação do desenho da parabola
    if key[pygame.K_e]:
        while vy < 470:
            theta = 3.14168*ang/180
            vx= v*cos(theta)
            voy= v*sin(theta)   
            a=-9.8
            pontoX = (pontoX + vx*t)
            pontoY = (pontoY + voy*t+a*t**2/2)
            t = t+0.2
            vx = vx + pontoX/fx
            vy = vy - pontoY/fy
            print (" Velocidade Horizontal x = %0.2f m/s" % (pontoX)) #imprimi no console as posções de X durante o desenho da parabola(OBS: posições de desenho e nao de resultados das formulas)
            print (" Velocidade Horizontal Y = %0.2f m/s" % (pontoY)) #imprimi no console as posções de Y durante o desenho da parabola(OBS: posições de desenho e nao de resultados das formulas)
            pygame.display.flip() # Limpa a tela para desenhar a nova posição da bola
            tela.blit(bola, (vx,vy)) #Desenha a bola na sua nova posição decorente ao tempo passado e a força e angulo aplicado, com o fator gravidade
            pygame.display.flip() #limpa a tela para um novo desenho
            #----------------------------------------------FIM do desenho da parabula
            if pontoY > 0 and i < 2:
                pontoYant = pontoY
                setDisMxX = 130
                i = i + 1
                
            if vy > 470:
                pontoXant = pontoX
                setAltMxY = 150
                i = i + 1

            if i == 0:
                pontoXant = 0
                pontoYant = 0
                #-----------------------------------------------------------------
            #verifica se acertou a caixa ( conseguiu atingir o resultado esperado para a formula)
            if vx > 780 and vx < 840:
                if vy >= 400 and vy <= 440: #verifica se acertou a caixa
                    setXmsg = 320 #seta valor de X na posição da mensagem de acerto da caixa
                    setYmsg = 250 # seta valor de Y na posição da mensagem da caixa
                    ang = 70
                    v = 30
                    angulo = myfont.render( "%0.1f G/s" % (ang), 1, yellow)
                    velocidade = myfont.render( "%0.1f m/s" % (v), 1, yellow)
                    
                    if setCaixa > 760:
                        sx = sx - 20
                        setCaixa = setCaixa - 20
                        
                    if altArvo > 60:
                        altArvo = altArvo - 10 # seta o valor da altura da arvore altArvo = parta que ela fique ainda mais alta que no level anterior
            #-----------------------------------------------------------
        #-------------------------- Zerando os valores da formula e das posições dos objetos, para que possa ser realizado um novo arremesso
        pontoX=0
        pontoY=0
        fx=20
        fy=375
        AmostraVx = vx
        AmostraVy = vy
        i = 0
    #volta a bola no ponto inicial para novo arremesso
    vx=fx
    vy=fy
    t=0
    pygame.display.flip()
    tela.blit(bola, (vx,vy))
            #-------------------------------------------------
#-------------------------------If responsavel pelo movimento constante da seta em cima da caixa
    if sy > 400:
        ind = False

    elif sy < 360:
        ind = True

    pygame.display.flip()
    
    if ind == True:
        sy=sy+veloSeta;
        
    else:
        sy=sy-veloSeta;

#if responsavel pela tomada de decisão entre sair do jogo ou não ( caso pressione Q ,  o jogo é encerrado)    
    if key[pygame.K_q]:
        func=False
        exit()
    pygame.display.flip()
