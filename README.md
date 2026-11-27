# Tema 16 - Analisador Léxico (AFD)

Linguagens Formais e Autômatos 2026.2 · Prof. Dr. Leonardo Angelo

**Equipe:**
1. Ana Clara de Queiroz Andrade
2. Daniela Gomes de Oliveira
3. Leandra Lima de Sousa
4. Maria Eduarda de Moura Ferreira
5. Thaís Rainara Marques de Morais

**Linguagem:** Python 3 (sem bibliotecas de expressão regular; sem `split`, `isalpha`, `isdigit` etc.)

## O que é
Analisador léxico para uma mini-linguagem, baseado em um Autômato Finito Determinístico explícito (29 estados, 26 finais, estado poço `q_erro`). Reconhece cinco categorias: `RESERVADA` (se, senao, enquanto, retorne), `ID`, `NUM`, `OP` e `DELIM`, usando maior prefixo (maximal munch). Mostra o caminho de estados de cada token e informa erros léxicos com a posição (a partir de 1).

## Estrutura
```
GRUPO_TEMA16/
├── README.md
├── src/
│   ├── afd.py                  # núcleo: Q, Σ, q0, F, poço, delta
│   ├── reservadas_id_num.py    # transições de RESERVADA, ID e NUM
│   ├── op_delim.py             # transições de OP e DELIM
│   ├── motor.py                # maior prefixo (ler_lexema)
│   ├── analisador.py           # espaços, laço da linha, erros
│   ├── saida.py                # caminho de estados e mensagens
│   └── lexer.py                # monta o AFD e executa
├── testes/
│   ├── entradas/               # 5 obrigatórias + 20 do grupo (Integrante 5)
│   └── executar_testes.py      # mostra esperado x obtido x bateu
└── docs/
    ├── diagrama.png
    ├── secao_definicao_formal.md          # Integrante 1 
    ├── secao_especificacao_er.md          # Integrante 2
    ├── secao_introducao_casos_criticos.md # Integrante 3
    ├── secao_implementacao_limitacoes.md  # Integrante 4
    ├── secao_testes_resultados.md         # Integrante 5
    └── relatorio.pdf                      # montado no final (Integrante 5)
```

## Como executar
```bash
cd src

# uma linha pela linha de comando
python lexer.py "se (x1 >= 10) { retorne x1 ; }"

# digitando a linha
python lexer.py

# verificação estrutural do AFD (29 estados, 26 finais)
python lexer.py --verificar
```

## Como rodar os testes
```bash
python testes/executar_testes.py
```
O script de testes deve adicionar `src/` ao caminho de importação e usar `processar(linha)` de `lexer.py`:
```python
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from lexer import construir_afd, processar
construir_afd()
```

## Divisão de responsabilidades (um responsável por arquivo)

| Integrante | Arquivos de código | Documento |
|---|---|---|
| 1. Maria Eduarda | `src/afd.py`, `src/lexer.py`, README e estrutura do repo | Definição Formal do AFD e `docs/diagrama.png` |
| 2. Thaís | `src/reservadas_id_num.py` | Especificação da Linguagem e Expressões Regulares |
| 3. Daniela | `src/op_delim.py`, `src/motor.py` | Introdução, Casos Críticos e revisão do diagrama |
| 4. Leandra | `src/analisador.py`, `src/saida.py` | Implementação e Limitações/Decisões |
| 5. Ana Clara | `testes/` | Testes e Resultados, Considerações Finais, PDF final |

## Contratos entre os módulos
- `motor.ler_lexema(linha, inicio)` devolve `(categoria, lexema, caminho)` ou `None`.
- `analisador.analisar_linha(linha)` devolve `(tokens, erro)`; `erro` é `None` ou `(caractere, posicao)`, com posição a partir de 1.
- `saida.formatar_saida(tokens, erro)` devolve a string final.
- Para preencher a tabela δ, usar sempre `adicionar(estado, simbolos, destino)` de `afd.py`.

