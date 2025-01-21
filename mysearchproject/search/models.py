from django.db import models
from elasticsearch_dsl import Document, Text
from elasticsearch_dsl.connections import connections

connections.create_connection(hosts=['http://localhost:9200'])


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

class ArticleDocument(Document):
    title = Text()
    content = Text()

    class Index:
        name = 'articles'

    def save(self, **kwargs):
        return super().save(**kwargs)