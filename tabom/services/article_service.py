from django.core.paginator import Page, Paginator
from django.db.models import Prefetch, QuerySet

from tabom.models import Article, Like


def get_an_article(article_id: int) -> Article:  # 그냥 가져오는 함수임.
    return Article.objects.filter(id=article_id).get()


def get_article_list(user_id: int, offset: int, limit: int) -> QuerySet[Article]:  # Article을 갖고있는 쿼리셋을 return
    # 내림차순하면 "-"쓰면 됨/ id의 내림차순/ 장고에서는 쿼리셋 슬라이싱[]로, offset부터 offset+limit을 더한만큼
    return (  # 괄호로 감싸면 여러줄로 쓰는게 가능
        Article.objects.order_by("-id")
        .prefetch_related("like_set")
        .prefetch_related(Prefetch("like_set", queryset=Like.objects.filter(user_id=user_id), to_attr="my_likes"))[
            offset : offset + limit
        ]
    )


# 페이지네이터 클래스 사용법
# def get_article_page(page: int, limit: int) -> Page:
#     return Paginator(Article.objects.order_by("-id"), limit).page(page)
