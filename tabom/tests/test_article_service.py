from django.test import TestCase

from tabom.models.article import Article
from tabom.services.article_service import get_an_article


class TestArticleService(TestCase):
    def test_you_can_get_an_article_by_id(self) -> None:  # id로 article을 조회할 수 있다.
        # Given #title과 게시글하나 만듬
        title = "test_title"
        article = Article.objects.create(title=title)

        # When get_an_article로 article.id를 통해 조회한 게시글을 result_article에 저장
        result_article = get_an_article(article.id)

        # Then
        self.assertEqual(article.id, result_article.id)  # article.id와 조회한 글의 id가 같은지
        self.assertEqual(title, result_article.title)  # title 과 조회한글의 title이 같은지 검증

    def test_it_should_raise_exception_when_article_does_not_exist(self) -> None:  # 게시글이 존재하지 않을때 테스트
        # Given #없는 article_id를 줌
        invalid_article_id = 9988

        # Expect #article이 존재하지 않는 에러가 발생해야함.
        with self.assertRaises(Article.DoesNotExist):
            get_an_article(invalid_article_id)  # 없는 article번호로 조회를 했을때
