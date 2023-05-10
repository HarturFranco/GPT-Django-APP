# chat/views.py

from django.shortcuts import render
from django.http import JsonResponse
import openai
import json

openai.api_key = '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'

def home(request):
    return render(request, 'chat/home.html')

def get_chat_response(request):
    if request.method == 'POST':
        model="gpt-3.5-turbo"
        prompt =  json.loads(request.POST.get('messages'))
        print(prompt)
        messages = prompt
        # chama a api
        response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=1, # Grau de Aleatoriedade
        )

        chat_response = response.choices[0].message["content"]

        # resposta em json JSON
        return JsonResponse({'chat_response': chat_response})
    else:
        return JsonResponse({'error': 'Invalid request method.'})
