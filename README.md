# Co. Meet

스코클 내배단5기 커뮤니티

# Start Routine

가상환경 재구성

py -m venv venv

source venv/scripts/activate

종속패키지 설치

pip install -r requirements.txt

시크릿키 발급

py -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

https://djecrety.ir/

.env파일 생성 후 시크릿키 적용

SECRET_KEY = '해당키'

db.sqlite3에 migrate

py manage.py migrate

이슈체크

py manage.py check

관리자 계정생성 및 서버테스트

py manage.py createsuperuser

py manage.py runserver


user app
유저에 대한 기능을 담은 app

commit
게시글에 대한 기능 담당하는 app
(git에서 commit하는것 처럼 게시물을 commit한다는 의미로 지음)


Co.Meet
협력하다의 coperate와 만나다의 meet을 합쳐 commit과 발음을 비슷하게 만든 합성어
