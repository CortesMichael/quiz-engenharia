import pygame
import sys
from perguntas import perguntas
from funcoes import *

# Inicialização do Pygame
pygame.init()
LARGURA, ALTURA = 900, 650
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Quiz: Engenharia da Transformação Digital")
clock = pygame.time.Clock()

# Paleta de Cores
COR_FUNDO = (24, 28, 36)
COR_CARD = (36, 42, 56)
COR_TEXTO = (240, 240, 240)
COR_BOTAO = (53, 162, 235)
COR_BOTAO_HOVER = (79, 180, 250)
COR_BOTAO_RESTART = (46, 204, 113)
COR_BOTAO_RESTART_HOVER = (82, 222, 139)
COR_CORRETA = (46, 204, 113)  
COR_ERRADA = (231, 76, 60)    

# Fontes
FONTE_TITULO = pygame.font.SysFont("Arial", 28, bold=True)
FONTE_TEXTO = pygame.font.SysFont("Arial", 20)

# --- FUNÇÃO PARA INICIALIZAR/REINICIAR O JOGO ---
def iniciar_novo_jogo():
    global perguntas_partida, pontos, indice_pergunta, respondido, opcao_escolhida
    embaralhar_perguntas(perguntas)
    perguntas_partida = perguntas[:10]
    pontos = 0
    indice_pergunta = 0
    respondido = False       
    opcao_escolhida = None   

# Inicializa as variáveis
nome_usuario = ""
estado_jogo = 'START'
iniciar_novo_jogo()

