Opção 1 — Rápida (instalar direto, ignorando a trava)
No terminal:

bash
/home/flrm/.local/bin/python3.14 -m pip install ipykernel -U --user --break-system-packages

--break-system-packages VS Code sugeriu. 
Isso resolve o erro e permite rodar as células # %% como se fosse Jupyter.

Opção 2 — Recomendada (ambiente virtual)
Mais limpo e evita esse tipo de conflito no futuro:

bash
cd ~/Projetos/Python
python3.14 -m venv .venv
source .venv/bin/activate
pip install ipykernel pandas
