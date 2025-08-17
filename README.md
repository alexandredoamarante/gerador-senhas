 # 🔐 Gerador de Senhas Seguras


Este é um projeto simples desenvolvido em Python usando o framework Flask que gera senhas aleatórias seguras, com o tamanho definido pelo usuário.

---

## Objetivo

Criar um gerador de senhas que permita ao usuário escolher o tamanho da senha e gere uma senha forte combinando letras maiúsculas, minúsculas, números e símbolos especiais.

---

## Tecnologias utilizadas

- Python 3  
- Flask (framework web)  
- HTML (template simples para a interface)

## ✅ Conteúdo deste repositório
- `app.py` — aplicação Flask
- `templates/index.html` — interface simples
- `requirements.txt` — dependências
- `.gitignore` — arquivos ignorados
- `LICENSE` — licença MIT

## ▶️ Como executar localmente
1. Clone o repositório:
   ```bash
   git clone https://github.com/alexandredoamarante/gerador-senhas.git
   cd gerador-senhas
   ```
2. Crie um ambiente virtual (recomendado) e ative:
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS / Linux
   source venv/bin/activate
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Rode a aplicação:
   ```bash
   python app.py
   ```
5. Abra no navegador:
   ```
   http://127.0.0.1:5000
   ```
##O que aprendi com este projeto

Durante o desenvolvimento deste projeto, aprendi e pratiquei:

Criar e rodar uma aplicação simples usando Flask.

Estruturar pastas e arquivos básicos de um projeto Flask (app.py, templates/).

Usar HTML para criar uma interface básica integrada ao Flask.

Gerar senhas seguras em Python utilizando o módulo random e combinando letras, números e símbolos.

Criar e usar um arquivo requirements.txt para gerenciar dependências.

Configurar e ativar um ambiente virtual (venv) no Python.

Entender como rodar a aplicação localmente e acessar no navegador.

Adicionar boas práticas ao repositório como .gitignore e LICENSE.


