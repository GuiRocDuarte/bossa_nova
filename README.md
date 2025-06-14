# 🎶 Projeto Streamlit - Gerador de Letras Bossa Nova

Este projeto permite executar uma aplicação Streamlit no Google Colab para gerar letras de música no estilo Bossa Nova, utilizando técnicas de Processamento de Linguagem Natural (NLP).

---

## 🚀 Como Executar no Google Colab

Siga os passos abaixo para rodar a aplicação diretamente no seu navegador usando o Google Colab:

### 1. Baixar os Arquivos

Faça o download dos arquivos deste repositório.

### 2. Enviar os Arquivos para o Colab

Você pode:
- Fazer **upload direto** no Colab (ícone de pasta > upload de arquivos)
- **Ou** salvar os arquivos no seu Google Drive e montá-lo no Colab com `drive.mount`
  
Todos os arquivos devem estar na mesma pasta, **incluindo** os modelos (.keras), tokenizadores (.json) e `app.py`.

### 3. Localizar a Subsessão "Executar"

No notebook Colab, vá até a subseção marcada como  `Executar`, dentro da seção `Streamlit`.

### 4. Gerar Token do Ngrok

- Acesse: https://dashboard.ngrok.com/authtokens
- Faça login ou crie uma conta
- Crie ou copie seu auth token e depois cole-o na parte indicada do código

Caso apareça a seguinte mensagem, está tudo certo: `Authtoken saved to configuration file: /root/.config/ngrok/ngrok.yml`

### 5. Configurar o Caminho

Localize a variável `diretorio_usado` e altere seu valor para o caminho onde estão os arquivos.

### 6. Rodar os Blocos

Execute todos os blocos de código da seção Executar, na ordem em que aparecem.

### 7. Acessar o Aplicativo

Ao final da execução, um link será gerado. Clique nele para abrir a aplicação no navegador e aproveitar!

Caso apareça algo pareceido com a imagem abaixo, apenas clique em `Visit Site`

![image](https://github.com/user-attachments/assets/631c83b1-3fb4-4f60-9d80-404d9af571dc)
