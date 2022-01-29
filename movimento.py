import math
import PySimpleGUI as sg

def Pegarangulo(rumo):
    if (rumo >0 and rumo <90):
        angulo = 90-rumo
        sinalx= 1
        sinaly= -1
    if (rumo >90 and rumo <180):
        angulo = rumo-90
        sinalx= 1
        sinaly= 1
    if (rumo >180 and rumo <270):
        angulo = 270-rumo
        sinalx= -1
        sinaly= 1
    if (rumo >270 and rumo <360):
        angulo = rumo-270
        sinalx= -1
        sinaly= -1
    if (rumo == 0 or rumo == 360):
        angulo = 90
        sinalx= 0
        sinaly= -1
    if (rumo == 90):
        angulo = 0
        sinalx= 1
        sinaly= 0
    if (rumo == 180):
        angulo = 90
        sinalx= 0
        sinaly= 1
    if (rumo == 270):
        angulo = 0
        sinalx= -1
        sinaly= 0

    return([angulo,sinalx,sinaly])


def voo(velocidade,rumo,novorumo,ladocurva):
    if (rumo!=novorumo):
        rumo = mudarproa(rumo,novorumo,ladocurva)

    angulo = Pegarangulo(rumo)[0]
    sinalvelx = Pegarangulo(rumo)[1]
    sinalvely = Pegarangulo(rumo)[2]
    velX = sinalvelx*velocidade*math.cos(math.radians(angulo))
    velY = sinalvely*velocidade*math.sin(math.radians(angulo))
    return([velX,velY,rumo])

def mudarproa(rumoinicial,novorumo,ladocurva):
    
    if (ladocurva=="esquerda"):
        sinalladocurva = -1
    if (ladocurva=="direita"):
        sinalladocurva = 1

    # if ladocurva=='menor':
        
    rumotemporario = float(rumoinicial+sinalladocurva*9)
    diferenca =abs(novorumo-rumotemporario)
    if (rumotemporario> 360):
        rumotemporario = rumotemporario-360

    if (rumotemporario<0):
        rumotemporario = rumotemporario+360
        
    if (diferenca<9):
        rumotemporario = novorumo

   

    print(f"---rumo temporario: {rumotemporario}")
    return(rumotemporario)

def inserirnovorumo(self):
       
    janela1.un_hide()
    while True:
        window,event,values = sg.read_all_windows()
        if (window == janela1 and event== sg.WIN_CLOSED):
            executa = False
            break
        if (window == janela1 and event== 'continuar'):
            if values[0]=='':
                executa = False
                
            else:
                proaNOVA = int(values[0])
                if values['e']==True:
                    executa = True
                    ladocurvaNOVA='esquerda'
                    
                elif values['d']==True:
                    executa = True
                    ladocurvaNOVA='direita'
                    
                else:  
                    executa = True
                    ladocurvaNOVA='menor'
                    
        if executa:
            self.aerodinamica(proaNOVA,ladocurvaNOVA)
            janela1.hide()
            break
               

def janelarumo():
    sg.theme('Reddit')
    layout =[
        [sg.Text('Insira novo rumo:')],
        [sg.Input()],
        [sg.Radio('Esquerda',key='e',group_id=1,default=True),sg.Radio('Direita',key='d',group_id=1)],
        [sg.Button('continuar')]
    ]
    return sg.Window('Inserir rumo',layout=layout,finalize=True)


janela1 = janelarumo()
janela1.hide()