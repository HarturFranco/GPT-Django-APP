# sent/views.py

from django.shortcuts import render
from django.http import JsonResponse
import openai
import json

# Set up OpenAI credentials
openai.api_key = 'API-KEY'

def home(request):
    return render(request, 'sent/index.html')

def get_sent_response(request):
    if request.method == 'POST':
        model="gpt-3.5-turbo"
        user_msg = request.POST.get('messages')
        
        prompt = f"""
        Você é um sistema de Analise de Sentimentos altamente inteligente e preciso.
        Você recebe um texto como entrada e sua tarefa é identificar sentimento do texto fornecido
        e classificá-las em um conjunto de tipos de sentimentos predefinidos a seguir: 
        ```Negativo, Neutro e Positivo```

        Descrição do formato de saída:
        ```Apenas um dos tipos de sentimentos predefinidos. Nenhum texto adicional como 'Sentimento:' ou 'O sentimento da frase é:' ou 'Saida:.
        ```

        Exemoplos do formato de saída:
        1 - ```Negativo.```
        2 - ```Neutro.```
        3 - ```Positivo.```
        
        Por favor, apenas uma palavra na saída.
        
        Texto de entrada: ```{user_msg}```
        """

        messages = [{"role": "user", "content": prompt}]
        # chama a api
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=0, # Grau de Aleatoriedade
            
        )

        sent_response = response.choices[0].message["content"]
        # print(chat_response)
        # resposta em json JSON
        return JsonResponse({'chat_response': sent_response})
    else:
        return JsonResponse({'error': 'Invalid request method.'})