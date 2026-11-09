Sim. Eu deixaria como uma **cola de aula**: título → palavras-chave → explicação curta que você pode ler/usar como base → exemplo quando necessário.

# Aula 01 — Introdução à Programação

---

## 1. O que é TI?

### Tecnologia da Informação

Área responsável pelo uso de tecnologia para **armazenar, processar, transmitir, proteger e utilizar informações**. TI não se resume a programação: envolve desenvolvimento, infraestrutura, redes, segurança, dados, cloud, suporte e várias outras áreas.

### Software

Conjunto de programas, instruções e dados que fazem um computador executar determinadas tarefas. Sistemas web, aplicativos, jogos e sistemas corporativos são exemplos de software.

### Hardware

Parte física de um computador ou dispositivo. Processador, memória RAM, HD/SSD, teclado e monitor são exemplos de hardware.

### Desenvolvimento de Software

Processo de criar, manter e evoluir sistemas. Envolve entender problemas, projetar soluções, escrever código, testar, corrigir erros e disponibilizar o software para os usuários.

### Backend

Parte da aplicação responsável principalmente pelas regras de negócio, processamento de dados, APIs, autenticação e comunicação com bancos de dados e outros sistemas.

### Frontend

Parte da aplicação com a qual o usuário interage diretamente. Envolve telas, componentes, formulários, navegação e experiências de interação.

### Dados

Informações utilizadas por sistemas para realizar operações, gerar relatórios, tomar decisões e alimentar processos.

### Infraestrutura

Conjunto de recursos necessários para executar sistemas, como servidores, redes, armazenamento, sistemas operacionais e serviços de infraestrutura.

### Cloud

Uso de recursos computacionais disponibilizados pela internet, como servidores, bancos de dados, armazenamento e serviços gerenciados.

### Segurança

Área responsável por proteger sistemas, dados, usuários e infraestrutura contra acessos indevidos, ataques, vazamentos e outros riscos.

---

# 2. O que é programação?

### Programação

Programação é o processo de criar instruções para que um computador execute determinadas tarefas e resolva problemas.

Um programador pega um problema que normalmente está descrito em linguagem humana e transforma esse problema em uma sequência de instruções que uma máquina consegue executar.

### Problema

É a necessidade que precisamos resolver.

Exemplo:

> "Precisamos calcular automaticamente o salário de um funcionário após um aumento de 10%."

Antes de escrever código, precisamos entender exatamente qual problema estamos tentando resolver.

### Solução

É a estratégia utilizada para resolver o problema.

No exemplo do salário:

```text
Receber salário
      ↓
Calcular 10%
      ↓
Adicionar o aumento
      ↓
Mostrar novo salário
```

### Instrução

Uma ação que o computador deve executar.

Exemplo:

```python
print("Olá, mundo!")
```

Nesse caso, estamos instruindo o Python a mostrar uma mensagem.

### Código

É o conjunto de instruções escritas em uma linguagem de programação.

Exemplo:

```python
nome = "João"
print(f"Olá, {nome}!")
```

### Programa

É um conjunto organizado de instruções que executa uma determinada função ou resolve um determinado problema.

Um programa pode ser extremamente simples, como uma calculadora, ou extremamente complexo, como um sistema bancário.

---

# 3. Algoritmo

### Algoritmo

Um algoritmo é uma sequência organizada de passos utilizada para resolver um problema ou realizar uma tarefa.

Não é algo exclusivo da programação.

Uma receita de bolo, por exemplo, pode ser considerada um algoritmo:

```text
1. Separar os ingredientes
2. Misturar os ingredientes
3. Colocar a massa em uma forma
4. Levar ao forno
5. Esperar assar
6. Retirar do forno
```

### Sequência

Representa a ordem em que as instruções devem ser executadas.

```text
Passo 1
   ↓
Passo 2
   ↓
Passo 3
   ↓
Passo 4
```

A ordem pode mudar completamente o resultado.

### Regra

Define uma condição ou comportamento que deve ser seguido durante a execução do algoritmo.

Exemplo:

> Se o usuário tiver 18 anos ou mais, permitir o acesso.

### Passo a passo

É a decomposição de um problema em pequenas ações que podem ser executadas individualmente.

Quanto melhor conseguimos dividir um problema, mais fácil fica transformá-lo em código.

---

# 4. Pensamento Computacional

### Pensamento Computacional

É a capacidade de analisar problemas e dividi-los de uma maneira que permita criar soluções sistemáticas e executáveis.

Não significa "pensar como um computador".

Significa **aprender a estruturar problemas de maneira lógica**.

