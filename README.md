## Startup Idea Generator - RapidAPI
Este projeto é uma aplicação web simples que utiliza a RapidAPI para gerar ideias inovadoras de startups com base em um tema fornecido pelo usuário. Ele faz chamadas à API do ChatGPT através da RapidAPI para gerar essas ideias, formatando os resultados com negrito e subtítulos para melhor organização.

## Funcionalidades

- Gera ideias de startups com base em temas fornecidos pelo usuário.
- Utiliza a API do ChatGPT via RapidAPI para gerar respostas.
- Exibe o resultado formatado com negrito para títulos e subtítulos.
- Backend em Flask.
- Frontend simples com HTML, CSS e JavaScript.

## Estrutura do Projeto
```bash 
├── app_rapidapi.py         # Arquivo principal utilizando a API da RapidAPI
├── static/                 # Pasta para arquivos estáticos (CSS e JS)
│   ├── style/
│   │   └── style.css       # Arquivo CSS personalizado
│   └── js/
│       └── index.js        # Código JavaScript para requisições AJAX
├── templates/
│   └── index.html          # Template HTML principal
├── README.md               # Documentação do projeto
├── requirements.txt        # Lista de dependências do projeto

```
## Requisitos

- Python 3.x
- Flask
- Requests
- Conta no RapidAPI (para usar a API ChatGPT via RapidAPI)

## Instalação


> Instale as dependências:

```bash
pip install -r requirements.txt
```
> Crie um arquivo .env (opcional para manter sua chave da API segura) ou defina diretamente no código sua chave da API.

- No caso da OpenAI, insira sua chave no código onde estiver escrito `YOUR_OPENAI_API_KEY`.

- No caso da RapidAPI, insira a chave no código onde estiver `YOUR_RAPIDAPI_KEY`.

## Estrutura dos Arquivos

### `app_rapidapi.py`
- Arquivo principal que contém a lógica para a geração de ideias de startups utilizando a API do ChatGPT via RapidAPI. A função test_rapidapi realiza a chamada para a API e retorna a resposta formatada.
### `index.html`
- Interface simples onde o usuário pode inserir um tema de startup e receber a ideia gerada pela API.
### `index.js`
- Código JavaScript que lida com as requisições AJAX, enviando o tema para o backend e recebendo a resposta da API.
### `style.css`
- Arquivo de estilos CSS que define o layout e o design da página.

## Considerações

- O uso da API via `RapidAPI` está sujeito a limites de requisição e possíveis custos, dependendo do seu plano de uso. Verifique a documentação da `RapidAPI` para entender os limites e custos
- Você pode ajustar o número de tokens e o nível de criatividade (`temperature`) nas requisições conforme suas necessidades, direto no arquivo `app_rapidapi.py`.
    + Para a RapidAPI sera deixado dois links de API's gratuitas para caso tenha interesse em testar, o nome do arquivo contendo so links se chama `sites.txt`, é necessario ter conta na RapidAPI.

## Contato

Se você tiver dúvidas ou sugestões, entre em contato com [Thomas Henrique](mailto:thomasnhenrique@gmail.com).
