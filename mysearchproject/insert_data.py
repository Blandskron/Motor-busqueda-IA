import os
import django
from elasticsearch_dsl.connections import connections


# Configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysearchproject.settings')
django.setup()

from search.models import Article, ArticleDocument

# Establecer conexión con Elasticsearch
connections.create_connection(hosts=['http://localhost:9200'])

# Función para insertar artículos en la base de datos y Elasticsearch
def insert_articles():
    # Lista de artículos para insertar
    articles = [
        {"title": "Primer artículo", "content": "Este es el contenido del primer artículo."},
        {"title": "Segundo artículo", "content": "Contenido del segundo artículo con información interesante."},
        {"title": "Tercer artículo", "content": "Aquí tenemos un contenido más detallado para el tercer artículo."},
    ]

    for article_data in articles:
        # Crear y guardar el artículo en la base de datos
        article = Article.objects.create(
            title=article_data['title'],
            content=article_data['content']
        )
        print(f"Artículo creado: {article}")

        # Indexar el artículo en Elasticsearch
        article_doc = ArticleDocument(
            meta={'id': article.id},
            title=article.title,
            content=article.content
        )
        article_doc.save()
        print(f"Artículo indexado en Elasticsearch: {article.title}")

if __name__ == "__main__":
    insert_articles()
