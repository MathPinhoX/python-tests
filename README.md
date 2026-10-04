# Desafio técnico em Python

Solução em Python para os três exercícios do desafio técnico.

## Estrutura

- `main.py`: menu principal;
- `comissoes.py`: cálculo das comissões;
- `estoque.py`: movimentação de estoque;
- `juros.py`: cálculo de juros por atraso;
- `vendas.json`: dados das vendas fornecidos no desafio;
- `estoque.json`: dados iniciais de estoque fornecidos no desafio.

## Como executar

No VS Code, abra a pasta do projeto e execute no terminal:

```bash
python main.py
```

No Windows, se necessário:

```bash
py main.py
```

## Exercício 1 — Comissões

Para cada venda:

- abaixo de R$ 100,00: sem comissão;
- de R$ 100,00 até abaixo de R$ 500,00: 1%;
- a partir de R$ 500,00: 5%.

O programa lê o JSON de vendas, calcula a comissão de cada registro e acumula o resultado por vendedor.

## Exercício 2 — Estoque

O programa:

- lê os produtos do JSON;
- recebe código, tipo da movimentação, quantidade e descrição;
- permite entrada ou saída;
- impede saída maior que o saldo disponível;
- gera um identificador para a movimentação;
- retorna o estoque final do produto movimentado.

## Exercício 3 — Juros

O programa recebe o valor e a data de vencimento, compara com a data atual e aplica juros simples de 2,5% por dia de atraso:

```text
juros = valor x 0,025 x dias em atraso
```

Se ainda não houver atraso, os juros ficam em zero.

## Execução

Ao executar `main.py`, é exibido o menu:

```text
1 - Comissões
2 - Movimentação de estoque
3 - Juros por atraso
0 - Sair
```
