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
