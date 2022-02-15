from django.db import connection
from django.test import TestCase
from django.test.utils import CaptureQueriesContext

from tabom.models import Article, Like, User


class TestCascade(TestCase):
    def test_capture_what_queries_excuted_when_cascade(self) -> None:
        #Given user,article, like를 하나씩 만들고
        user = User.objects.create(name="user1")
        article = Article.objects.create(title="artice1")
        like = Like.objects.create(user_id=user.id, article_id=article.id)
        with CaptureQueriesContext(connection) as ctx:
            article.delete()#article을 삭제했을때 어떻게 되는지
            print(ctx) #article을 지우기전 연결된 친구가 있느지 확인해서 like가 있으니 like를 먼저지우고, article을 지워줌. 장고가!
