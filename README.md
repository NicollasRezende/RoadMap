# Roadmap de Estudos em TI

Roadmap de estudos criado para acompanhar a evolução de profissionais que estão iniciando na área de Tecnologia da Informação.

A proposta deste repositório é servir como material de apoio para aulas, estudos, exercícios e projetos práticos, partindo dos fundamentos da programação até conceitos utilizados no desenvolvimento de software em ambientes profissionais.

> **Objetivo:** construir uma base sólida de programação e desenvolvimento de software, aprendendo não apenas a escrever código, mas também a trabalhar com ferramentas, processos e práticas utilizadas no mercado.

---

## Sobre o Roadmap

Este roadmap foi dividido em módulos progressivos.

A ideia é evitar aprender ferramentas isoladamente. Antes de aprender um framework, vamos entender os fundamentos necessários para utilizá-lo corretamente.

A sequência proposta é:

```text
Fundamentos de Programação
          │
          ▼
       Python
          │
          ▼
    Orientação a Objetos
          │
          ▼
       FastAPI
          │
          ▼
        Java
          │
          ▼
    Orientação a Objetos
          │
          ▼
       Spring
          │
          ▼
   Git / GitHub / CI/CD
          │
          ▼
 Processos de Desenvolvimento
          │
          ▼
      Inteligência Artificial
       no ambiente de trabalho
```

---

# Módulos

## Módulo 1 — Python

### Objetivo

Aprender os fundamentos da programação utilizando Python como primeira linguagem.

Neste módulo, o foco principal não será apenas aprender Python, mas desenvolver o raciocínio necessário para programar.

### Conteúdos

- Introdução à programação
- Algoritmos e lógica de programação
- Variáveis
- Tipos de dados
- Operadores
- Entrada e saída de dados
- Estruturas condicionais
- Estruturas de repetição
- Listas
- Tuplas
- Dicionários
- Sets
- Funções
- Parâmetros e argumentos
- Retorno de funções
- Tratamento de exceções
- Organização de código
- Módulos e imports
- Ambientes virtuais
- Orientação a Objetos
  - Classes
  - Objetos
  - Atributos
  - Métodos
  - Encapsulamento
  - Herança
  - Polimorfismo
  - Composição
- Boas práticas de programação

### FastAPI

Após consolidar os fundamentos de Python, será introduzido o desenvolvimento de APIs utilizando FastAPI.

Conteúdos:

- O que é uma API
- HTTP
- Métodos HTTP
- Status Codes
- JSON
- Rotas
- Parâmetros
- Request e Response
- Validação de dados
- Pydantic
- Organização de uma API
- CRUD
- Documentação automática
- Integração com banco de dados

### Projeto

Ao final do módulo, será desenvolvido um projeto utilizando Python e FastAPI para aplicar os conceitos aprendidos.

---

# Módulo 2 — Java

## Objetivo

Consolidar os fundamentos de programação e aprofundar os conceitos de Orientação a Objetos utilizando Java.

Java será utilizado para reforçar conceitos que já foram apresentados em Python e introduzir conceitos importantes presentes em aplicações corporativas.

### Conteúdos

#### Fundamentos

- Sintaxe Java
- Variáveis
- Tipos primitivos
- Strings
- Operadores
- Condicionais
- Loops
- Arrays
- Métodos
- Entrada e saída
- Tratamento de exceções

#### Orientação a Objetos

- Classes
- Objetos
- Atributos
- Métodos
- Construtores
- `private`
- `public`
- `protected`
- Encapsulamento
- Getters e Setters
- Herança
- Polimorfismo
- Abstração
- Classes abstratas
- Interfaces
- Composição

#### Java na prática

- Collections
- `List`
- `Set`
- `Map`
- Generics
- Enums
- Exceptions
- Organização de projetos
- Pacotes
- Boas práticas
- SOLID

---

## Spring

Depois dos fundamentos de Java e Orientação a Objetos, iniciaremos o desenvolvimento de aplicações utilizando Spring.

### Conteúdos

