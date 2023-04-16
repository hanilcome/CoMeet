from django.shortcuts import render, redirect
# login_required : 로그인이 되어있어야만 실행되게 하는 함수
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from django.contrib.auth import get_user_model
from .models import User
from commit.models import Commit


# 로그인

def log_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        me = auth.authenticate(request, username=username, password=password)
        if me is not None:
            auth.login(request, me)
            return redirect('commit:home')    # 메인페이지로 가는
        else:
            messages.warning(request, '당신 누구야!!')
            return redirect('user:log_in')

    elif request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/login.html')


# 회원가입
def sign_up_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)
        email = request.POST.get('email', None)
        bio = request.POST.get('bio', None)

        if password != password2:
            # 비밀번호 불일치시 회원가입 화면 다시 보여주기
            messages.warning(request, '비밀번호가 틀렸어요..')
            return render(request, 'user/signup.html')
        else:
            exist_user = get_user_model().objects.filter(username=username)
            if exist_user:
                messages.warning(request, 'Doppelgänger!!')
                return render(request, 'user/signup.html')
            else:
                User.objects.create_user(
                    username=username, password=password, email=email, bio=bio)
                return redirect('user:log_in')

# 로그아웃


@login_required
def log_out_view(request):
    auth.logout(request)
    return redirect('/')

# 내 프로필보기


@login_required
def my_page_view(request, id):
    updated_user = User.objects.get(id=id)
    my_commit = Commit.objects.filter(writer=request.user)
    print(my_commit)
    if request.method == 'GET':
        return render(request, 'user/mypage.html', {'user': updated_user, 'commit': my_commit})

    elif request.method == 'POST':
        username = request.POST.get('username', None)
        email = request.POST.get('email', None)
        bio = request.POST.get('bio', None)

        # 기존 유저정보 수정하는 방법
        exist_user = get_user_model().objects.filter(username=username)
        if exist_user:
            messages.warning(request, '이미 존재하는 유저 이름입니다.')
            return render(request, 'user/mypage.html', {'user': updated_user, 'commit': my_commit})
        else:
            updated_user.username = username
            updated_user.email = email
            updated_user.bio = bio
            updated_user.save()
            messages.success(request, '프로필이 수정되었습니다.')

            return render(request, 'user/mypage.html', {'user': updated_user, 'commit': my_commit})

# 다른사람 프로필보기


def user_my_view(request, id):
    my_user = User.objects.get(id=id)
    my_commit = Commit.objects.filter(writer=my_user)
    if request.method == 'GET':
        return render(request, 'user/userview.html', {'user': my_user, 'commit': my_commit})
