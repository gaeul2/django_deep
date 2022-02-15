import articles as articles
from django.test import TestCase

from tabom.models.article import Article
from tabom.services.article_service import get_an_article, get_article_list, get_article_page
from tabom.models import User, Like
from tabom.services.like_service import do_like


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

    def test_get_article_list_should_prefetch_like(self) -> None:
        #Given
        user = User.objects.create(name='test_user')
        articles = [Article.objects.create(title=f'{i}') for i in range(1,21)]
        Like.objects.create(user_id=user.id, article_id=articles[-1].id) #[-1]로 가장 마지막에 생성된 게시물에 좋아요를 해보겠다.

        #When
        result_articles = get_article_list(0,10) #offset과 limit임

        #Then #len(result_articles) 대신 result_articles.count()써도 됨.
        self.assertEqual(len(result_articles), 10) #limit이 10이므로 길이도 10이어야함
        self.assertEqual(1, result_articles[0].like_set.count())#가장마지막에 생성된 게시물에 좋아요했으니까 지금은 0번째로 불러와야 제일 첫게시물임.
        self.assertEqual(
            [a.id for a in reversed(articles[10:21])], #reversed로 역순정렬하는 효과
            [a.id for a in result_articles], #게시물을 역순정렬해서 20~11번까지의 id가 result_articles의 id 와 같은지확인
        )

#페이지네이터 사용법
    # def test_get_article_page_should_prefetch_like(self) -> None:
    #     #Given
    #     user = User.objects.create(name='test_user')
    #     articles = [Article.objects.create(title=f'{i}') for i in range(1,21)]
    #     Like.objects.create(user_id=user.id, article_id=articles[-1].id) #[-1]로 가장 마지막에 생성된 게시물에 좋아요를 해보겠다.
    #
    #     #When
    #     result_articles = get_article_page(1,10) #offset과 limit임
    #
    #     #Then #len(result_articles) 대신 result_articles.count()써도 됨.
    #     self.assertEqual(len(result_articles), 10) #limit이 10이므로 길이도 10이어야함
    #     self.assertEqual(1, result_articles[0].like_set.count())#가장마지막에 생성된 게시물에 좋아요했으니까 지금은 0번째로 불러와야 제일 첫게시물임.
    #     self.assertEqual(
    #         [a.id for a in reversed(articles[10:21])], #reversed로 역순정렬하는 효과
    #         [a.id for a in result_articles], #게시물을 역순정렬해서 20~11번까지의 id가 result_articles의 id 와 같은지확인
    #     )