from django.core.management.base import BaseCommand
from search.models import Article, ArticleDocument

class Command(BaseCommand):
    help = 'Index all articles to Elasticsearch'

    def handle(self, *args, **kwargs):
        ArticleDocument.init()
        for article in Article.objects.all():
            doc = ArticleDocument(title=article.title, content=article.content)
            doc.save()
        self.stdout.write(self.style.SUCCESS('Successfully indexed all articles'))