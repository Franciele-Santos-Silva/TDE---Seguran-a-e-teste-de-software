# Validação de Login em Python

Aplicação simples para validar usuário e senha, acompanhada de testes utilizando **Particionamento de Equivalência** e **Análise de Valor Limite**.

## Sobre o Projeto

Este projeto implementa uma função de login que valida:

- Tamanho do **usuário**: entre **4 e 12 caracteres**
- Tamanho da **senha**: entre **6 e 10 caracteres**
- Credenciais válidas (banco de dados simulado):  
  - **Usuário:** `admin`  
  - **Senha:** `123456`

Além disso, o código executa testes automáticos organizados em duas técnicas de teste de software.

## Tecnologias de Teste Utilizadas

### Particionamento de Equivalência

Garante que entradas representativas de cada classe (válidas e inválidas) sejam testadas.

### Análise de Valor Limite

Testa valores exatamente nos limites e imediatamente acima/abaixo deles.

## Executando os Testes

    python main.py
