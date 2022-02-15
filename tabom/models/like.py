from django.db import models

from tabom.models.article import Article
from tabom.models.base_model import BaseModel
from tabom.models.user import User


class Like(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE) #장고에서의 cascade옵션을 적용하는것.
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # updated_at = models.DateTimeField(auto_now=True)
    # created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["user", "article"], name="unique_user_article")]  # 만들었다면 migrate
