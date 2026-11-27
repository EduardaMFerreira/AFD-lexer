"""
RESERVADA, ID e NUM  -  RESPONSÁVEL: INTEGRANTE 2

Preencher a tabela δ com as transições das reservadas (trie), de ID e de NUM.
Use SEMPRE adicionar(estado, simbolos, destino) importada de afd.py.

PROIBIDO: reconhecer tudo como ID e filtrar com "if palavra in lista" (RF02).
A diferença entre reservada e ID tem que estar nos ESTADOS.
"""

from afd import adicionar, LETRAS, DIGITOS, LDU


def montar_reservadas_id_num():
    """
    TODO (Integrante 2)

    1) Saídas de q0:   s -> q_s ; e -> q_e ; r -> q_r
                       outra letra (a..z menos s, e, r) -> q_id
                       D (0..9) -> q_num
       (q0 com '_' NÃO tem transição: cai em q_erro por padrão)

    2) Trie de senao:     q_s -e-> q_se -n-> q_sen -a-> q_sena -o-> q_senao
       Trie de enquanto:  q_e -n-> q_en -q-> q_enq -u-> q_enqu -a-> q_enqua
                          -n-> q_enquan -t-> q_enquant -o-> q_enquanto
       Trie de retorne:   q_r -e-> q_re -t-> q_ret -o-> q_reto -r-> q_retor
                          -n-> q_retorn -e-> q_retorne

    3) Em TODOS os estados das 3 cadeias:
       "outra L, D, U" (letras diferentes da próxima letra da cadeia
       + todos os dígitos + '_') -> q_id
       Em q_senao, q_enquanto e q_retorne não há próxima letra:
       LDU inteiro -> q_id.

    4) Laços:  q_id  --LDU--> q_id        q_num --D--> q_num

    Dica: LETRAS - {"e"} dá "todas as letras menos e".
    Confira: se1, sena, senao2, senao_, enquant, retorne_x, 12abc.
    """
    pass
