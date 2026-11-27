"""
EXECUTOR DE TESTES  -  RESPONSÁVEL: INTEGRANTE 5

TODO (Integrante 5): para cada caso, mostrar saída esperada, saída obtida
e se bateu (Documento 1, seção 5).

Uso (a partir da raiz do repositório):
    python testes/executar_testes.py

Dica: importe o lexer assim e chame processar(linha) ou analisar_linha(linha):
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))

from lexer import construir_afd, processar   # noqa: E402,F401


def main():
    construir_afd()
    # TODO (Integrante 5):
    #  1) ler os casos de testes/entradas/
    #  2) rodar cada um no lexer
    #  3) comparar com a saída esperada (Documento 1, seção 5)
    #  4) imprimir esperada x obtida x bateu e o total de acertos
    pass


if __name__ == "__main__":
    main()
