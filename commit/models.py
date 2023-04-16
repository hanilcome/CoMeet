from django.db import models
from user.models import User
from django.conf import settings


# Create your models here.
class Commit(models.Model):
    class Meta:
        db_table = "my_commit"

    category = models.CharField(max_length=256, default='')  # 카테고리
    title = models.CharField(max_length=256, default='')  # 타이틀
    writer = models.ForeignKey(User, on_delete=models.CASCADE)  # 작성자
    content = models.CharField(max_length=256)  # 글내용
    like_commit = models.PositiveIntegerField(default=0)  # 좋아요
    created_at = models.DateTimeField(auto_now_add=True)  # 작성일
    updated_at = models.DateTimeField(auto_now=True)  # 수정일


class Comment(models.Model):
    class Meta:
        db_table = "comment"

    commit = models.ForeignKey(Commit, on_delete=models.CASCADE)  # 해당글
    writer = models.ForeignKey(User, on_delete=models.CASCADE)  # 댓글작성자
    comment = models.CharField(max_length=256)  # 댓글
    created_at = models.DateTimeField(auto_now_add=True)  # 댓글작성일
    updated_at = models.DateTimeField(auto_now=True)  # 수정일
