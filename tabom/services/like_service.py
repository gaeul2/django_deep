from tabom.models.like import Like


def do_like(user_id: int, article_id: int) -> Like:  # return타입이 Like라고 명시해준것.
    return Like.objects.create(user_id=user_id, article_id=article_id)  # 바로 생성하도록 코드를짬


def undo_like(user_id: int, article_id: int) -> None:  # 삭제하는 함수는 무언가를 리턴할 필요 없음
    # 먼저 좋아요정보를 가져옴. (user_id와 글id가 일치하는) unique_con어쩌고 사용하니까
    # 좋아요는 한개이거나 존재하지 않음. 2개이상일 수 없음. 따라서 get사용
    # like = Like.objects.filter(user_id=user_id, article_id=article_id).get()
    # like.delete() #가져온 like를 delete()해주면 끝...개쉽네 그냥 delete()기본 제공되나봐
    #
    # -------------------위는 모델에서 불러와서 삭제하는 방법----------------------

    # -------아래는 그냥 qeuryset에서 바로 삭제하는 방법----------------------------
    Like.objects.filter(user_id=user_id, article_id=article_id).delete()
    # 이방법 사용시 test에서
    # test_it_should_raise_an_exception_when_undo_like_which_does_not_exist는 필요없음