- O que é Spring
- Spring Boot
- Estrutura de uma aplicação
- Injeção de dependência
- Beans
- Controllers
- Services
- Repositories
- DTOs
- APIs REST
- Validação
- Tratamento de exceções
- Persistência de dados
- JPA
- Hibernate
- Banco de dados
- Configurações
- Profiles
- Logs
- Boas práticas de arquitetura

### Projeto

Ao final do módulo será desenvolvido um projeto completo utilizando Java + Spring Boot.

O objetivo será aplicar os conceitos de programação, Orientação a Objetos, APIs REST, banco de dados e organização de uma aplicação real.

---

# Módulo 3 — Git, CI/CD e Processos

## Objetivo

Aprender como o desenvolvimento de software funciona em um ambiente profissional.

Programar é apenas uma parte do trabalho de um desenvolvedor.

Neste módulo serão apresentados os processos e ferramentas utilizados para trabalhar em equipe e entregar software.

### Git

- O que é Git
- Repositórios
- `clone`
- `add`
- `commit`
- `push`
- `pull`
- `fetch`
- `merge`
- `rebase`
- Branches
- Resolução de conflitos
- Tags
- Histórico
- `stash`

### GitHub

- Repositórios
- Issues
- Pull Requests
- Code Review
- Branch Protection
- Releases
- README
- Organização de projetos

### Processos de desenvolvimento

- Trabalho em equipe
- Organização de tarefas
- Kanban
- Scrum
- Issues
- Tasks
- Estimativas
- Code Review
- Pull Request
- Definition of Done
- Comunicação técnica
- Documentação

### CI/CD

- O que é CI
- O que é CD
- Pipelines
- Build
- Testes automatizados
- Lint
- Análise de código
- Artefatos
- Deploy
- Ambientes
- Desenvolvimento
- Homologação
- Produção
- Automação de entregas

### Projeto

Criar um pipeline de CI/CD para um dos projetos desenvolvidos nos módulos anteriores.

---

# Módulo 4 — Inteligência Artificial no Ambiente de Trabalho

## Objetivo

Aprender a utilizar Inteligência Artificial como ferramenta de produtividade e desenvolvimento, entendendo também suas limitações e riscos.

A IA não será tratada como substituta do conhecimento técnico.

O objetivo é aprender a utilizá-la como uma ferramenta dentro do processo de desenvolvimento.

### Conteúdos

- O que é IA
- Modelos de linguagem
- LLMs
- Contexto
- Prompts
- Engenharia de Prompt
- Geração de código
- Explicação de código
- Debugging
- Refatoração
- Code Review
- Testes
- Documentação
- Geração de SQL
- Automação de tarefas
- Análise de logs
- Análise de erros
- Brainstorming técnico

### IA no desenvolvimento

Exemplos de utilização:

```text
Problema
   │
   ▼
Entender o problema
   │
   ▼
Propor uma solução
   │
   ▼
Utilizar IA como apoio
   │
   ▼
Revisar criticamente o resultado
   │
   ▼
Testar
   │
   ▼
Validar
   │
   ▼
Implementar
```

A IA pode acelerar o trabalho, mas o desenvolvedor continua responsável pelo resultado produzido.

### Segurança e boas práticas

- Não enviar informações sensíveis
- Não compartilhar credenciais
- Não expor dados de clientes
- Não copiar código sem entender
- Validar respostas geradas por IA
- Revisar código
- Testar soluções
- Verificar dependências
- Avaliar riscos de segurança
- Respeitar políticas da empresa

---

# Projetos

Os projetos serão utilizados para consolidar os conhecimentos adquiridos durante o roadmap.

A ideia é evoluir os projetos conforme novos conceitos são apresentados.

### Projeto 1 — Python

Aplicação desenvolvida utilizando os fundamentos de Python.

### Projeto 2 — API

API desenvolvida utilizando Python + FastAPI.

### Projeto 3 — Java

Aplicação desenvolvida utilizando Java e Orientação a Objetos.

### Projeto 4 — Spring Boot

API REST desenvolvida utilizando Java + Spring Boot + banco de dados.

### Projeto 5 — Pipeline

Integração de um projeto com Git, CI/CD e processos de desenvolvimento.

---

# Metodologia

As aulas serão divididas entre teoria e prática.

A estrutura esperada para cada conteúdo é:

