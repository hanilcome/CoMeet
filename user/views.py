from django.shortcuts import render, redirect
# login_required : 로그인이 되어있어야만 실행되게 하는 함수
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from django.contrib.auth import get_user_model
from .models import User


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

        if password != password2:
            messages.warning(request, '기억력 딸림?')  # 비밀번호 불일치시 회원가입 화면 다시 보여주기
            return render(request, 'user/signup.html')
        else:
            exist_user = get_user_model().objects.filter(username=username)
            if exist_user:
                messages.warning(request, 'Doppelgänger!!')
                return render(request, 'user/signup.html')
            else:
                User.objects.create_user(
                    username=username, password=password, email=email)
                return redirect('user:log_in')


@login_required
def log_out_view(request):
    auth.logout(request)
    return redirect('/')


@login_required
def my_page_view(request, id):
    """
    마이페이지, 내 프로필 수정, (비밀번호 초기화)
    엘리사님
    """
    updated_user = User.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'user/mypage.html', {'user': updated_user})

    elif request.method == 'POST':
        username = request.POST.get('username', None)
        email = request.POST.get('email', None)

        # 기존 유저정보 수정하는 방법
        updated_user.username = username
        updated_user.email = email
        updated_user.save()
        messages.success(request, '프로필이 수정되었습니다.')

        return render(request, 'mypage.html', {'user': updated_user})
