# 📁 Aula 02: Manipulação de Arquivos (TXT, CSV e JSON)

Este laboratório foi dedicado à prática de persistência e estruturação de dados em arquivos locais utilizando as funções nativas e as bibliotecas integradas do Python.

## 🚀 O que foi explorado:
* **Arquivos TXT:** Leitura e escrita de strings em blocos utilizando o gerenciador de contexto `with open()`.
* **Arquivos CSV:** Uso da biblioteca integrada `import csv` para ler e desempacotar dados estruturados no formato tabular (linhas e colunas).
* **Arquivos JSON:** Uso da biblioteca integrada `import json` para praticar a serialização (`json.dump()`) e deserialização (`json.load()`) de dicionários complexos, simulando o tráfego de dados estruturados.

---

## 🔍 Aprendizados Práticos & Resolução de Erros

* **SyntaxError no Modo Interativo:** Entendimento prático de que blocos `with` e laços `for` executados diretamente no terminal interativo (`>>>`) exigem uma linha em branco (Enter duplo) para fechar o escopo antes da execução do comando `print()`.
* **Encoding (Codificação de Caracteres):** Análise do impacto do tratamento de acentuações, corrigido na leitura dinâmica do Python através da atribuição estrita do parâmetro `encoding='utf-8'`.
* **NameError (Variáveis Não Definidas):** Fixação de que chaves e objetos dinâmicos (como o parâmetro `dados` na escrita do JSON) precisam ser instanciados previamente na memória do terminal antes da chamada de gravação no arquivo.

---

## 📸 Evidências Práticas de Execução

### 1. Manipulação de Arquivos de Texto (.txt)
![Leitura de arquivo TXT corrigido com UTF-8](print-txt.png)

### 2. Manipulação de Arquivos Tabulares (.csv)
![Leitura e desempacotamento de arquivo CSV](print-csv.png)

### 3. Manipulação de Estruturas de Dados (.json)
![Escrita e leitura de objeto JSON com sucesso](print-json.png)
