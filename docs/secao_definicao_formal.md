# Definição Formal do AFD

## 1. Estratégia de modelagem

O analisador léxico é modelado como um Autômato Finito Determinístico (AFD) explícito. As palavras reservadas (`se`, `senao`, `enquanto` e `retorne`) são reconhecidas dentro da própria ramificação de identificadores, como uma árvore de prefixos (trie): cada letra de uma reservada tem um estado intermediário. Se, no meio ou logo depois da palavra, aparecer qualquer outra letra, dígito ou `_` (como em `se1` ou `senao2`), o autômato desvia para o estado genérico `q_id` e não volta mais. Nenhuma lista de strings é consultada.

A função de transição δ é total: toda transição não listada na tabela da seção 4 vai para o estado poço `q_erro`, que absorve todos os símbolos.

## 2. Definição formal (5-tupla)

**M = (Q, Σ, δ, q0, F)**

**Q (29 estados):**

| Grupo | Estados | Qtde |
|---|---|---|
| Inicial | q0 | 1 |
| Cadeia de `senao` | q_s, q_se, q_sen, q_sena, q_senao | 5 |
| Cadeia de `enquanto` | q_e, q_en, q_enq, q_enqu, q_enqua, q_enquan, q_enquant, q_enquanto | 8 |
| Cadeia de `retorne` | q_r, q_re, q_ret, q_reto, q_retor, q_retorn, q_retorne | 7 |
| Demais | q_id, q_num, q_op, q_op1, q_op2, q_excl, q_delim, q_erro | 8 |
| **Total** | | **29** |

**Σ** = { a..z, 0..9, `_`, ' ', `+`, `-`, `*`, `/`, `=`, `!`, `<`, `>`, `(`, `)`, `{`, `}`, `;` }

**q0** = q0 (estado inicial)

**F (26 estados finais) e suas categorias:**

| Categoria | Estados finais | Qtde |
|---|---|---|
| RESERVADA | q_se, q_senao, q_enquanto, q_retorne | 4 |
| ID | q_s, q_sen, q_sena, q_e, q_en, q_enq, q_enqu, q_enqua, q_enquan, q_enquant, q_r, q_re, q_ret, q_reto, q_retor, q_retorn, q_id | 17 |
| NUM | q_num | 1 |
| OP | q_op, q_op1, q_op2 | 3 |
| DELIM | q_delim | 1 |
| **Total** | | **26** |

Estados não finais (3): `q0`, `q_excl` e `q_erro` (poço). Conferência: 26 + 3 = 29.

## 3. Significado dos estados

| Estado(s) | Categoria | Significado |
|---|---|---|
| q0 | não final | Repouso entre tokens. O espaço mantém em q0 (laço), sem gerar token. |
| q_s, q_e, q_r | ID | Lido `s`, `e` ou `r` como primeira letra. Se o token acabar aqui, é um ID de uma letra. |
| q_sen, q_sena, q_en, q_enq, q_enqu, q_enqua, q_enquan, q_enquant, q_re, q_ret, q_reto, q_retor, q_retorn | ID | Lido um prefixo próprio de uma reservada. Se o token acabar aqui, é um ID válido. Se vier a próxima letra da cadeia, avança; qualquer outra letra, dígito ou `_` leva a q_id. |
| q_se | RESERVADA | Lido exatamente `se`. Se vier `n`, continua para `senao`; outra letra, dígito ou `_` vai a q_id (ex.: `se1` é ID). |
| q_senao, q_enquanto, q_retorne | RESERVADA | Lida uma reservada completa. Qualquer letra, dígito ou `_` depois dela vai a q_id (`senao2`, `retorne_x`). |
| q_id | ID | Identificador genérico: começou com letra e já não é (nem pode virar) reservada. |
| q_num | NUM | Um ou mais dígitos. Letra ou `_` depois não tem transição: o motor emite NUM e recomeça (`12abc`). |
| q_op | OP | Operador de um símbolo que não se estende: `+ - * /`. |
| q_op1 | OP | Lido `=`, `<` ou `>`. Já é operador, mas se vier `=` vira composto. |
| q_excl | não final | Lido `!`. Só é válido se vier `=` (`!=`). Caso contrário não há token: erro léxico no `!`. |
| q_op2 | OP | Operador composto: `==`, `!=`, `<=`, `>=`. |
| q_delim | DELIM | Delimitador de um símbolo: `( ) { } ;`. |
| q_erro | não final (poço) | Absorve tudo. Chegar aqui significa que o token acabou (se houve estado final antes) ou que há erro léxico. |