### Decomposição

Consiste em pegar um problema grande e dividi-lo em problemas menores.

Exemplo:

```text
Sistema de cadastro
│
├── Cadastrar usuário
├── Consultar usuário
├── Alterar usuário
├── Excluir usuário
└── Validar usuário
```

### Abstração

Consiste em ignorar detalhes que não são importantes para determinado problema e focar apenas no que realmente interessa.

Por exemplo, ao utilizar uma função:

```python
calcular_salario()
```

não precisamos necessariamente saber todos os detalhes internos para utilizá-la.

### Reconhecimento de padrões

Consiste em identificar comportamentos ou problemas que se repetem.

Exemplo:

```text
Cadastrar cliente
Cadastrar funcionário
Cadastrar fornecedor
```

Todos possuem características semelhantes:

```text
Receber dados
↓
Validar dados
↓
Salvar dados
```

Identificar esse padrão ajuda a criar soluções reutilizáveis.

---

# 5. Como o computador trabalha?

### Entrada

São os dados fornecidos para o programa.

Exemplos:

```text
Nome
Idade
Salário
Senha
Arquivo
Requisição HTTP
```

### Processamento

É o momento em que o programa utiliza os dados recebidos para realizar alguma operação.

Exemplo:

```text
salário = 3000

salário × 1.10

resultado = 3300
```

### Saída

É o resultado produzido pelo processamento.

Exemplo:

```text
Novo salário: R$ 3300,00
```

### Modelo principal

```text
ENTRADA
   ↓
PROCESSAMENTO
   ↓
SAÍDA
```

Esse modelo aparece praticamente em qualquer sistema.

---

# 6. Linguagem de Programação

### Linguagem de programação

É uma linguagem criada para permitir que desenvolvedores escrevam instruções que possam ser executadas por computadores.

Cada linguagem possui sua própria sintaxe, recursos e características.

Exemplos:

```text
Python
Java
JavaScript
C
C++
C#
Go
Kotlin
Rust
```

### Sintaxe

São as regras que determinam como o código precisa ser escrito.

Por exemplo, em Python:

```python
print("Olá")
```

Se escrevermos de maneira inválida:

```python
print "Olá"
```

teremos um erro porque essa sintaxe não é válida na versão moderna do Python.

### Python

Linguagem de programação de alto nível conhecida por possuir uma sintaxe relativamente simples e uma grande quantidade de bibliotecas.

Será nossa primeira linguagem porque permite focar inicialmente na lógica de programação sem adicionar uma quantidade muito grande de complexidade sintática.

### Java

Linguagem de programação fortemente utilizada em sistemas corporativos, backend, aplicações de grande porte e diversos outros contextos.

Será utilizada posteriormente para aprofundar Orientação a Objetos e desenvolvimento de aplicações corporativas.

---

# 7. Primeiro código Python

### `print()`

Função utilizada para enviar informações para a saída padrão, normalmente o terminal.

```python
print("Olá, mundo!")
```

### String

Representa uma sequência de caracteres.

```python
"Olá, mundo!"
"João"
"Python"
```

Strings normalmente são delimitadas por aspas.

### Execução

É o processo de executar as instruções presentes no programa.

Quando executamos:

```python
print("Olá, mundo!")
```

o Python interpreta essa instrução e produz:

```text
Olá, mundo!
```

---

# 8. Variáveis

### Variável

Uma variável é um nome utilizado pelo programa para referenciar um determinado valor.

```python
nome = "João"
idade = 25
```

Nesse exemplo:

```text
nome → "João"
idade → 25
```

### Atribuição

É o processo de associar um valor a uma variável.

```python
idade = 25
```

Aqui estamos atribuindo o valor `25` à variável `idade`.

### Valor

É o dado armazenado ou referenciado por uma variável.

```python
nome = "João"
```

O valor da variável `nome` é `"João"`.

### Reatribuição

Uma variável pode receber outro valor posteriormente.

```python
nome = "João"

nome = "Maria"
```

Ao final:

```text
nome → "Maria"
```

---

# 9. Tipos de Dados

### Tipo de dado

Define que tipo de informação determinado valor representa e quais operações podem ser realizadas com ele.

### `str`

Representa textos.

```python
nome = "João"
cidade = "Brasília"
```

### `int`

Representa números inteiros.

```python
idade = 25
quantidade = 10
```

### `float`

Representa números com casas decimais.

```python
altura = 1.75
preco = 199.90
```

### `bool`

Representa um valor lógico que pode ser:

```python
True
False
```

Exemplo:

```python
maior_de_idade = True
```

