from django.shortcuts import render, redirect
# login_required : 로그인이 되어있어야만 실행되게 하는 함수
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def log_in_view(request):
    """
    로그인! 김태연
    """


def sign_up_view(requset):
    """
    회원가입!김태연
    """


@login_required
def log_out_view(requset):
    """
    로그아웃. 남는 사람이 하는걸로 !
    """


@login_required
def my_page_view(request):
    """
    마이페이지, 내 프로필 수정, (비밀번호 초기화)
    엘리사님
    """
    if request.method == 'GET':
        return render(request, 'user/mypage.html')

    elif request.method == 'POST':
        username = request.POST.get('username', None)
        email = request.POST.get('email', None)

        # 기존 유저정보 수정하는 방법
        updated_user.username = username
        updated_user.email = email
        updated_user.save()
        messages.success(request, '프로필이 수정되었습니다.')

        return render(request, 'mypage.html', {'user': user})
