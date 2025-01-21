from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PromptSerializer
import openai
from django.conf import settings
from elasticsearch import Elasticsearch
import logging

logger = logging.getLogger(__name__)

es = Elasticsearch("http://localhost:9200")

# Configura la clave de API
openai.api_key = settings.OPENAI_API_KEY

def recognize_keyword(prompt):
    """
    Extrae la palabra clave más importante del texto dado.
    """
    response = openai.chat.completions.create(
        model="gpt-4",
        store=True,
        messages=[{"role": "user", "content": f"Extrae la palabra clave más importante del siguiente texto: {prompt}"}],
        max_tokens=100
    )
    return response.choices[0].message.content.strip()

class SearchView(APIView):
    def get(self, request):
        # Validar los datos de entrada con el serializador
        serializer = PromptSerializer(data=request.query_params)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Obtener el prompt validado
        prompt = serializer.validated_data['prompt']

        # Realizar la búsqueda en Elasticsearch
        try:
            # Construir la consulta de Elasticsearch
            query = {
                "query": {
                    "match": {
                        "content": prompt
                    }
                }
            }

            # Realizar la búsqueda en Elasticsearch
            response = es.search(index="articles", body=query)

            # Verificar si se encontraron resultados
            if response['hits']['total']['value'] > 0:
                return Response(response['hits']['hits'], status=status.HTTP_200_OK)
            else:
                return Response({"message": "No se encontraron resultados"}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
def search_page(request):
    return render(request, 'search.html')
