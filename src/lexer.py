"""
Analisador Léxico (AFD) - Tema 16
Linguagens Formais e Autômatos 2026.2 - Prof. Dr. Leonardo Angelo

PONTO DE ENTRADA E MONTAGEM  -  RESPONSÁVEL: INTEGRANTE 1

Mapa dos módulos (um responsável por arquivo):
  afd.py                 Integrante 1   núcleo: Q, Σ, q0, F, poço, delta
  reservadas_id_num.py   Integrante 2   transições de RESERVADA, ID e NUM
  op_delim.py            Integrante 3   transições de OP e DELIM
  motor.py               Integrante 3   maior prefixo (ler_lexema)
  analisador.py          Integrante 4   espaços, laço da linha, erros com posição
  saida.py               Integrante 4   caminho de estados e mensagens
  lexer.py               Integrante 1   monta o AFD e executa
  ../testes/             Integrante 5   25 casos e script executor

REGRAS DO PROJETO (valem para todo o grupo):
  - PROIBIDO: re, split, isalpha, isdigit, etc.
  - PROIBIDO reconhecer tudo como ID e filtrar com "if palavra in lista".
  - Cada integrante edita SOMENTE os seus arquivos.
  - Uma branch por integrante: integrante2, integrante3, integrante4, integrante5.

CONTRATOS ENTRE OS MÓDULOS (não mudar sem avisar o grupo):
  motor.ler_lexema(linha, inicio)  -> (categoria, lexema, caminho)  ou  None
  analisador.analisar_linha(linha) -> (tokens, erro)
      tokens: lista de (categoria, lexema, caminho); caminho = lista de estados
      erro:   None  ou  (caractere, posicao)   # posicao a partir de 1
  saida.formatar_saida(tokens, erro) -> string
"""

import sys

from afd import TRANSICOES, adicionar, ESPACO, verificar_afd
from reservadas_id_num import montar_reservadas_id_num
from op_delim import montar_op_delim
from analisador import analisar_linha
from saida import formatar_saida


def construir_afd():
    """Monta a tabela δ chamando o preenchimento de cada integrante."""
    TRANSICOES.clear()
    montar_reservadas_id_num()          # Integrante 2
    montar_op_delim()                   # Integrante 3
    adicionar("q0", ESPACO, "q0")       # Integrante 1: espaço é laço em q0


def processar(linha):
    """Analisa uma linha e devolve o texto de saída. Usado também pelos testes."""
    tokens, erro = analisar_linha(linha)
    return formatar_saida(tokens, erro)


def main():
    construir_afd()
    if len(sys.argv) > 1 and sys.argv[1] == "--verificar":
        verificar_afd()
        return
    if len(sys.argv) > 1:
        linha = sys.argv[1]
    else:
        linha = input("Digite a linha: ")
    print(processar(linha))


if __name__ == "__main__":
    main()
