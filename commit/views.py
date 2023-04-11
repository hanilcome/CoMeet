from django.shortcuts import render, redirect
from .models import Commit
# Create your views here.


def home(request):
    """
    기본메인페이지. 남는 사람이 하는걸로 !
    """


def detail(request):
    """
    상세 게시글. 발전 시키게 된다면 댓글 기능까지! -윤보영-
    detail/1 detail/2
    """


def write_view(request):
    """
    게시글 쓰기. 백지현
    """

# 게시글 수정함수


def edit_view(request, id):
    my_commit = Commit.objects.get(id=id)
    if request.method == 'POST':
        user = request.user
        my_commit = Commit()
        my_commit.writer = user
        my_commit.title = request.POST.get('title', '')
        my_commit.content = request.POST.get('content', '')
        my_commit.save()
        return render(request, 'commit/detail.html', {'commit': my_commit})
    elif request.method == 'GET':
        return render(request, 'commit/edit.html', {'commit': my_commit})


def delete_view(request):
    """
    게시글 삭제. 남는 사람이 하는걸로 !
    """
