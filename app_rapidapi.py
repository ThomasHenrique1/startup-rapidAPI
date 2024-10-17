from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)


def test_api(query_text):
    url = "https://cheapest-gpt-4-turbo-gpt-4-vision-chatgpt-openai-ai-api.p.rapidapi.com/v1/chat/completions"
    
    payload = {
     "messages": [
        {
            "role": "user",
            "content": f"Me dê uma ideia inovadora para uma startup sobre {query_text}. Responda em português, utilizando negrito para títulos e seções e '##' para subtítulos. Limite a resposta a no máximo 150 palavras e use no máximo 100 tokens."
        }
    ],
    "model": "gpt-4o",  # Modelo da API disponibilizada pela RapidAPI
    "max_tokens": 150,  
    "temperature": 0.9
    }
    
    headers = {
        "x-rapidapi-key": "",# Adicione a KEY encontrada no Site da RapidAPI
        "x-rapidapi-host": "cheapest-gpt-4-turbo-gpt-4-vision-chatgpt-openai-ai-api.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.HTTPError as http_err:
        return {'error': f'Erro HTTP: {http_err}'}
    except requests.exceptions.RequestException as req_err:
        return {'error': f'Erro de requisição: {req_err}'}
    except Exception as err:
        return {'error': f'Erro inesperado: {err}'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-startup', methods=['POST'])
def generate_startup():
    user_input = request.json.get('input')

    api_response = test_api(user_input)
    
    if 'choices' in api_response and len(api_response['choices']) > 0:
        response_message = api_response['choices'][0]['message']['content'].strip()

        # Removendo símbolos desnecessários e ajustando formatação
        formatted_message = response_message.replace('#', '').strip()  # Ajustar se necessário

        return jsonify({"msg": f"## Ideia:\n{formatted_message}"})
    else:
        return jsonify(api_response)


if __name__ == '__main__':
    app.run(debug=True)
