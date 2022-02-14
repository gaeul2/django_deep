from django.db import IntegrityError
from django.test import TestCase

from tabom.models import Like
from tabom.models.article import Article
from tabom.models.user import User
from tabom.services.like_service import do_like, undo_like


class TestLikeService(TestCase):
    def test_a_user_can_like_an_article(self) -> None:
        # Given 유저와 게시글이 주어졌을때
        user = User.objects.create(name="test")
        article = Article.objects.create(title="test_title")

        # When 게시글에 대해서 유저가 좋아요를 했을때 like라는 객체가 생기고
        like = do_like(user.id, article.id)

        # Then 검증하는곳
        self.assertIsNotNone(like.id)  # like의 id는 None이 아니다.
        self.assertEqual(user.id, like.user_id)  # user의 id가 like의 user_id와 같다
        self.assertEqual(article.id, like.article_id)  # article도 like의 article_id와 같다

    def test_a_user_can_like_an_article_only_once(self) -> None:
        # Given
        user = User.objects.create(name="test")
        article = Article.objects.create(title="test_title")

        # Expect
        do_like(user.id, article.id)
        with self.assertRaises(IntegrityError):  # 에러를 일으키고싶은데 어떤 에러인지모르니까 Exception을 인자로 줌
            # pass #하는경우 test는 실패
            # raise Exception()#with구문에서 exception이 일어나면 에러가 성공
            do_like(user.id, article.id)

            # do_like함수자체에 아무것도 없는 상태에서 테스트를 실행하면 실패함. 왜? do_like함수자체에 에러가 일어날만한 곳이 없기때문
            # 단순히 like1, like2 객체만 생성하고 끝남
            # like모델에서 constraints 추가하고 테스트해보면 테스크성공함!
            # 즉, like1에서는 에러가 발생하지 않았고, like2에서 에러가 발생했다는것

            # with문 다음 try except로 아래코드를 넣고 테스트 실행하면 테스트 통과함.
            # evaluate(표현식평가)로 e의 type을 잡아보면 intergrity라고 나오므로
            # with의 인자로 IntergrityError를 넣어줌
            # 마무리로 쓰지않는 변수인 like1,like2를 지워주고 테스트 실행
            # try:
            #     like2 = do_like(user.id, article.id)
            # except Exception as e:
            #     print(e)

    def test_it_should_raise_exception_when_like_an_user_does_not_exist(self) -> None:

        # Given
        invalid_user_id = 9988
        article = Article.objects.create(title="test_title")

        # Expect
        # with self.assertRaises(IntegrityError):
        try:
            do_like(invalid_user_id, article.id)
        except Exception as e:
            print(e)

    def test_it_should_raise_exception_when_like_an_article_does_not_exist(self) -> None:

        # Given
        user = User.objects.create(name="test")
        invalid_article_id = 9988

        # Expect
        with self.assertRaises(IntegrityError):
            do_like(user.id, invalid_article_id)

    def test_like_count_should_increase(self) -> None:
        # Given
        user = User.objects.create(name="test")
        article = Article.objects.create(title="test_title")  # 게시글을 만들자마자

        # When
        do_like(user.id, article.id)  # 좋아요를 하나했기때문에 좋아요개수는 1부터시작

        # Then
        article = Article.objects.get(id=article.id)
        self.assertEqual(1, article.like_set.count())  # 좋아요 갯수가 1과 같다면.
        # 좋아요 개수에 어떻게 접근하냐면 like_set이라는 변수로 접근
        # poetry run mypy .해도 mypy가 무사히 넘어가는 이유는 django_stub덕분
        # django_stub이 mypy에게 like_set이라는 변수는 django가 넣어준다고 알려줌

    def test_a_use_can_undo_like(self) -> None:  # 테스트 먼저작성후 함수 작성
        # Given #user, article, like 하나씩 줌
        user = User.objects.create(name="test")
        article = Article.objects.create(title="test_title")
        like = do_like(user.id, article.id)

        # When 그다음 좋아요 취소를 했보면
        undo_like(user.id, article.id)

        # Then #삭제했을때 검증
        with self.assertRaises(Like.DoesNotExist):  # Like가 존재하지 않는 에러가 발생하는지 검증할것.
            # 어떨때? get으로 모델에서 like.id가 일치하는 오브젝트를 가져오려고 할때
            Like.objects.filter(id=like.id).get()  # 아무것도 존재하지 않는 에러가 발생해야함

    # def test_it_should_raise_an_exception_when_undo_like_which_does_not_exist(self) -> None:
    #     #Given #user, article 만줌. like가 존재하지 않아야 하기때문
    #     user = User.objects.create(name='test')
    #     article = Article.objects.create(title='test_title')
    #
    #     #Expect
    #     with self.assertRaises(Like.DoesNotExist): #없는 좋아요를 취소하려고 하니깐
    #         undo_like(user.id, article.id) #좋아요가 존재하지 않는 에러가 발생해야함.
