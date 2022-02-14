from django.db import models

from tabom.models.base_model import BaseModel


class User(BaseModel):
    name = models.CharField(max_length=50)
    # updated_at = models.DateTimeField(auto_now=True)
    # created_at = models.DateTimeField(auto_now_add=True)
