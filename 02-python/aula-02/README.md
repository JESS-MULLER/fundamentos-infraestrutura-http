# 📁 Aula 02: Manipulação e Persistência de Arquivos (TXT, CSV, JSON e Inputs)

Este laboratório foi dedicado à prática de persistência, estruturação e manipulação de dados em arquivos locais utilizando funções nativas, capturas dinâmicas do usuário e bibliotecas integradas do Python.

## 🚀 O que foi explorado:
* **Entrada e Saída de Dados:** Manipulação segura de arquivos utilizando o gerenciador de contexto `with open()`.
* **Arquivos TXT Básicos:** Escrita e leitura estruturada de strings em blocos de texto puro com tratamento de codificação (`utf-8`).
* **Arquivos CSV:** Uso da biblioteca integrada `import csv` para ler e processar dados estruturados no formato tabular (linhas e colunas).
* **Arquivos JSON:** Uso da biblioteca integrada `import json` para realizar a serialização e deserialização de dicionários usando `json.dump()` e `json.load()`.
* **Captura Dinâmica (`input()`) & Modo Append (`'a'`):** Criação de scripts interativos para receber dados do usuário via terminal e salvá-los de forma incremental no arquivo, adicionando novas linhas ao final do documento sem sobrescrever os registros anteriores.

---

## 🔍 Aprendizados Práticos & Resolução de Erros

* **Erros de Sintaxe no Modo Interativo:** Entendimento de que blocos que abrem escopo executados direto no terminal (`>>>`) exigem uma linha vazia (Enter duplo) para fechar o bloco antes de chamar outras funções.
* **Caminhos de Arquivos (Paths):** Compreensão de que declarar apenas o nome do arquivo faz o Python criá-lo na raiz global. Para salvar de forma organizada dentro do projeto, deve-se explicitar a árvore de diretórios.

---

## 📸 Evidências Práticas de Execução

### 1. Manipulação de Arquivos de Texto (.txt)
![Leitura de arquivo TXT corrigido com UTF-8](print-txt.png)

### 2. Manipulação de Arquivos Tabulares (.csv)
![Leitura e desempacotamento de arquivo CSV](print-csv.png)

### 3. Manipulação de Estruturas de Dados (.json)
![Escrita e leitura de arquivo JSON com sucesso](print-json.png)

### 4. Captura com Input e Escrita em Modo Append
![Código de captura de inputs rodando com sucesso no terminal](print-input-data .png)

### 5. Arquivo Gerado Incrementalmente
![Estrutura do arquivo de texto populado via inputs](print-input-data_txt.png)

### 6. Leitura de Dados Dinâmicos
![Leitura de dados do arquivo txt pelo terminal](print-read_data.png)
