"""
OP e DELIM  -  RESPONSÁVEL: INTEGRANTE 3

Preencher a tabela δ com as transições de operadores (1 e 2 caracteres)
e delimitadores. Use SEMPRE adicionar(estado, simbolos, destino) de afd.py.
"""

from afd import adicionar


def montar_op_delim():
    """
    TODO (Integrante 3)

    Saídas de q0:   + - * /   -> q_op
                    = < >     -> q_op1
                    !         -> q_excl
                    ( ) { } ; -> q_delim

    Demais:         q_op1  --=--> q_op2      (==, <=, >=)
                    q_excl --=--> q_op2      (!=)
                    q_op, q_op2, q_delim: nenhuma transição

    Lembrete: q_excl NÃO é final. '!' sozinho gera erro léxico (a!b, !x).
    """
    pass
