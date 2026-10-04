# Desafio técnico em Python

Projeto preparado para executar no VS Code sem bibliotecas externas.

## Estrutura

- `main.py`: programa principal com menu e os três desafios.
- `vendas.json`: dados do desafio de comissões.
- `estoque.json`: estoque inicial e saldo atualizado após movimentações.
- `movimentacoes.json`: histórico das entradas e saídas registradas.

## Como executar no VS Code

1. Instale o Python 3 no computador, caso ainda não esteja instalado.
2. Abra o VS Code.
3. Instale a extensão **Python**, da Microsoft, se o VS Code sugerir.
4. Vá em **File > Open Folder** e abra esta pasta.
5. Abra o terminal do VS Code em **Terminal > New Terminal**.
6. Execute:

```bash
python main.py
```

No Windows, se `python` não funcionar, tente:

```bash
py main.py
```

O programa mostrará um menu:

- `1`: calcula as comissões por vendedor;
- `2`: registra entrada ou saída de estoque e atualiza o JSON;
- `3`: calcula juros de 2,5% ao dia de atraso;
- `0`: encerra.

## Lógica do desafio 1

O programa percorre cada venda e aplica a regra individualmente:

- abaixo de R$ 100,00: 0%;
- de R$ 100,00 até abaixo de R$ 500,00: 1%;
- a partir de R$ 500,00: 5%.

Depois, acumula o valor vendido e a comissão por vendedor.

Resultado esperado com os dados fornecidos:

- João Silva: comissão de **R$ 495,69**;
- Maria Souza: comissão de **R$ 465,96**;
- Carlos Oliveira: comissão de **R$ 379,38**;
- Ana Lima: comissão de **R$ 404,99**.

## Lógica do desafio 2

O programa:

1. lê o estoque do `estoque.json`;
2. recebe o código do produto;
3. recebe se a movimentação é entrada ou saída;
4. recebe quantidade e descrição;
5. impede saída maior que o estoque disponível;
6. cria um identificador único com UUID;
7. atualiza o saldo no `estoque.json`;
8. salva o histórico no `movimentacoes.json`;
9. mostra o estoque final.

## Lógica do desafio 3

O usuário informa o valor e o vencimento. O programa compara o vencimento com a data atual.

Se o título estiver vencido, calcula:

```text
juros = valor x 2,5% x dias em atraso
```

Foi adotada a interpretação de **juros simples de 2,5% por dia**, porque o enunciado apenas informa “2,5% ao dia” e não determina capitalização composta.

Se a data ainda não venceu, os dias em atraso e os juros ficam em zero.

## Como explicar na entrevista

Você pode explicar assim, com suas palavras:

> Eu organizei a solução em três funções principais, uma para cada problema. Mantive os dados em JSON, como solicitado no enunciado. Na comissão eu percorro cada venda, aplico a faixa correspondente e acumulo o resultado por vendedor. Para valores monetários usei Decimal para evitar erros de precisão de ponto flutuante. No estoque, além de entrada e saída, incluí validação de saldo, identificação única da movimentação e persistência do histórico. No cálculo de juros, comparo a data de vencimento com a data atual e aplico 2,5% por dia somente aos dias efetivamente em atraso.

### Se perguntarem por que você fez validações extras

> Porque eu quis tratar o desafio como um pequeno sistema real. Então evitei quantidade negativa, saída maior que o saldo, produto inexistente e entrada de datas ou valores inválidos.

### Se perguntarem por que usar `Decimal`

> Porque valores financeiros com `float` podem gerar pequenas diferenças de precisão. O `Decimal` me permite trabalhar e arredondar valores monetários de forma mais segura.

### Se perguntarem o que poderia melhorar

> Em uma versão maior eu separaria cada responsabilidade em módulos ou classes, colocaria testes automatizados, banco de dados e uma interface ou API. Para o escopo do desafio, mantive uma solução simples, executável e fácil de revisar.