running = True
while running:
    pos_mouse = pygame.mouse.get_pos()
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
            
        # --- LÓGICA DA TELA DE INÍCIO ---
        if estado_jogo == 'START':
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN and nome_usuario.strip() != "":
                    estado_jogo = 'QUIZ'
                elif evento.key == pygame.K_BACKSPACE:
                    nome_usuario = nome_usuario[:-1]
                else:
                    if len(nome_usuario) < 15 and (evento.unicode.isalnum() or evento.unicode == " "):
                        nome_usuario += evento.unicode

        # --- LÓGICA DA TELA DO QUIZ ---
        elif estado_jogo == 'QUIZ':
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                
                if respondido:
                    respondido = False
                    opcao_escolhida = None
                    indice_pergunta += 1
                    
                    if indice_pergunta >= len(perguntas_partida):
                        salvar_ranking(nome_usuario, pontos)
                        estado_jogo = 'FIM'
                        
                else:
                    for i, ret_botao in enumerate(retangulos_botoes):
                        if ret_botao.collidepoint(pos_mouse):
                            pergunta_atual = perguntas_partida[indice_pergunta]
                            opcao_escolhida = i
                            respondido = True
                            
                            acertou = verificar_resposta(pergunta_atual, i)
                            pontos = atualizar_pontos(acertou, pontos)

        # --- LÓGICA DA TELA DE FIM ---
        elif estado_jogo == 'FIM':
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if ret_botao_restart.collidepoint(pos_mouse):
                    iniciar_novo_jogo()
                    nome_usuario = ""
                    estado_jogo = 'START'

    # --- DESENHO DAS TELAS ---
    tela.fill(COR_FUNDO)

    if estado_jogo == 'START':
        txt = FONTE_TITULO.render("Quiz de Engenharia da Transformação Digital", True, COR_TEXTO)
        tela.blit(txt, (LARGURA//2 - txt.get_width()//2, 150))
        
        txt_Instrucao = FONTE_TEXTO.render("Digite seu nome e aperte ENTER para começar:", True, COR_TEXTO)
        tela.blit(txt_Instrucao, (LARGURA//2 - txt_Instrucao.get_width()//2, 280))
        
        caixa_nome = pygame.Rect(LARGURA//2 - 200, 330, 400, 50)
        pygame.draw.rect(tela, COR_CARD, caixa_nome, border_radius=8)
        txt_nome = FONTE_TITULO.render(nome_usuario, True, COR_BOTAO_HOVER)
        tela.blit(txt_nome, (caixa_nome.x + 20, caixa_nome.y + 10))

    elif estado_jogo == 'QUIZ':
        pergunta_atual = perguntas_partida[indice_pergunta]
        resposta_correta = pergunta_atual["resposta"]
        
        txt_progresso = FONTE_TEXTO.render(f"Pergunta {indice_pergunta + 1} de {len(perguntas_partida)}", True, COR_TEXTO)
        tela.blit(txt_progresso, (50, 30))
        
        caixa_pergunta = pygame.Rect(50, 70, LARGURA - 100, 140)
        pygame.draw.rect(tela, COR_CARD, caixa_pergunta, border_radius=10)
        desenhar_texto_quebrado(tela, pergunta_atual["pergunta"], (caixa_pergunta.x + 20, caixa_pergunta.y + 20), caixa_pergunta.width - 40, FONTE_TEXTO, COR_TEXTO)
        
        if respondido:
            txt_aviso = FONTE_TEXTO.render("Clique em qualquer lugar para continuar ->", True, COR_BOTAO_HOVER)
            tela.blit(txt_aviso, (LARGURA - txt_aviso.get_width() - 50, 30))
        
        retangulos_botoes = []
        y_opcao = 240
        for i, alternativa in enumerate(pergunta_atual["alternativas"]):
            ret_botao = pygame.Rect(50, y_opcao, LARGURA - 100, 75)
            retangulos_botoes.append(ret_botao)
            
            # --- LÓGICA DE CORES (VERDE/VERMELHO) ---
            if respondido:
                if i == resposta_correta:
                    cor_atual = COR_CORRETA
                elif i == opcao_escolhida and opcao_escolhida != resposta_correta:
                    cor_atual = COR_ERRADA
                else:
                    cor_atual = COR_CARD
            else:
                cor_atual = COR_BOTAO_HOVER if ret_botao.collidepoint(pos_mouse) else COR_BOTAO
            
            pygame.draw.rect(tela, cor_atual, ret_botao, border_radius=8)
            
            cor_texto_opcao = COR_TEXTO if respondido else COR_FUNDO
            desenhar_texto_quebrado(tela, alternativa, (ret_botao.x + 20, ret_botao.y + 15), ret_botao.width - 40, FONTE_TEXTO, cor_texto_opcao)
            y_opcao += 90

    elif estado_jogo == 'FIM':
        txt_fim = FONTE_TITULO.render(f"Fim de Jogo, {nome_usuario}!", True, COR_TEXTO)
        tela.blit(txt_fim, (LARGURA//2 - txt_fim.get_width()//2, 30))
        
        txt_pontos = FONTE_TEXTO.render(f"Sua pontuação final foi: {pontos} de 10 acertos", True, COR_BOTAO_HOVER)
        tela.blit(txt_pontos, (LARGURA//2 - txt_pontos.get_width()//2, 75))
        
        txt_rank_titulo = FONTE_TITULO.render("RANKING GERAL", True, COR_TEXTO)
        tela.blit(txt_rank_titulo, (LARGURA//2 - txt_rank_titulo.get_width()//2, 130))
        
        ranking = ordenar_ranking(carregar_ranking())
        y_rank = 180
        for i, jogador in enumerate(ranking[:5]):
            caixa_rank = pygame.Rect(LARGURA//2 - 200, y_rank, 400, 40)
            pygame.draw.rect(tela, COR_CARD, caixa_rank, border_radius=5)
            
            txt_pos = FONTE_TEXTO.render(f"{i+1}º", True, COR_BOTAO_HOVER)
            txt_jogador = FONTE_TEXTO.render(f"{jogador['nome']}", True, COR_TEXTO)
            txt_pts = FONTE_TEXTO.render(f"{jogador.get('pontos', 0)} pts", True, COR_TEXTO)
            
            tela.blit(txt_pos, (caixa_rank.x + 15, caixa_rank.y + 8))
            tela.blit(txt_jogador, (caixa_rank.x + 60, caixa_rank.y + 8))
            tela.blit(txt_pts, (caixa_rank.x + 320, caixa_rank.y + 8))
            y_rank += 48

        ret_botao_restart = pygame.Rect(LARGURA//2 - 150, 520, 300, 55)
        cor_restart = COR_BOTAO_RESTART_HOVER if ret_botao_restart.collidepoint(pos_mouse) else COR_BOTAO_RESTART
        pygame.draw.rect(tela, cor_restart, ret_botao_restart, border_radius=8)
        
        txt_restart = FONTE_TITULO.render("Tentar Novamente", True, COR_FUNDO)
        tela.blit(txt_restart, (ret_botao_restart.x + ret_botao_restart.width//2 - txt_restart.get_width()//2, ret_botao_restart.y + 12))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()