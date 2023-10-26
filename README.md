# Projeto Disciplinar – Compilador - 2023 - 2

Este é o repositorio do Projeto Disciplinar de Compiladores para o ano de 2023, turma 2.

## Equipe

- [Erick Lemmy dos Santos Oliveira](https://github.com/eriklemy/Compilador)
- Gabrielle Batista Garcia
- Leandro Ricardo Guimarães
- [Matheus Herman](https://github.com/matheusherman/Projeto_Compilador#readme)

## Objetivo

O objetivo deste projeto é permitir que você pesquise e aplique os conceitos de compiladores em uma plataforma de sistemas embarcados, como Arduino Mega, Raspberry PI ou Tiva, baseada na tecnologia ARM. 

### Requisitos da Linguagem

A seguir, estão listados os principais requisitos que a linguagem deve atender:

- [x] Estrutura do Programa: Um programa na linguagem consiste em um bloco de declarações definidas.

- [] Tipos Básicos: A linguagem deve definir tipos básicos para representar dados, incluindo inteiros e números de ponto flutuante de acordo com o padrão IEEE-754 de 16 bits.

- [x] Expressões e Operadores: Deve ser implementada a precedência de operadores e associatividade corretas em expressões matemáticas. Use não-terminais para definir níveis de precedência e um não-terminal "factor" para tratar expressões entre parênteses, identificadores, referências de arranjos e constantes.

- [x] Tipos Estáticos: A linguagem deve ser de tipos estáticos, ou seja, os tipos de variáveis, valores e expressões precisam ser explicitamente definidos no código.

- [x] Interção com Hardware: É necessário definir regras de produção para interação com o hardware, permitindo ler e escrever em pinos do microcomputador, portas seriais, e em componentes opcionais, como conversores digital-analógico e analógico-digital.

## Descrição do Trabalho

Este projeto está dividido em três fases, cada uma com sua entrega correspondente e apresentação:

### [Fase 1 - Definição da Linguagem e Análise Léxica](https://github.com/eriklemy/Compilador/tree/main/Fase%201)

Nesta fase, você deverá criar uma linguagem de programação que permita a criação de programas para a plataforma de sistemas embarcados escolhida. A linguagem deve ser definida a partir de um esboço dado e deve incluir declarações para interagir com o hardware, tipos de dados estáticos, manipulação de números inteiros e de ponto flutuante de acordo com o padrão IEEE-754 de 16 bits, além de regras de produção para interação com o hardware. Você também deve criar no mínimo três exemplos de código que demonstrem todas as funcionalidades da linguagem.

### [Fase 2 - Verificação de Código – Análise Sintática e Semântica](https://github.com/eriklemy/Compilador/tree/main/Fase%202)

Nesta fase você deverá implementar um analisador sintático usando um parser, usando LL1, ou LR1 e uma estrutura baseada em cálculo de sequentes para a verificação dos tipos dos identificadores, valores e expressões criadas na sua linguagem. 

Todas as linguagens criadas deverão utilizar tipos estáticos. Ou seja, os tipos precisam ser definidos
no código, arquivo de texto, que contém seu programa.

Estes dois analisadores, devem ser implementados em Python, ou C++, recebem o texto contendo o
código na linha de comando e devolvem, relatórios de erro contendo o número da linha onde o erro
se encontra, e uma árvore sintática, contendo os lexemas identificados, com suas classes, tipos e
posições definidas.

A Entrega será composta dos documentos necessários para explicar o código desenvolvido, a
apresentação deste código em sala e dos links para teste e validação do código desenvolvido. Para
os testes, você deverá fornecer, no mínimo três códigos diferentes escritos na sua linguagem. Estes
códigos devem apresentar todas as funcionalidades da linguagem e permitir a validação do código
por meio de testes de indiquem as capacidades de verificação de erros dos três analisadores.

### Fase 3 - Geração de Código de Máquina e Testes

TODO: Escrever

## Normas e Padronização

- Todos os documentos produzidos, incluindo código-fonte, relatórios e apresentações, devem seguir as normas da ABNT em relação a fontes, espaçamentos, identificação de figuras, quadros e tabelas, e a utilização de referências de pesquisa.

## Apresentações

- Cada entrega deve incluir uma apresentação dos resultados.
- As apresentações devem ser claras e informativas, destacando os principais pontos do trabalho.

## Documentação Adicional

- Registro de todas as decisões de design, desafios encontrados e soluções implementadas ao longo do projeto. Isso pode ser útil para futuros desenvolvimentos e para explicar seu processo.
