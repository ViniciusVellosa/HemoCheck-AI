# HemoCheck AI - Análise Inteligente de Exames de Sangue

<p align="center">
  <img src="https://github.com/user-attachments/assets/8751db8b-4180-46da-9ca9-70fc49dc8581" alt="Imagem do Projeto HemoCheck AI" width="600"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/status-concluído-green" alt="Status do Projeto: Concluído">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/OpenAI-412991?style=flat&logo=openai&logoColor=white" alt="OpenAI API">
</p>

## 📄 Descrição

O HemoCheck AI é um sistema web projetado para processar exames de sangue em formato PDF, fornecendo relatórios de saúde detalhados com base em análises automatizadas de Inteligência Artificial. O objetivo é permitir que usuários façam o upload de seus exames e obtenham uma análise rápida e precisa sobre possíveis condições de saúde.


## 🚀 Funcionalidades Principais

* **Upload de Exames:** Interface intuitiva para o envio de arquivos de exames em formato PDF.
* **Extração de Dados com OCR:** Utiliza tecnologia OCR para extrair as informações relevantes e os valores do exame de forma automatizada.
* **Análise com IA:** Integração com a API do GPT-4 da OpenAI para analisar os dados extraídos e compará-los com valores de referência.
* **Geração de Relatórios:** Cria um relatório detalhado e de fácil compreensão para o usuário, com possíveis riscos e recomendações.

## 🛠️ Tecnologias Utilizadas

O projeto foi construído utilizando as seguintes tecnologias:

* **Front-end:** HTML, CSS, JavaScript
* **Back-end:** Python com o framework Flask para o gerenciamento do servidor e da comunicação.
* **Bibliotecas Principais:**
    * `pdf2image`: Para converter as páginas do PDF em imagens.
    * `Pytesseract`: Para realizar o OCR nas imagens e extrair o texto.
    * `OpenAI API`: Para enviar os dados extraídos e receber a análise inteligente.
    * `python-dotenv`: Para gerenciamento seguro de chaves de API.

## ⚙️ Como Executar o Projeto Localmente

Para executar o HemoCheck AI no seu ambiente local, siga os passos abaixo:

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/ViniciusVellosa/HemoCheck-AI.git](https://github.com/ViniciusVellosa/HemoCheck-AI.git)
    cd HemoCheck-AI
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    # Para Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    (Certifique-se de que o arquivo `requirements.txt` está na pasta)
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure as variáveis de ambiente:**
    * Crie um arquivo chamado `.env` na raiz do projeto.
    * Dentro dele, adicione sua chave da OpenAI:
        ```
        OPENAI_API_KEY="sk-..."
        ```

5.  **Execute a aplicação:**
    ```bash
    flask run
    ```
    Abra seu navegador e acesse `http://127.0.0.1:5000`.

## 👥 Equipe do Projeto

Este projeto foi desenvolvido como parte de um trabalho acadêmico por uma equipe talentosa de estudantes de Engenharia da Computação:

* Eduardo Da Cruz Barbosa (Front-end DEV)
* Gustavo Henrique Femiano (Full-Stack DEV)
* Jean Domiciano De Menezes (Back-end DEV)
* João Pedro Marucci Pagliuso (Back-end DEV)
* **Vinicius Gussoni Vellosa (Full-Stack DEV)**
* Yasmim Fernandes (Back-end DEV, Analista de Sistemas)

## ⚖️ Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
