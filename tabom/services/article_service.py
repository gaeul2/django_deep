from tabom.models import Article


def get_an_article(article_id: int) -> Article:  # 그냥 가져오는 함수임.
    return Article.objects.filter(id=article_id).get()
