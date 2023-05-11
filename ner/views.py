# ner/views.py

from django.shortcuts import render
from django.http import JsonResponse
import openai
import json

# Set up OpenAI credentials
openai.api_key = 'API-KEY'

def home(request):
    return render(request, 'ner/index.html')

def get_ner_response(request):
    if request.method == 'POST':
        model="gpt-3.5-turbo"
        user_msg = request.POST.get('messages')
        
        prompt = f"""
        Você é um sistema de Reconhecimento de Entidades Nomeadas (NER) altamente inteligente e preciso.
        Você recebe um texto como entrada e sua tarefa é reconhecer 
        tipos específicos de entidades nomeadas nesse texto fornecido e classificá-las em um conjunto
        de tipos de entidades predefinidos a seguir: ```Organizacao, Pessoa, Tempo, Valor, Local```

        Descrição do formato de saída:
        ```O texto de entrada completo com as entidades reconhecidas 
        delimitadas por 《》 e o tipo da entidade reconhecida delimitado por [] após a delimitação 
        da entidade. A saída não deve ter nenhum texto adicional, apenas o que foi descrito.
        ```

        Exemplos de resposta: 
        1 - A 《Organização de Desenvolvimento Sustentável Global (ODSG)》[Organizacao]
        realizou sua conferência anual em 《15 de março de 2023》[Tempo], 
        na cidade de 《Nova York》[Local].   
        2 - A parceria visa arrecadar 《US$ 10 milhões》[Valor] 
        para investir em projetos de energia renovável em países em desenvolvimento.
        3 - O 《Dr. Mendes》[Pessoa] compartilhou histórias inspiradoras sobre o trabalho da "Verde Vida" 
        em comunidades rurais, fornecendo acesso à energia limpa e melhorando a qualidade de vida 
        das pessoas.
        4 - A 《Fundação Esperança》[Organizacao] busca angariar 《R$ 500.000,00》[Valor] por meio de doações online e eventos de 
        conscientização. Os recursos serão destinados à construção de escolas, fornecimento de materiais 
        educativos e capacitação de professores, visando criar oportunidades de aprendizado e 
        transformação para essas crianças.

        Texto de entrada: ```{user_msg}```
        """

        messages = [{"role": "user", "content": prompt}]
        # chama a api
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=0, # Grau de Aleatoriedade
            
        )

        ner_response = response.choices[0].message["content"]
        # print(chat_response)
        # resposta em json JSON
        return JsonResponse({'chat_response': ner_response})
    else:
        return JsonResponse({'error': 'Invalid request method.'})