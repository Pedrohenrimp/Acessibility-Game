import pygame, sys, random

from pygame.constants import K_DOWN, K_UP


# Lógica do jogo
def criar_colisor_moedas():
    posicao = random.choice(alturas_moedas)
    colisor_moeda = moeda.get_rect(bottomleft = (1280, posicao))
    return colisor_moeda

def desenhar_moedas(moedas):
    for moe in moedas:
        tela.blit(moeda, moe)

def mover_moedas(moedas):
    for moeda in moedas:
        moeda.centerx -= 2
    return moedas

def verificar_colisao_moedas(moedas):
    for moeda in moedas:
        if colisor_passaro.colliderect(moeda):
            return True
    return False

def verificar_colisao_topo_chao():
    if colisor_passaro.top <= 0 or colisor_passaro.bottom >= 720:
        return True

def verificar_proximidade_topo_chao():
    if colisor_passaro.top <= 100 or colisor_passaro.bottom >= 590:
        return True

def mostrar_score(gameOver):
    if not gameOver:
        texto_score = fonte_score.render(str(int(score)), True, (255, 255, 255))
        posicao_score = texto_score.get_rect(center = (640, 80))
        tela.blit(texto_score, posicao_score)
    else:
        txt_h_score = fonte_score.render("High Score: " + str(int(high_score)), True, (255, 255, 255))
        posicao_high_score = txt_h_score.get_rect(center = (640, 400))
        tela.blit(txt_h_score, posicao_high_score)
        
        texto_score = fonte_score.render("Score: " + str(int(score)), True, (255, 255, 255))
        posicao_score = texto_score.get_rect(center = (640, 500))
        tela.blit(texto_score, posicao_score)

        txt_recomecar = fonte_msg.render("Pressione << Espaço >> p/ recomeçar", True, (255, 255, 255))
        posicao_txt_recomecar = txt_recomecar.get_rect(center = (640, 600))
        tela.blit(txt_recomecar, posicao_txt_recomecar)


def atualizar_high_score(score, high_score):
    if score > high_score:
        high_score = score
    return high_score

pygame.mixer.init()
pygame.mixer.set_num_channels(10)


pygame.init()

# Configurações do Jogo
tela = pygame.display.set_mode((1280, 720))
relogio = pygame.time.Clock()
fonte_score = pygame.font.SysFont('Comic Sans MS', 40, bold = True)
fonte_msg = pygame.font.SysFont('Comic Sans MS', 30)


# Variáveis do Jogo
gravidade = 0.1
movimento_passaro = 0
game_over = False
pegou_moeda = False
score = 0
high_score = 0
pause = False
proximo = False
daltonismo = False
feedback_visual = False
feedback_auditivo = False
audio_feedback_auditivo = False
audio_pressione_espaco = False


# Elementos do Jogo
fundo = pygame.image.load('src/img/Inacessivel/fundo.png')

fundo_gameOver = pygame.image.load('src/img/Inacessivel/fundo_game_over.png')

aperte_espaco_01 = pygame.transform.scale(pygame.image.load('src/img/Acessivel/aperte_espaco_01.png'), (170, 95))
aperte_espaco_02 = pygame.transform.scale(pygame.image.load('src/img/Acessivel/aperte_espaco_02.png'), (170, 95))

instucao_jogo = pygame.transform.scale(pygame.image.load('src/img/Acessivel/instrucao_jogo.png'), (320, 126))

passaro = pygame.image.load('src/img/Inacessivel/passaro.png')
colisor_passaro = passaro.get_rect(center = (200, 360))
audio_passaro = pygame.mixer.Sound("src/sons/asa_batendo.ogg")
audio_perigo = pygame.mixer.Sound("src/sons/perigo.ogg")

moeda = pygame.image.load('src/img/Inacessivel/moeda.png')
lista_moedas = []
SPAWN_MOEDAS = pygame.USEREVENT
pygame.time.set_timer(SPAWN_MOEDAS, 2400)
alturas_moedas = [100, 150, 200, 250, 300, 400, 450, 500, 550, 600]


