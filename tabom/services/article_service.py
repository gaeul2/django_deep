from django.core.paginator import Page, Paginator
from django.db.models import QuerySet

from tabom.models import Article


def get_an_article(article_id: int) -> Article:  # 그냥 가져오는 함수임.
    return Article.objects.filter(id=article_id).get()


def get_article_list(offset: int, limit: int) -> QuerySet[Article]:  # Article을 갖고있는 쿼리셋을 return
    # 내림차순하면 "-"쓰면 됨/ id의 내림차순/ 장고에서는 쿼리셋 슬라이싱[]로, offset부터 offset+limit을 더한만큼
    return Article.objects.order_by("-id").prefetch_related("like_set")[offset : offset + limit]


# 페이지네이터 클래스 사용법
# def get_article_page(page: int, limit: int) -> Page:
#     return Paginator(Article.objects.order_by("-id"), limit).page(page)