## 4. Tabela de transições δ

Legenda: L = a..z, D = 0..9, U = `_`. Todo símbolo não listado na linha (inclusive os fora de Σ) vai para q_erro. Estados marcados com `*` são finais.

### 4.1 Estado inicial e estados genéricos

| Estado | Transições (tudo o mais → q_erro) |
|---|---|
| → q0 | `s` → q_s; `e` → q_e; `r` → q_r; outra L → q_id; D → q_num; `+ - * /` → q_op; `= < >` → q_op1; `!` → q_excl; `( ) { } ;` → q_delim; `' '` → q0; U → q_erro |
| * q_id | L, D, U → q_id |
| * q_num | D → q_num |
| * q_op | (nenhuma) |
| * q_op1 | `=` → q_op2 |
| q_excl | `=` → q_op2 |
| * q_op2 | (nenhuma) |
| * q_delim | (nenhuma) |
| q_erro | todos os símbolos → q_erro |

### 4.2 Estados das cadeias de reservadas

Em todas as linhas, "outra L, D, U" significa as letras diferentes da próxima letra da cadeia, mais todos os dígitos e `_`.

| Estado | Categoria | Próxima letra da cadeia | Outra L, D, U |
|---|---|---|---|
| * q_s | ID | `e` → q_se | q_id |
| * q_se | RESERVADA | `n` → q_sen | q_id |
| * q_sen | ID | `a` → q_sena | q_id |
| * q_sena | ID | `o` → q_senao | q_id |
| * q_senao | RESERVADA | (nenhuma) | q_id |
| * q_e | ID | `n` → q_en | q_id |
| * q_en | ID | `q` → q_enq | q_id |
| * q_enq | ID | `u` → q_enqu | q_id |
| * q_enqu | ID | `a` → q_enqua | q_id |
| * q_enqua | ID | `n` → q_enquan | q_id |
| * q_enquan | ID | `t` → q_enquant | q_id |
| * q_enquant | ID | `o` → q_enquanto | q_id |
| * q_enquanto | RESERVADA | (nenhuma) | q_id |
| * q_r | ID | `e` → q_re | q_id |
| * q_re | ID | `t` → q_ret | q_id |
| * q_ret | ID | `o` → q_reto | q_id |
| * q_reto | ID | `r` → q_retor | q_id |
| * q_retor | ID | `n` → q_retorn | q_id |
| * q_retorn | ID | `e` → q_retorne | q_id |
| * q_retorne | RESERVADA | (nenhuma) | q_id |

Nesses estados, qualquer símbolo que não seja L, D ou U (operador, delimitador, espaço ou símbolo fora de Σ) vai a q_erro; o motor do maior prefixo então emite o token do último estado final visitado.

## 5. Motor do maior prefixo (maximal munch)

O leitor parte de q0, avança enquanto δ não levar a q_erro e guarda a posição e o estado do último estado final visitado. Quando a próxima transição vai a q_erro (ou a linha acaba):

- se houve um estado final, emite o token da categoria desse estado e recomeça em q0 logo depois do lexema;
- se não houve nenhum, reporta erro léxico no primeiro caractere do lexema que começou ali.

Assim, "encerrar token" não é um estado nem uma transição: é o comportamento do motor quando δ chega ao poço a partir de um estado final.

## 6. Diagrama

O arquivo `docs/diagrama.png` representa exatamente a tabela da seção 4: finais em círculo duplo, `q_excl` em círculo simples, o espaço como laço em q0, e as transições "outra L, D, U" para q_id agrupadas por uma seta tracejada saindo da caixa da trie.
