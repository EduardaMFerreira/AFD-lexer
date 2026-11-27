# Especificação da Linguagem e Expressões Regulares (Integrante 2)

## 1. Alfabeto Σ

Σ = L ∪ D ∪ U ∪ {espaço} ∪ OPERADORES ∪ DELIMITADORES, em que:

| Símbolo | Conjunto | Elementos |
|---|---|---|
| L | letras minúsculas | `a b c ... z` |
| D | dígitos | `0 1 2 ... 9` |
| U | sublinhado | `_` |
| — | espaço | ` ` (separador, não gera token) |
| OPERADORES | | `+ - * / = ! < >` |
| DELIMITADORES | | `( ) { } ;` |

Classe auxiliar usada nos desvios para ID: **LDU = L ∪ D ∪ U**.

Qualquer caractere fora de Σ (por exemplo letras maiúsculas, `,`, `.`, `[`, `@`) leva o autômato ao estado de erro `q_erro`.

## 2. Categorias de tokens

A linguagem possui 5 categorias de tokens.

| Categoria | Descrição | Exemplos válidos | Exemplos inválidos |
|---|---|---|---|
| **NUM** | Inteiro sem sinal: um ou mais dígitos. | `0`, `42`, `2026` | `4.2` (ponto fora de Σ), `-5` (o `-` é OP, não faz parte do número) |
| **ID** | Começa com letra; depois, letras, dígitos ou `_`. Não pode ser uma palavra reservada. | `x`, `soma_1`, `se1`, `sena`, `senao2`, `senao_`, `enquant`, `retorne_x` | `_x` (começa com `_`), `1x` (começa com dígito), `Soma` (maiúscula fora de Σ) |
| **RESERVADA** | Uma das 4 palavras reservadas. | `se`, `senao`, `enquanto`, `retorne` | `Se`, `ENQUANTO` (maiúsculas fora de Σ); `retornar` é ID, não reservada |
| **OP** | Operadores aritméticos, de atribuição e relacionais. ⚠️ | `+`, `-`, `*`, `/`, `=`, `<`, `>`, `==`, `<=`, `>=`, `!=` | `!` sozinho, `=+=`, `@` |
| **DELIM** | Delimitadores de um caractere. | `(`, `)`, `{`, `}`, `;` | `,`, `[`, `:` (fora de Σ) |

## 3. Regras de formação

1. **Maior lexema (longest match).** O analisador consome o maior prefixo aceito pelo AFD. Por isso `senao2` é um único ID, e não `senao` seguido de `2`; e `retorne_x` é um único ID.
2. **Reservada versus ID.** Um lexema é RESERVADA somente se for **exatamente** `se`, `senao`, `enquanto` ou `retorne`. Qualquer outro lexema que comece com letra é ID. Exemplos: `se1`, `sena`, `senao_` e `enquant` são ID.
3. **Distinção nos estados.** A diferença entre reservada e ID está nos estados do autômato (trie das reservadas), nunca em filtro por lista de palavras (RF02). Os prefixos próprios das reservadas (`s`, `sen`, `sena`, `e`, `en`, ..., `r`, `re`, ..., `retorn`) são finais de ID.
4. **Início de ID.** Um ID deve começar com letra. O `_` só é permitido a partir do segundo caractere; em `q0` não há transição para `_`, então ele leva a `q_erro`.
5. **NUM seguido de letra.** `q_num` só aceita dígitos. Em `12abc` o lexema NUM `12` termina ao ler `a`, e `abc` é reconhecido depois como ID (ou tratado como erro, conforme a política do analisador).
6. **Espaços.** O espaço separa tokens e não gera token.
7. **Operadores de dois caracteres.** ⚠️ `==`, `<=`, `>=` e `!=` são reconhecidos como um único OP. O `!` isolado não é final (estado `q_excl`) e, portanto, é erro.
8. **Delimitadores.** Cada delimitador é um token de um único caractere.

## 4. Expressões regulares equivalentes

Com L = `[a-z]`, D = `[0-9]` e U = `_`:

| Categoria | Expressão regular |
|---|---|
| NUM | `D+` |
| ID | `L (L \| D \| U)*`, excluindo as palavras reservadas |
| RESERVADA | `se \| senao \| enquanto \| retorne` |
| OP | `+ \| - \| * \| / \| = \| < \| > \| == \| <= \| >= \| !=` ⚠️ |
| DELIM | `( \| ) \| { \| } \| ;` |

Observação: a ER de ID descreve o conjunto de todos os identificadores sem as 4 reservadas. No AFD, essa exclusão é obtida pelos estados da trie, sem consulta a listas.

## 5. Relação com o AFD

O autômato M = (Q, Σ, δ, q0, F) possui:

- **29 estados:** `q0`; as cadeias de `senao` (5), `enquanto` (8) e `retorne` (7); e os estados `q_id`, `q_num`, `q_op`, `q_op1`, `q_op2`, `q_excl`, `q_delim` e `q_erro`.
- **26 estados finais:** 4 RESERVADA, 17 ID, 1 NUM, 3 OP e 1 DELIM.
- **Não finais:** `q0`, `q_excl` e `q_erro` (poço).
- **δ total:** toda transição não cadastrada leva a `q_erro`.

### Verificação dos casos limite

| Entrada | Último estado | Categoria |
|---|---|---|
| `se` | `q_se` | RESERVADA |
| `se1` | `q_id` | ID |
| `sena` | `q_sena` | ID |
| `senao` | `q_senao` | RESERVADA |
| `senao2` | `q_id` | ID |
| `senao_` | `q_id` | ID |
| `enquant` | `q_enquant` | ID |
| `enquanto` | `q_enquanto` | RESERVADA |
| `retorne_x` | `q_id` | ID |
| `12abc` | `q_num`, depois `q_id` | NUM + ID |
| `_x` | `q_erro` | erro |