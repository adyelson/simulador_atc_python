import pygame
from movimento import voo, inserirnovorumo

pygame.init()

velocidade = 5
janela = pygame.display.set_mode((800,600))

pygame.display.set_caption("AIR TRAFFIC")


janela_aberta=True
tamanhorastro= 9
tamanhovetor = 3
class aeronave():
    def __init__(self,vel,rumoinicial, tipo,matricula,posinicialx,posinicialy,ladocurva='esquerda',passadas=[],contpassadas=0):
        self.tipo = tipo
        self.matricula = matricula      
        self.x = posinicialx
        self.y = posinicialy
        self.passadas=passadas
        self.ladocurva = ladocurva
        self.contpassadas = contpassadas
        self.rumo = [rumoinicial,rumoinicial]
        self.vel = vel
        
    def aerodinamica(self,novorumo,ladocurva):
        if(self.rumo[0]!=novorumo):
            self.rumo[1]=novorumo
        print("rumos:"+str(self.rumo))
        self.ladocurva =ladocurva

        #condição para determinar o tamanho do rastro
        if (self.contpassadas<tamanhorastro):
            self.passadas.append((self.x,self.y))
            self.contpassadas+=1
        else:
            self.passadas.pop(0)
            self.passadas.append((self.x,self.y))
        # variavel x passa o para de posição para o pygame desenhar
        for x in self.passadas:
            pygame.draw.circle(janela, (0,0,0), (x), 2, width=0)#rastro

        #chamar função para converter velocidade composta nos eixos
        velComposta = voo(self.vel,self.rumo[0],self.rumo[1],self.ladocurva)
        velX= velComposta[0]
        velY= velComposta[1]
        self.rumo[0]= velComposta[2]
        print("rumo1:"+str(self.rumo[0]))
        print("rumo2:"+str(self.rumo[1]))
        self.x= self.x+ velX
        self.y= self.y+ velY

            
        #desenho do plot
        pygame.draw.circle(janela, (0,0,0), (self.x,self.y), 14, width=0)
        pygame.draw.circle(janela, (170,170,170), (self.x,self.y), 12, width=0)
        pygame.draw.line(janela, (0,0,0), (self.x-1,self.y-12),(self.x-1,self.y+12), width=2)
        pygame.draw.line(janela, (0,0,0), (self.x-12,self.y-1),(self.x+12,self.y-1), width=2)
        pygame.draw.line(janela, (0,0,0), (self.x,self.y),(self.x+velX*tamanhovetor,self.y+velY*tamanhovetor), width=2)#vetor medida

#criar aeronave
acft1 = aeronave(15,290,"atr","passaredo",400,400)
passada=0
acfts = []
acfts.append(acft1)
while janela_aberta:
    pygame.time.delay(3000)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta= False
        
    janela.fill((170,170,170))
    pressed = pygame.key.get_pressed()
          
    if pressed[pygame.K_h]:
        pressed=''
        inserirnovorumo(acft1)   
    else:
        acft1.aerodinamica(acft1.rumo[0],acft1.ladocurva)

    pygame.display.update()

pygame.quit()    
