# Projeto Disciplinar – Compilador - 2023 - 2

Este é o repositorio do Projeto Disciplinar de Compiladores para o ano de 2023, turma 2.

## Equipe

- Erick Lemmy dos Santos Oliveira
- Gabrielle Batista Garcia
- Leandro Ricardo Guimarães
- Matheus Herman

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

### Fase 1 - Definição da Linguagem e Análise Léxica

Nesta fase, você deverá criar uma linguagem de programação que permita a criação de programas para a plataforma de sistemas embarcados escolhida. A linguagem deve ser definida a partir de um esboço dado e deve incluir declarações para interagir com o hardware, tipos de dados estáticos, manipulação de números inteiros e de ponto flutuante de acordo com o padrão IEEE-754 de 16 bits, além de regras de produção para interação com o hardware. Você também deve criar no mínimo três exemplos de código que demonstrem todas as funcionalidades da linguagem.

### Fase 2 - Análise Sintática e Geração de Código Intermediário

Nesta fase, você irá construir um analisador sintático para sua linguagem. O analisador sintático deve ser capaz de validar a sintaxe dos programas escritos na linguagem definida na Fase 1. Além disso, você deve implementar a geração de código intermediário para programas válidos.

### Fase 3 - Geração de Código de Máquina e Testes

Na última fase, você irá desenvolver um gerador de código de máquina para a plataforma de sistemas embarcados escolhida. O objetivo é traduzir o código intermediário gerado na Fase 2 em código executável para a plataforma alvo. Além disso, você deve realizar testes abrangentes para garantir que o compilador produza código funcional.

## Normas e Padronização

- Todos os documentos produzidos, incluindo código-fonte, relatórios e apresentações, devem seguir as normas da ABNT em relação a fontes, espaçamentos, identificação de figuras, quadros e tabelas, e a utilização de referências de pesquisa.

## Apresentações

- Cada entrega deve incluir uma apresentação dos resultados.
- As apresentações devem ser claras e informativas, destacando os principais pontos do trabalho.

## Documentação Adicional

- Mantenha um registro de todas as decisões de design, desafios encontrados e soluções implementadas ao longo do projeto. Isso pode ser útil para futuros desenvolvimentos e para explicar seu processo.

Lembre-se de que este é um projeto complexo que abrange várias áreas da computação. Planeje seu tempo adequadamente e consulte regularmente seus professores e colegas para obter orientação e apoio.
