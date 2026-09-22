# Estudos_python
Linguagem paython pura desde o inicio


Python/
├── Exercicios/          ← seus notebooks (Mod-01, 02, 03...)
│   ├── .venv/           ← aqui sim, use venv + pip
│   ├── Mod-01-...py
│   ├── Mod-02-...py
│   └── ...
│
└── CRUD/                ← projeto "de verdade"
    ├── BACKEND/
    ├── pyproject.toml   ← Poetry gerencia tudo aqui
    ├── .gitignore
    └── ...




    Treinamento Python — Exercícios e Fundamentos

Repositório de estudos práticos de Python, organizado por módulos que evoluem do básico (variáveis, tipos, erros) até estruturas de dados e funções, além de um projeto CRUD separado.

Nota: não consegui acessar o conteúdo do repositório diretamente (o GitHub bloqueou o acesso automatizado e o repositório não apareceu nos resultados de busca — provavelmente é privado). Este README foi montado a partir da estrutura de pastas/arquivos da captura de tela que você enviou. Se quiser um README mais detalhado (com trechos de código, funções específicas, exemplos de saída), me envie o conteúdo dos .py (upload direto aqui no chat) que eu refino o documento.

📁 Estrutura do repositório
Python/
├── CRUD/                                   # Projeto prático de CRUD (Create, Read, Update, Delete)
└── Exercicios/
    ├── .gitignore
    ├── Configuracoes.md
    ├── Mod-01-Notebook_Exercicios_Fund.py
    ├── Mod-02-Notebook_Exercicios_Tipos_Erros.py
    ├── Mod-03-Notebook_Estrutura_dados.py
    ├── Mod-04-1-Notebook_Funcoes_Procedimentos.py
    ├── Mod-04-2-Notebook_Param_Args_Func_Unpa...py
    ├── README.md
    ├── teste.py
    └── teste_00.py
🎯 Objetivo do treinamento

Consolidar a base da linguagem Python de forma incremental — cada módulo constrói em cima do anterior — para dar suporte à transição para engenharia de dados moderna (ETL, automação, scripts de tratamento de dados).

📚 Módulos e o que foi aprendido
Mod-01 — Exercícios Fundamentais
Sintaxe básica: variáveis, tipos primitivos (int, float, str, bool)
Entrada e saída de dados (input(), print(), formatação de strings)
Operadores aritméticos, relacionais e lógicos
Por quê: é a base para tudo que vem depois — sem entender tipos e operadores, estruturas mais complexas (loops, funções) ficam difíceis de depurar.
Mod-02 — Tipos e Erros
Conversão entre tipos (int(), str(), float()) e os erros comuns causados por conversões inválidas
Tratamento de exceções (try/except)
Por quê: entender por que um erro acontece (e não só corrigi-lo) evita repetir o mesmo bug em scripts de produção — especialmente relevante para pipelines de dados, onde dados "sujos" quebram conversões de tipo.
Mod-03 — Estrutura de Dados
Listas, tuplas, dicionários e/ou sets
Operações de manipulação (indexação, slicing, métodos nativos)
Por quê: estruturas de dados são a base de qualquer transformação de dados (equivalente conceitual a registros/colunas em ETL).
Mod-04-1 — Funções e Procedimentos
Definição de funções (def), diferença entre função (retorna valor) e procedimento (executa uma ação)
Escopo de variáveis (local vs. global)
Por quê: modularizar código é o que torna scripts reutilizáveis — princípio direto de qualquer pipeline ETL bem escrito.
Mod-04-2 — Parâmetros, Argumentos e Unpacking
Parâmetros posicionais, nomeados e valores default
*args e **kwargs
Unpacking de listas/dicionários
Por quê: entender *args/**kwargs é pré-requisito para ler bibliotecas de terceiros (pandas, boto3, etc.) cujas assinaturas de função dependem disso.
Arquivos auxiliares
teste.py / teste_00.py: scripts de teste/rascunho usados durante o estudo dos módulos acima
Configuracoes.md: anotações de configuração do ambiente de estudo
.gitignore: arquivos/pastas excluídos do versionamento
🗂 Projeto CRUD

Pasta separada com uma aplicação prática de CRUD, aplicando os conceitos dos módulos de Exercícios em um caso de uso mais próximo do "mundo real" (persistência e manipulação de registros).

🚀 Próximos passos sugeridos
Adicionar testes automatizados (pytest) aos módulos já feitos
Documentar o projeto CRUD com seu próprio README (tecnologias usadas, como rodar)
Seguir para módulos de manipulação de arquivos, POO (classes/objetos) e bibliotecas externas