"""
MOTOR DO MAIOR PREFIXO (maximal munch)  -  RESPONSÁVEL: INTEGRANTE 3

Lê UM lexema a partir de uma posição da linha, rodando o AFD.
Quem chama este módulo é o analisador.py (Integrante 4), que cuida de
espaços, repetição até o fim da linha e erros.
"""

from afd import INICIAL, ERRO, delta, eh_final, categoria


def emitir_token(categoria_token, lexema, caminho):
    """Monta a tupla do token. Formato combinado com o grupo:
    (categoria, lexema, caminho)  -> caminho = lista de estados."""
    return (categoria_token, lexema, caminho)


def ler_lexema(linha, inicio):
    """
    TODO (Integrante 3) - RF03

    Entrada:
      linha  : string da linha inteira
      inicio : índice (a partir de 0) do primeiro caractere do lexema.
               Garantia do analisador: linha[inicio] NÃO é espaço.

    O que fazer:
      - começar em q0 e ir aplicando delta(estado, linha[i]);
      - parar quando delta devolver ERRO (ou a linha acabar);
      - guardar o ÚLTIMO estado final visitado, o índice onde ele ocorreu
        e o caminho de estados até ele (RF05);
      - ao parar, se houve estado final: devolver
            emitir_token(categoria(ultimo_final), lexema, caminho_ate_ele)
        onde lexema = linha[inicio:fim];
      - se não houve nenhum estado final: devolver None.

    Retorno: tupla do token  OU  None (nenhum prefixo válido: erro léxico).

    Casos que precisam funcionar: senao2, 12abc, a===b, >=, a!b, se1.
    NÃO tratar espaços nem erros aqui: isso é do analisador.py.
    """
    return None
