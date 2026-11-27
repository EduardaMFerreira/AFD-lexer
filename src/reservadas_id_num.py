"""
RESERVADA, ID e NUM  -  RESPONSÁVEL: INTEGRANTE 2

Preencher a tabela δ com as transições das reservadas (trie), de ID e de NUM.
Use SEMPRE adicionar(estado, simbolos, destino) importada de afd.py.

PROIBIDO: reconhecer tudo como ID e filtrar com "if palavra in lista" (RF02).
A diferença entre reservada e ID tem que estar nos ESTADOS.
"""

from afd import adicionar, LETRAS, DIGITOS, LDU


def montar_reservadas_id_num():
    # 1) Saídas de q0
    adicionar("q0", {"s"}, "q_s")
    adicionar("q0", {"e"}, "q_e")
    adicionar("q0", {"r"}, "q_r")
    adicionar("q0", LETRAS - {"s", "e", "r"}, "q_id")
    adicionar("q0", DIGITOS, "q_num")
    # '_' em q0: sem transição -> q_erro por padrão

    # 2) e 3) Tries + desvio para q_id
    # Cada cadeia: lista de estados; o estado i lê a letra palavra[i+1].
    cadeias = [
        ("senao",    ["q_s", "q_se", "q_sen", "q_sena", "q_senao"]),
        ("enquanto", ["q_e", "q_en", "q_enq", "q_enqu", "q_enqua",
                      "q_enquan", "q_enquant", "q_enquanto"]),
        ("retorne",  ["q_r", "q_re", "q_ret", "q_reto", "q_retor",
                      "q_retorn", "q_retorne"]),
    ]

    for palavra, estados in cadeias:
        for i in range(len(estados) - 1):
            proxima = palavra[i + 1]
            adicionar(estados[i], {proxima}, estados[i + 1])   # segue a trie
            adicionar(estados[i], LDU - {proxima}, "q_id")     # qualquer outra L, D ou _
        # último estado da cadeia: não há próxima letra
        adicionar(estados[-1], LDU, "q_id")

    # 4) Laços
    adicionar("q_id", LDU, "q_id")
    adicionar("q_num", DIGITOS, "q_num")