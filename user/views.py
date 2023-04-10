from django.shortcuts import render, redirect
# login_required : 로그인이 되어있어야만 실행되게 하는 함수
from django.contrib.auth.decorators import login_required


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
