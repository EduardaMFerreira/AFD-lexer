"""
NÚCLEO DO AFD  -  RESPONSÁVEL: INTEGRANTE 1

Aqui ficam as 5 partes do autômato M = (Q, Σ, δ, q0, F):
  Q  -> ESTADOS (29)
  Σ  -> ALFABETO
  δ  -> TRANSICOES + delta()
  q0 -> INICIAL
  F  -> FINAIS (26, com a categoria de cada um)
e o estado poço ERRO.

Os outros módulos IMPORTAM daqui. Ninguém além da Integrante 1 edita este arquivo.
"""

# --- Q: 29 estados ---------------------------------------------------
ESTADO_INICIAL_Q = ["q0"]                                                           # 1
CADEIA_SENAO = ["q_s", "q_se", "q_sen", "q_sena", "q_senao"]                        # 5
CADEIA_ENQUANTO = ["q_e", "q_en", "q_enq", "q_enqu", "q_enqua",
                   "q_enquan", "q_enquant", "q_enquanto"]                           # 8
CADEIA_RETORNE = ["q_r", "q_re", "q_ret", "q_reto",
                  "q_retor", "q_retorn", "q_retorne"]                               # 7
DEMAIS = ["q_id", "q_num", "q_op", "q_op1", "q_op2",
          "q_excl", "q_delim", "q_erro"]                                            # 8

ESTADOS = (ESTADO_INICIAL_Q + CADEIA_SENAO + CADEIA_ENQUANTO
           + CADEIA_RETORNE + DEMAIS)                                               # 29

# --- Σ: alfabeto (tudo escrito por extenso, sem isalpha/isdigit) -----
LETRAS = set("abcdefghijklmnopqrstuvwxyz")         # L
DIGITOS = set("0123456789")                        # D
SUBLINHADO = set("_")                              # U
ESPACO = set(" ")
OPERADORES = set("+-*/=!<>")
DELIMITADORES = set("(){};")

ALFABETO = LETRAS | DIGITOS | SUBLINHADO | ESPACO | OPERADORES | DELIMITADORES

# Classe "L, D, U" usada nos desvios para q_id
LDU = LETRAS | DIGITOS | SUBLINHADO

# --- q0 e poço -------------------------------------------------------
INICIAL = "q0"
ERRO = "q_erro"   # estado poço

# --- F: estado final -> categoria (26 estados finais) ----------------
FINAIS = {
    # RESERVADA (4)
    "q_se": "RESERVADA", "q_senao": "RESERVADA",
    "q_enquanto": "RESERVADA", "q_retorne": "RESERVADA",
    # ID (17): prefixos próprios das reservadas + q_id
    "q_s": "ID", "q_sen": "ID", "q_sena": "ID",
    "q_e": "ID", "q_en": "ID", "q_enq": "ID", "q_enqu": "ID",
    "q_enqua": "ID", "q_enquan": "ID", "q_enquant": "ID",
    "q_r": "ID", "q_re": "ID", "q_ret": "ID", "q_reto": "ID",
    "q_retor": "ID", "q_retorn": "ID",
    "q_id": "ID",
    # NUM (1)
    "q_num": "NUM",
    # OP (3)
    "q_op": "OP", "q_op1": "OP", "q_op2": "OP",
    # DELIM (1)
    "q_delim": "DELIM",
}
# Não finais (3): q0, q_excl, q_erro

# --- δ: função de transição ------------------------------------------
# Dicionário (estado, símbolo) -> estado.
# Tudo que NÃO estiver listado aqui vai para q_erro (δ total).
TRANSICOES = {}


def adicionar(estado, simbolos, destino):
    """Registra δ(estado, s) = destino para cada s em 'simbolos'.
    'simbolos' pode ser um conjunto/string de caracteres (ex.: LDU, "+-*/", "n").
    TODOS os integrantes devem usar esta função para preencher a tabela."""
    for s in simbolos:
        TRANSICOES[(estado, s)] = destino


def delta(estado, simbolo):
    """δ total: transição inexistente ou símbolo fora de Σ => q_erro.
    O poço q_erro absorve todos os símbolos."""
    if estado == ERRO:
        return ERRO
    return TRANSICOES.get((estado, simbolo), ERRO)


def eh_final(estado):
    return estado in FINAIS


def categoria(estado):
    return FINAIS[estado]


def verificar_afd():
    """Checagens estruturais. Rodar: python lexer.py --verificar"""
    assert len(ESTADOS) == 29, f"esperado 29 estados, há {len(ESTADOS)}"
    assert len(set(ESTADOS)) == 29, "há estados repetidos"
    assert len(FINAIS) == 26, f"esperado 26 finais, há {len(FINAIS)}"
    for f in FINAIS:
        assert f in ESTADOS, f"final {f} não está em Q"
    for nao_final in ("q0", "q_excl", "q_erro"):
        assert nao_final not in FINAIS, f"{nao_final} não deve ser final"
    assert INICIAL in ESTADOS and ERRO in ESTADOS
    for (origem, simbolo), destino in TRANSICOES.items():
        assert origem in ESTADOS and destino in ESTADOS, (origem, simbolo, destino)
        assert simbolo in ALFABETO, f"símbolo {simbolo!r} fora de Σ"
    contagem = {}
    for cat in FINAIS.values():
        contagem[cat] = contagem.get(cat, 0) + 1
    assert contagem == {"RESERVADA": 4, "ID": 17, "NUM": 1, "OP": 3, "DELIM": 1}, contagem
    print("OK: 29 estados, 26 finais (4 RESERVADA, 17 ID, 1 NUM, 3 OP, 1 DELIM).")
    print(f"Transições cadastradas até agora: {len(TRANSICOES)}")
