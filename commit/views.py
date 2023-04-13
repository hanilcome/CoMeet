from django.shortcuts import render, redirect
from .models import Commit
# Create your views here.

# 홈 들어갔을 때 뉴스피드로 main.html 띄워주기.
def home(request):
    if request.method == 'GET':
        all_commit = Commit.objects.all().order_by('-created_at')
        return render(request, 'commit/main.html', {'commit':all_commit})



def detail(request):
    """
    상세 게시글. 발전 시키게 된다면 댓글 기능까지! -윤보영-
    detail/1 detail/2
    """


def write_view(request):
    # 화면 띄워주기
    if request.method == 'GET':
        return render(request, 'commit/write_view.html')
    
    # 데이터베이스에 값 저장
    if request.method == 'POST':
        user = request.user
        my_commit = Commit()
        my_commit.writer = user
        my_commit.title = request.POST.get('my-title','')
        my_commit.content = request.POST.get('my-content','')
        my_commit.save()
        return redirect('/')

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
