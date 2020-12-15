#BIBLIOTECAS
import pygame
import winsound
#=================#
#Som Princioal!
def SomPrincipal():
    #Usando o winsound e passando 4 parâmetros.Fazendo com que a musica seja reproduzida de fundo e em loop.
    winsound.PlaySound('udr.wav',winsound.SND_FILENAME+winsound.SND_LOOP+winsound.SND_ASYNC)
#Função principal!
def main():
    #---------------------------------------------------------# 
    #Areá das variaveis 
    pygame.init()
    tela=pygame.display.set_mode([500,500])
    pygame.display.set_caption("Buggy Block")
    relogio=pygame.time.Clock()
    corTelaPrincipal=(28,28,28)
    #superficie=pygame.Surface((300,300))
    corSuperficie1=(54,54,54)
    corButton=(0,0,128)
    corButton2=(139,0,139)
    
    ret=pygame.Rect(50,25,30,29)
    
    ret2=pygame.Rect(0,40,455,10)
    ret3=pygame.Rect(0,87,240,10)
    
    ret4=pygame.Rect(276,87,250,10)
    ret5=pygame.Rect(45,130,500,10)
    
    ret6=pygame.Rect(0,175,230,10)
    ret7=pygame.Rect(266,175,230,10)
    
    ret8=pygame.Rect(0,220,280,10)
    ret9=pygame.Rect(315,220,230,10)
    
    ret10=pygame.Rect(0,265,200,10)
    ret11=pygame.Rect(235,265,280,10)
    
    ret12=pygame.Rect(0,310,140,10)
    ret13=pygame.Rect(175,310,100,10)
    
    ret14=pygame.Rect(310,310,300,10)
    ret15=pygame.Rect(43,355,413,10)

    ret16=pygame.Rect(0,400,240,10)
    ret17=pygame.Rect(276,400,240,10)

    ret18=pygame.Rect(0,420,240,10)
    ret19=pygame.Rect(276,420,240,10)

    ret20=pygame.Rect(0,440,240,10)
    ret21=pygame.Rect(276,440,240,10)

    wallDireita=pygame.Rect(493,0,20,600)
    wallEsquerda=pygame.Rect(0,0,7,600)
    wallCima=pygame.Rect(0,0,500,2)
    

    
    #--------------------------------------------------------#
    #DECLRAÇÃO DE FONTES!
    pygame.font.init()
    font_padrao=pygame.font.get_default_font()
    fonte_perdeu=pygame.font.SysFont(font_padrao,45)
    fonte_ganhou=pygame.font.SysFont(font_padrao,45)
    #---------------------------------------------------------#

    sair=False
    while sair!=True:
        tela.fill(corTelaPrincipal)
        #tela.blit(superficie,(10,10))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair=True

            #====================================#
               #Movimentação do bloco principal
            (xant,yant)=(ret.left,ret.top)
            (ret.left,ret.top)=pygame.mouse.get_pos()
            ret.left=ret.left-ret.width/2
            ret.top=ret.top-ret.height/2
            if event.type==pygame.MOUSEBUTTONDOWN:
                pygame.mouse.set_pos(28,20)
                main()
            #=====================================#
        #====================================##=====================================##=====================================#
                #Colisões
        if ret.colliderect(ret2) or ret.colliderect(ret3) or ret.colliderect(ret4) or ret.colliderect(ret5) or ret.colliderect(ret6) or ret.colliderect(ret7) or ret.colliderect(ret8) or ret.colliderect(ret9) or ret.colliderect(ret10) or ret.colliderect(ret11) or ret.colliderect(ret12) or ret.colliderect(ret13) or ret.colliderect(ret14) or ret.colliderect(ret15) or ret.colliderect(ret16) or ret.colliderect(ret17) or ret.colliderect(ret18) or ret.colliderect(ret19) or ret.colliderect(ret20) or ret.colliderect(ret21) or ret.colliderect(wallCima) or ret.colliderect(wallDireita) or ret.colliderect(wallEsquerda):
            text=fonte_perdeu.render('Você Perdeu!',1,(255,255,255))
            tela.blit(text,(250,250))
            pygame.mouse.set_pos(30,20)
            (ret.left,ret.top)=(xant,yant)
        #=====================================##=====================================##=====================================#            

        if ret.top > 450:
            text=fonte_perdeu.render('Parabéns!',1,(255,255,255))
            tela.blit(text,(150,100))
            text=fonte_perdeu.render('Obrigado por jogar Buggy Block!',1,(255,255,255))
            tela.blit(text,(10,150))
            ret2.left=600
            ret3.left=600
            ret4.left=600
            ret5.left=600
            ret6.left=600
            ret7.left=600
            ret8.left=600
            ret9.left=600
            ret10.left=600
            ret11.left=600
            ret12.left=600
            ret13.left=600
            ret14.left=600
            ret15.left=600
            ret16.left=600
            ret17.left=600
            ret18.left=600
            ret19.left=600
            ret20.left=600
            ret21.left=600

        pygame.draw.rect(tela,corButton,ret)
        pygame.draw.rect(tela,corButton2,ret2)
        pygame.draw.rect(tela,corButton2,ret3)
        pygame.draw.rect(tela,corButton2,ret4)
        pygame.draw.rect(tela,corButton2,ret5)
        pygame.draw.rect(tela,corButton2,ret6)
        pygame.draw.rect(tela,corButton2,ret7)
        pygame.draw.rect(tela,corButton2,ret8)
        pygame.draw.rect(tela,corButton2,ret9)
        pygame.draw.rect(tela,corButton2,ret10)
        pygame.draw.rect(tela,corButton2,ret11)
        pygame.draw.rect(tela,corButton2,ret12)
        pygame.draw.rect(tela,corButton2,ret13)
        pygame.draw.rect(tela,corButton2,ret14)
        pygame.draw.rect(tela,corButton2,ret15)
        pygame.draw.rect(tela,corButton2,ret16)
        pygame.draw.rect(tela,corButton2,ret17)
        pygame.draw.rect(tela,corButton2,ret18)
        pygame.draw.rect(tela,corButton2,ret19)
        pygame.draw.rect(tela,corButton2,ret20)
        pygame.draw.rect(tela,corButton2,ret21)
        pygame.draw.rect(tela,corButton2,wallDireita)
        pygame.draw.rect(tela,corButton2,wallEsquerda)
        pygame.draw.rect(tela,corButton2,wallCima)
        pygame.display.update()
    pygame.quit()
SomPrincipal()
main()