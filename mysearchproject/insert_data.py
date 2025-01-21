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
        {"title": "Cuarto artículo", "content": "El cuarto artículo habla sobre tecnología y su impacto en la sociedad."},
        {"title": "Quinto artículo", "content": "En el quinto artículo se discuten las tendencias actuales en inteligencia artificial."},
        {"title": "Sexto artículo", "content": "El sexto artículo explora los avances en medicina moderna."},
        {"title": "Séptimo artículo", "content": "El séptimo artículo analiza el cambio climático y sus efectos."},
        {"title": "Octavo artículo", "content": "En el octavo artículo se habla de la importancia de la educación en línea."},
        {"title": "Noveno artículo", "content": "El noveno artículo trata sobre las startups y su impacto en la economía."},
        {"title": "Décimo artículo", "content": "El décimo artículo explora las tendencias en diseño gráfico."},
        {"title": "Undécimo artículo", "content": "En el undécimo artículo se discute el futuro de los vehículos autónomos."},
        {"title": "Duodécimo artículo", "content": "El duodécimo artículo habla sobre la importancia de la ciberseguridad."},
        {"title": "Decimotercer artículo", "content": "El decimotercer artículo explora las tendencias en redes sociales."},
        {"title": "Decimocuarto artículo", "content": "En el decimocuarto artículo se analiza el impacto de la globalización."},
        {"title": "Decimoquinto artículo", "content": "El decimoquinto artículo trata sobre la innovación en la industria alimentaria."},
        {"title": "Decimosexto artículo", "content": "El decimosexto artículo habla sobre los desafíos de la energía renovable."},
        {"title": "Decimoséptimo artículo", "content": "En el decimoséptimo artículo se discute el papel de la ética en la tecnología."},
        {"title": "Decimoctavo artículo", "content": "El decimoctavo artículo explora las tendencias en marketing digital."},
        {"title": "Decimonoveno artículo", "content": "El decimonoveno artículo trata sobre el futuro del trabajo remoto."},
        {"title": "Vigésimo artículo", "content": "En el vigésimo artículo se analiza el impacto de la realidad virtual."},
        {"title": "Vigésimo primer artículo", "content": "El vigésimo primer artículo habla sobre la importancia de la privacidad en línea."},
        {"title": "Vigésimo segundo artículo", "content": "El vigésimo segundo artículo explora las tendencias en fintech."},
        {"title": "Vigésimo tercer artículo", "content": "En el vigésimo tercer artículo se discute el futuro de la educación."},
        {"title": "Vigésimo cuarto artículo", "content": "El vigésimo cuarto artículo trata sobre los avances en biotecnología."},
        {"title": "Vigésimo quinto artículo", "content": "El vigésimo quinto artículo habla sobre la importancia de la sostenibilidad."},
        {"title": "Vigésimo sexto artículo", "content": "En el vigésimo sexto artículo se analiza el impacto de la inteligencia artificial en el arte."},
        {"title": "Vigésimo séptimo artículo", "content": "El vigésimo séptimo artículo explora las tendencias en comercio electrónico."},
        {"title": "Vigésimo octavo artículo", "content": "El vigésimo octavo artículo trata sobre los desafíos de la movilidad urbana."},
        {"title": "Vigésimo noveno artículo", "content": "En el vigésimo noveno artículo se discute el futuro de la robótica."},
        {"title": "Trigésimo artículo", "content": "El trigésimo artículo habla sobre la importancia de la innovación en la salud."},
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
