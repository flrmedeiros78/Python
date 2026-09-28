# Estudos de Python e Engenharia de Dados

Repositório com meus estudos práticos de Python, dos fundamentos até um projeto completo com API, banco de dados e Docker. Faz parte da minha transição para engenharia de dados moderna (ETL, automação e pipelines).

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-4169E1?logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-frontend-FF4B4B?logo=streamlit&logoColor=white)

## Projetos

| Pasta | O que é | Tecnologias |
|-------|---------|-------------|
| [**CRUD/**](CRUD/) | API REST de produtos com banco de dados e front-end, tudo em containers. Projeto principal do repositório. | FastAPI, PostgreSQL, SQLAlchemy, Pydantic, Streamlit, Docker Compose, Poetry |
| [**Exercicios/**](Exercicios/) | Exercícios de fundamentos de Python, organizados por módulo. | Python |

## Destaque: CRUD de Produtos

Aplicação completa para cadastrar, listar, buscar, atualizar e remover produtos:

- **Backend:** API REST em FastAPI, com validação de dados (Pydantic) e persistência em PostgreSQL via SQLAlchemy.
- **Front-end:** interface em Streamlit que consome a API.
- **Infraestrutura:** Docker Compose para subir os serviços, e configuração por variáveis de ambiente (`.env`).

Arquitetura, endpoints, como executar e os problemas resolvidos durante o desenvolvimento estão no **[README do CRUD](CRUD/README.md)**.

## Exercícios de Python

Módulos que evoluem do básico até funções, cada um construindo sobre o anterior:

| Módulo | Assunto |
|--------|---------|
| Mod-01 | Fundamentos: variáveis, tipos, entrada e saída, operadores |
| Mod-02 | Tipos e erros: conversões e tratamento de exceções (`try/except`) |
| Mod-03 | Estruturas de dados: listas, tuplas, dicionários e sets |
| Mod-04-1 | Funções e procedimentos, escopo de variáveis |
| Mod-04-2 | Parâmetros, `*args`, `**kwargs` e unpacking |

Detalhes e o porquê de cada módulo estão no [README de Exercicios](Exercicios/README.md).

## Objetivo

Consolidar a base da linguagem de forma incremental para dar suporte à transição para engenharia de dados: scripts de tratamento de dados, automação, ETL e, mais adiante, pipelines em nuvem.

## Próximos passos

- Testes automatizados com pytest nos módulos e no CRUD
- Migrações de banco com Alembic no CRUD
- Manipulação de arquivos, POO (classes e objetos) e bibliotecas externas

## Autor

**Fabio Medeiros** — [flrmedeiros78](https://github.com/flrmedeiros78)