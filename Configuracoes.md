estou querendo usar o arquivo.py como se estivesse usando no databricks ou no jupyter. o que preciso instalar ou configurar e como fazer?

O erro é bem específico: seu Python 3.14.6 é um Python "gerenciado pelo sistema" (PEP 668), e por isso o pip install normal foi bloqueado. Isso não tem relação direta com Databricks/Jupyter — é só uma trava de segurança do seu sistema operacional (provavelmente WSL/Linux) para não misturar pacotes do sistema com pacotes do pip.

Você tem duas opções:

Opção 1 — Rápida (instalar direto, ignorando a trava)
No terminal:

bash
/home/flrm/.local/bin/python3.14 -m pip install ipykernel -U --user --break-system-packages
Só adicionei --break-system-packages ao comando que o próprio VS Code sugeriu. Isso resolve o erro imediato e permite rodar as células # %% como se fosse Jupyter.

Opção 2 — Recomendada (ambiente virtual)
Mais limpo e evita esse tipo de conflito no futuro:

bash
cd ~/Projetos/Python
python3.14 -m venv .venv
source .venv/bin/activate
pip install ipykernel pandas
Depois, no VS Code, clique em "Python 3.14.6" no canto superior direito (onde aparece agora) e selecione o interpretador dentro de .venv que acabou de criar. O VS Code vai reconhecer automaticamente e usar esse ambiente para rodar as células.