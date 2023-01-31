##########################################################
#앱 사용방법
##########################################################
[초기 install]
pip3 install django-crontab
pip3 install 'Django<4.0'
pip3 install requests

[서버 실행]
python manage.py runserver

[접속]
http://127.0.0.1:8000/python_lotto_app/

[로또번호 갱신방법]
C:\lotto\python_lotto_app\views.py 에서 회차 수정

http://127.0.0.1:8000/python_lotto_app/insert

##########################################################


###참고 사이트

#템플릿 경로 설정
https://nachwon.github.io/django-8-template/

###계정

# Superadmin
ID : admin
PW : 1234

### 메모
1. 프로젝트 설정 -> URL설정 -> 포트 변경
# [서버기동]
2. python manage.py runserver

### CMD 정리

# 프로젝트 생성
django-admin startproject [프로젝트명]

# 앱 생성
Python3 manage.py startapp [앱이름]

# 모델 작성 후 테이블 생성
python3 manage.py makemigrations
python3 manage.py migrate


# *서버 실행 
python3 manage.py runserver 0.0.0.0:8000

# Superadmin생성 [Domain/admin 페이지]
python3 manage.py createsuperuser

# Mysql 실행
service mysql start
mysql -p 

----