### `type()`

Função utilizada para verificar o tipo de determinado valor.

```python
idade = 25

print(type(idade))
```

Resultado:

```text
<class 'int'>
```

---

# 10. Entrada de dados

### `input()`

Permite receber informações digitadas pelo usuário durante a execução do programa.

```python
nome = input("Digite seu nome: ")
```

### Usuário

É quem fornece informações ou interage com o sistema.

Exemplo:

```text
Digite seu nome: João
```

O programa recebe:

```text
João
```

### Conversão de tipo

Como o `input()` retorna uma string, muitas vezes precisamos converter o valor recebido.

```python
idade = int(input("Digite sua idade: "))
```

Nesse caso:

```text
input()
   ↓
"25"
   ↓
int()
   ↓
25
```

### `int()`

Converte um valor para inteiro quando a conversão é válida.

```python
idade = int("25")
```

### `float()`

Converte um valor para número decimal.

```python
salario = float("3500.50")
```

---

# 11. Operadores

### Operadores aritméticos

São utilizados para realizar operações matemáticas.

```python
+
-
*
/
%
```

Exemplo:

```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
```

### Operador `%`

Retorna o resto de uma divisão.

```python
10 % 3
```

Resultado:

```text
1
```

É muito utilizado para descobrir, por exemplo, se um número é par:

```python
numero % 2 == 0
```

### Operadores de comparação

São utilizados para comparar valores.

```python
>
<
>=
<=
==
!=
```

Exemplo:

```python
idade = 20

print(idade >= 18)
```

Resultado:

```text
True
```

### `==`

Verifica se dois valores são iguais.

```python
idade == 18
```

### `!=`

Verifica se dois valores são diferentes.

```python
idade != 18
```

---

# 12. Condições

### Condição

Permite que o programa tome decisões diferentes dependendo de uma determinada situação.

Exemplo:

```python
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
```

### `if`

Executa um bloco de código quando uma condição é verdadeira.

```python
if idade >= 18:
```

### `else`

Executa outro bloco quando a condição do `if` não é verdadeira.

```python
else:
```

### Verdadeiro e falso

Uma condição sempre pode resultar em um valor lógico:

```text
True
False
```

Exemplo:

```python
idade >= 18
```

Se:

```text
idade = 20
```

resultado:

```text
True
```

Se:

```text
idade = 15
```

resultado:

```text
False
```

---

# 13. Primeiro programa completo

Agora junta tudo:

```python
nome = input("Nome: ")
idade = int(input("Idade: "))
salario = float(input("Salário: "))

novo_salario = salario * 1.10

print()
print(f"Olá, {nome}!")
print(f"Você tem {idade} anos.")
print(f"Seu novo salário será R$ {novo_salario:.2f}")

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
```

Aqui você pode parar e perguntar:

> **Quantos conceitos diferentes nós usamos para construir esse programa?**

Eles vão identificar:

```text
input()
variáveis
str
int
float
operações matemáticas
if
else
comparação
print()
f-string
```

Isso fecha muito bem a primeira aula porque mostra que **programação não é decorar comandos isolados**. É combinar pequenos conceitos para resolver um problema.

---

# 14. Exercício da aula

### Cadastro de usuário

**Palavras-chave:**

- `input()`
- Variáveis
- `str`
- `int`
- `print()`
- `f-string`

O aluno deve criar um programa que receba:

```text
Nome
Idade
Cidade
Profissão
```

E produza:

```text
Olá, João!

Você tem 25 anos.
Mora em Brasília.
Sua profissão é Desenvolvedor.
```

---

# 15. Desafio

### Calculadora de salário

**Palavras-chave:**

- `input()`
- `float()`
- Variáveis
- Operadores
- Multiplicação
- `print()`
- `f-string`

O programa deve:

1. Receber o nome.
2. Receber o salário.
3. Calcular um aumento de 10%.
4. Mostrar o salário atual.
5. Mostrar o valor do aumento.
6. Mostrar o novo salário.

Exemplo:

```text
Nome: João
Salário: 3000

Salário atual: R$ 3000.00
Aumento: R$ 300.00
Novo salário: R$ 3300.00
```

---

## Fechamento da aula

No final, deixa essa sequência na tela:

```text
PROBLEMA
    ↓
ALGORITMO
    ↓
LÓGICA
    ↓
CÓDIGO
    ↓
EXECUÇÃO
    ↓
RESULTADO
```

E a mensagem principal da primeira aula:

> **Programar não é decorar código. É aprender a resolver problemas de forma lógica e transformar essas soluções em instruções que o computador consegue executar.**