```text
1. Conceito
   ↓
2. Exemplo
   ↓
3. Implementação
   ↓
4. Exercício
   ↓
5. Desafio
   ↓
6. Revisão
```

O objetivo é que cada assunto seja acompanhado por código e exercícios práticos.

---

# Regras de estudo

## 1. Não decorar código

O objetivo não é memorizar sintaxe.

É entender:

- o problema;
- a solução;
- por que aquela solução funciona;
- quais alternativas existem;
- quais são os trade-offs.

## 2. Não copiar código sem entender

Código encontrado na internet ou gerado por IA deve ser analisado antes de ser utilizado.

## 3. Errar faz parte

Erros de compilação, exceptions e bugs fazem parte do processo de desenvolvimento.

Aprender a interpretar um erro é uma habilidade fundamental para um desenvolvedor.

## 4. Praticar

Programação não é uma habilidade que se aprende apenas assistindo aulas.

É necessário escrever código.

## 5. Perguntar

Dúvidas fazem parte do processo.

Se alguma coisa não estiver clara, o objetivo é entender o conceito antes de avançar.

---

# Objetivo Final

Ao concluir o roadmap, o aluno deverá possuir uma base para:

- compreender lógica de programação;
- desenvolver aplicações em Python;
- desenvolver APIs com FastAPI;
- compreender Orientação a Objetos;
- desenvolver aplicações em Java;
- desenvolver APIs com Spring Boot;
- utilizar Git e GitHub;
- trabalhar com branches e Pull Requests;
- compreender processos de desenvolvimento;
- compreender CI/CD;
- trabalhar em equipe utilizando ferramentas de desenvolvimento;
- utilizar Inteligência Artificial como ferramenta de produtividade;
- compreender os riscos e limitações do uso de IA;
- continuar evoluindo de forma independente.

---

# Progresso

## Módulo 1 — Python

- [ ] Introdução à programação
- [ ] Sintaxe Python
- [ ] Variáveis e tipos
- [ ] Condicionais
- [ ] Loops
- [ ] Coleções
- [ ] Funções
- [ ] Exceções
- [ ] Orientação a Objetos
- [ ] Projeto Python
- [ ] Introdução a APIs
- [ ] FastAPI
- [ ] Projeto FastAPI

## Módulo 2 — Java

- [ ] Sintaxe Java
- [ ] Variáveis e tipos
- [ ] Condicionais
- [ ] Loops
- [ ] Métodos
- [ ] Classes e objetos
- [ ] Construtores
- [ ] Encapsulamento
- [ ] Getters e Setters
- [ ] Modificadores de acesso
- [ ] Herança
- [ ] Polimorfismo
- [ ] Interfaces
- [ ] Collections
- [ ] Exceptions
- [ ] Projeto Java
- [ ] Spring Boot
- [ ] API REST
- [ ] Banco de dados
- [ ] Projeto Spring

## Módulo 3 — Git, CI/CD e Processos

- [ ] Git
- [ ] GitHub
- [ ] Branches
- [ ] Merge
- [ ] Rebase
- [ ] Pull Requests
- [ ] Code Review
- [ ] Processos de desenvolvimento
- [ ] CI
- [ ] CD
- [ ] Pipelines
- [ ] Deploy

## Módulo 4 — IA

- [ ] Fundamentos de IA
- [ ] LLMs
- [ ] Prompting
- [ ] Geração de código
- [ ] Debugging
- [ ] Refatoração
- [ ] Code Review
- [ ] Testes
- [ ] Documentação
- [ ] Automação
- [ ] Segurança
- [ ] Uso responsável de IA

---

# Como utilizar este repositório

A recomendação é seguir os módulos em ordem.

Cada módulo possui conteúdos teóricos, exemplos de código, exercícios e projetos.

Não é necessário ter conhecimento prévio de programação para iniciar o roadmap.

O mais importante é acompanhar as aulas, praticar os exercícios e desenvolver os projetos propostos.

---

## Em construção

Este roadmap está em desenvolvimento e será atualizado conforme novos conteúdos, exercícios e projetos forem adicionados.

A estrutura pode ser modificada ao longo do curso de acordo com as necessidades dos alunos e com os conhecimentos adquiridos durante as aulas.