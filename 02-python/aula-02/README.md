# 📁 Aula 02: Manipulação de Arquivos (TXT e CSV)

Este laboratório foi dedicado à prática de persistência de dados em arquivos de texto utilizando as funções nativas e bibliotecas integradas do Python.

## 🚀 O que foi explorado:
* **Entrada e Saída de Dados:** Manipulação de arquivos com o gerenciador de contexto `with open()`.
* **Arquivos TXT:** Leitura e escrita estruturada de strings em blocos.
* **Arquivos CSV:** Uso da biblioteca integrada `import csv` para ler e desempacotar dados estruturados no formato de tabelas (linhas e colunas).

---

## 🔍 Aprendizados Práticos & Resolução de Erros

* **SyntaxError no Modo Interativo:** Entendimento prático de que blocos `with` e laços `for` executados diretamente no terminal interativo (`>>>`) exigem uma linha em branco (Enter duplo) para fechar o escopo antes da execução do comando `print()`.
* **Encoding (Codificação de Caracteres):** Análise do impacto do tratamento de acentuações, corrigido na leitura dinâmica do Python através da atribuição estrita do parâmetro `encoding='utf-8'`.

---

## 📸 Evidências Práticas de Execução

### 1. Manipulação de Arquivos de Texto (.txt)
![Leitura de arquivo TXT corrigido com UTF-8](print-txt.png)

### 2. Manipulação de Arquivos Tabulares (.csv)
![Leitura e desempacotamento de arquivo CSV](print-csv.png)
