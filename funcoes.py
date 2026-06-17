import random
import csv

def embaralhar_perguntas(perguntas):
    random.shuffle(perguntas)

def verificar_resposta(pergunta, indice_escolhido):
    return indice_escolhido == pergunta["resposta"]

def atualizar_pontos(acertou, pontos):
    if acertou:
        pontos += 1
    return pontos

def salvar_ranking(nome, pontos):
    with open("ranking.csv", "a", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([nome, pontos])

def carregar_ranking():
    ranking = []
    try:
        with open("ranking.csv", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)
            for linha in leitor:
                if linha: # Evita linhas vazias
                    ranking.append({
                        "nome": linha[0],
                        "pontos": int(linha[1])
                    })
    except FileNotFoundError:
        pass
    return ranking

def ordenar_ranking(ranking):
    ranking.sort(key=lambda jogador: jogador["pontos"], reverse=True)
    return ranking

def desenhar_texto_quebrado(superficie, texto, posicao, largura_maxima, fonte, cor):
    palavras = texto.split(' ')
    linhas = []
    linha_atual = ""
    
    for palavra in palavras:
        test_linha = linha_atual + palavra + " "
        if fonte.size(test_linha)[0] < largura_maxima:
            linha_atual = test_linha
        else:
            linhas.append(linha_atual)
            linha_atual = palavra + " "
    linhas.append(linha_atual)
    
    x, y = posicao
    for linha in linhas:
        texto_renderizado = fonte.render(linha, True, cor)
        superficie.blit(texto_renderizado, (x, y))
        y += fonte.get_linesize() + 5