# Loop do Jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if game_over and evento.key == pygame.K_SPACE:
                game_over = False
                colisor_passaro.center = (200, 360)
                lista_moedas.clear()
                movimento_passaro = 0
                score = 0
            if not game_over and evento.key == pygame.K_SPACE and (score == 5 or score == 10 or score == 15):
                if not proximo:
                    if feedback_auditivo and score == 15:
                        pygame.mixer.music.stop()
                    pause = False
                else:
                    proximo = False
        if evento.type == SPAWN_MOEDAS and not pause:
            lista_moedas.append(criar_colisor_moedas())
            
    
    # Fundo
    tela.blit(fundo, (0, 0))

    game_over = verificar_colisao_topo_chao()

    if not game_over and not pause:
        # Pássaro
        movimento_passaro += gravidade
        colisor_passaro.centery += movimento_passaro
        if pygame.key.get_pressed()[K_DOWN]:
            movimento_passaro = 3
            colisor_passaro.centery += movimento_passaro
            if not pygame.mixer.Channel(1).get_busy() and score >= 15:
                pygame.mixer.Channel(1).play(audio_passaro)
        if pygame.key.get_pressed()[K_UP]:
            movimento_passaro = -3
            colisor_passaro.centery += movimento_passaro
            movimento_passaro = 0
            if not pygame.mixer.Channel(1).get_busy() and score >= 15:
                pygame.mixer.Channel(1).play(audio_passaro)
        tela.blit(passaro, colisor_passaro)
    
        # Moedas
        lista_moedas = [moeda for moeda in lista_moedas if moeda.right > 0]
        lista_moedas = mover_moedas(lista_moedas)
        desenhar_moedas(lista_moedas)

        pegou_moeda = verificar_colisao_moedas(lista_moedas)
        if pegou_moeda:
            del(lista_moedas[0])
            score += 1
            if score > 15:
                pygame.mixer.music.load("src/sons/coletar_ponto.mp3")
                pygame.mixer.music.play()
            pegou_moeda = False
            if score == 5 or score == 10 or score == 15:
                pause = True
        
        if score >= 10:
            tela.blit(instucao_jogo, (480, 580))

        if score >= 15:
            if verificar_proximidade_topo_chao():
                if not pygame.mixer.Channel(3).get_busy():
                    pygame.mixer.Channel(3).play(audio_perigo)
            else:
                pygame.mixer.Channel(3).fadeout(600)

    elif pause:
        if score == 5:
            if not daltonismo:
                proximo = True
                daltonismo = True
            tela.blit(pygame.image.load('src/img/Acessivel/tela_acessibilidade_daltonismo_01.png'), (0, 0))
            if not proximo:
                tela.blit(fundo, (0, 0))
                tela.blit(pygame.image.load('src/img/Acessivel/tela_acessibilidade_daltonismo_02.png'), (0, 0))
                fundo = pygame.image.load('src/img/Acessivel/fundo.png')
                fundo_gameOver = pygame.image.load('src/img/Acessivel/fundo_game_over_sem_feedback_visual.png')
                passaro = pygame.image.load('src/img/Acessivel/passaro.png')
                moeda = pygame.image.load('src/img/Acessivel/moeda.png')
        elif score == 10:
            feedback_visual = True
            fundo_gameOver = pygame.image.load('src/img/Acessivel/fundo_game_over.png')
            tela.blit(pygame.image.load('src/img/Acessivel/tela_acessibilidade_deficientes_auditivos.png'), (0, 0))
            tela.blit(aperte_espaco_02, (1050, 510))
            mostrar_score(game_over)
            pygame.display.update()
            pygame.time.wait(500)
            tela.blit(fundo, (0, 0))
            tela.blit(pygame.image.load('src/img/Acessivel/tela_acessibilidade_deficientes_auditivos.png'), (0, 0))
            tela.blit(aperte_espaco_01, (1050, 510))
            mostrar_score(game_over)
            pygame.display.update()
            pygame.time.wait(500)
            
        elif score == 15:
            feedback_auditivo = True
            tela.blit(pygame.image.load('src/img/Acessivel/tela_acessibilidade_deficientes_visuais.png'), (0, 0))
            if not audio_feedback_auditivo:
                audio_feedback_auditivo = True
                pygame.mixer.music.load("src/sons/script_feedback_auditivo.mp3")
                pygame.mixer.music.play()
            if audio_feedback_auditivo and not pygame.mixer.music.get_busy() and not audio_pressione_espaco:
                audio_pressione_espaco = True
                pygame.mixer.music.load("src/sons/script_pressione_espaco_para_voltar_ao_jogo.mp3")
                pygame.mixer.music.play()
        
        if pygame.mixer.Channel(3).get_busy():
            pygame.mixer.Channel(3).stop()



    else:
        high_score = atualizar_high_score(score, high_score)
        if feedback_visual:
            tela.blit(fundo_gameOver, (0, 0))
            tela.blit(aperte_espaco_02, (1010, 510))
            mostrar_score(game_over)
            pygame.display.update()
            pygame.time.wait(750)
            tela.blit(fundo_gameOver, (0, 0))
            tela.blit(aperte_espaco_01, (1010, 510))
            mostrar_score(game_over)
            pygame.display.update()
            pygame.time.wait(750)
        else:
            tela.blit(fundo_gameOver, (0, 0))
            mostrar_score(game_over)
    mostrar_score(game_over)
    pygame.display.update()
    relogio.tick(120)