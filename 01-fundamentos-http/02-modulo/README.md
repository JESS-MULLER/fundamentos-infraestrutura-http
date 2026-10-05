# 🔒 Módulo 02: Detalhes, Evolução e Segurança HTTP

Este laboratório contém o detalhamento técnico e as análises práticas sobre o funcionamento avançado do protocolo HTTP, análise de cabeçalhos, evolução das versões (HTTP/1.1, 2 e 3) e os pilares de segurança na web.

---

## 📊 1. Status Codes (Códigos de Status HTTP)

Os códigos de status indicam se uma requisição HTTP foi concluída com sucesso ou se houve algum erro. Eles são divididos em 5 categorias oficiais:

*   **1xx (Informativo):** A requisição foi recebida e o processo continua.
*   **2xx (Sucesso):** A ação foi recebida, compreendida e aceita com sucesso.
    *   *Exemplo:* `200 OK` (Requisição bem-sucedida).
*   **3xx (Redirecionamento):** Mais ações precisam ser tomadas para completar a requisição.
    *   *Exemplo:* `301 Moved Permanently` (A URL mudou de lugar em definitivo).
*   **4xx (Erro do Cliente):** A requisição contém sintaxe incorreta ou não pode ser processada pelo cliente.
    *   *Exemplo:* `404 Not Found` (O recurso/página não foi encontrado).
*   **5xx (Erro do Servidor):** O servidor falhou ao tentar processar uma requisição que era válida.
    *   *Exemplo:* `500 Internal Server Error` (Ocorreu um erro genérico no servidor).

---

## 🔍 2. Anatomia de uma Requisição HTTP

Uma requisição HTTP é dividida estruturalmente em partes claras. No topo, temos a **Linha da Requisição**, seguida pelos **Cabeçalhos** e, por fim, o **Corpo** (separados por uma linha em branco).

### Elementos da Linha Inicial:
*   **Método (Verbo):** Define a ação (ex: `POST`, `GET`).
*   **URI / Path:** O endereço do recurso solicitado (ex: `/api/usuarios`).
*   **Protocolo:** A versão do HTTP sendo utilizada (ex: `HTTP/1.1`).

### Simulação de Requisição POST estruturada:
```http
POST /api/login HTTP/1.1
Host: localhost:3000
Content-Type: application/json
Authorization: Bearer xyz123_token_aqui
Content-Length: 43

{
  "usuario": "jess",
  "senha": "123"
}
```
> *Nota: Os cabeçalhos controlam os metadados (como o tamanho com `Content-Length` e o formato com `Content-Type`), enquanto o Corpo (Body) carrega os dados reais enviados após a linha em branco.*

---

## 🛠️ 3. Análise de Cabeçalhos (Headers) no DevTools/Postman

Ao inspecionar a aba **Network** do DevTools ou usar o Postman, identificamos cabeçalhos fundamentais que definem a localidade e o tipo de resposta:

*   **User-Agent:** Identifica o cliente (qual navegador, sistema operacional e versão estão fazendo a requisição).
*   **Accept:** Informa ao servidor quais formatos de dados o cliente consegue entender (ex: `text/html`, `application/json`).
*   **Accept-Language:** Define o idioma de preferência do usuário (ex: `pt-BR,pt;q=0.9`), permitindo que o servidor entregue a página traduzida localmente.

---

## ⚡ 4. Evolução do Protocolo: HTTP/1.1 vs HTTP/2 vs HTTP/3

| Recurso / Versão | HTTP/1.1 | HTTP/2 | HTTP/3 |
| :--- | :--- | :--- | :--- |
| **Protocolo de Transporte** | TCP | TCP | **UDP (via QUIC)** |
| **Conexões** | Uma por recurso (bloqueio Head-of-Line) | Uma conexão multiplexada | Uma conexão multiplexada real |
| **Vantagem Principal** | Simplicidade e maturidade | Compressão de headers e multiplexação | **Sem travamento de rede e muito mais veloz** |

### Vantagens do HTTP/3:
O HTTP/3 abandona o tradicional TCP e adota o protocolo **QUIC** (baseado em UDP). Ele traz a **multiplexação real**, o que significa que se um pacote de dados cair ou atrasar em uma rede oscilante (como o 4G/5G do celular), o restante da página continua carregando normalmente, sem travar o navegador inteiro.

---

## 🔒 5. Segurança na Web: HTTP vs HTTPS

*   **HTTP (Inseguro):** Os dados trafegam em texto puro pela rede. Qualquer pessoa conectada no mesmo Wi-Fi pode interceptar e ler suas senhas ou cartões.
*   **HTTPS (Seguro):** Adiciona uma camada de segurança chamada **TLS (Transport Layer Security)**. Todos os dados são criptografados antes de sair do seu computador.

### Certificados Digitais:
Funcionam como uma carteira de identidade da sua página web, emitida por autoridades confiáveis. Eles garantem a criptografia das requisições e provam para o navegador que o site visitado é real e não uma cópia falsa.

### Riscos Comuns na Web Sem Segurança:
*   **Man-in-the-middle (MitM):** Um invasor intercepta a comunicação entre você e o servidor para roubar dados.
*   **Phishing:** Páginas clonadas projetadas para enganar o usuário e capturar dados confidenciais.
*   **Injection (Injeção):** Envio de códigos maliciosos inseridos em formulários que tentam burlar a segurança do servidor.

---

## 🍪 6. Cookies vs Sessões no Navegador

Para resolver o fato de o HTTP não guardar o estado das coisas entre as páginas, navegadores utilizam duas ferramentas de armazenamento:

*   **Cookies:** Dados salvos diretamente no computador do usuário (ex: preferências de tema escuro/claro, rastreamento de marketing, itens que ficaram salvos no carrinho de compras).
*   **Sessões (Session/Token):** Dados de validação temporários guardados no servidor (ex: identificação de que você já fez o login e está autorizado a acessar o painel administrativo da Alura).
