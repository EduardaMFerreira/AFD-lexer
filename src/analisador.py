"""
ANALISADOR DA LINHA  -  RESPONSÁVEL: INTEGRANTE 4

Percorre a linha inteira: ignora espaços, chama o motor (motor.ler_lexema)
para cada lexema e para no primeiro erro léxico.
"""

from afd import ESPACO
from motor import ler_lexema


def analisar_linha(linha):
    """
    TODO (Integrante 4) - RF06, RF07, RF08

    Algoritmo sugerido:
      i = 0
      enquanto i < len(linha):
          - se linha[i] é espaço: i += 1 e continuar (RF06, não gera token)
          - resultado = ler_lexema(linha, i)
          - se resultado é None: erro léxico em linha[i], posição i + 1
            (posição a partir de 1, contando espaços) -> guardar erro e
            PARAR a análise (RF08)
          - senão: guardar o token e avançar i pelo tamanho do lexema

    Retorna: (tokens, erro)
      tokens: lista de tuplas (categoria, lexema, caminho)
      erro:   None  ou  (caractere, posicao)

    Casos: "" (linha vazia: sem tokens, sem erro), "a!b" (erro em '!', pos 2),
           "x = 3 # 2" (erro em '#', pos 7), "_temp" (erro em '_', pos 1).
    """
    tokens = []
    erro = None
    return tokens, erro
