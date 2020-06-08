### 메모
1. 프로젝트 설정 -> URL설정 -> 포트 변경
# [서버기동]
2. python manage.py runserver 0.0.0.0:8000 //구름은 이렇게해줘야함
# [구름 IDE에서 브랜치처리]
3_1. 새 브런치(local_branch) 생성
3_2. 내용 수정 후 병합하기.
3_3. 병합 후 git에 branch생성 되고 PR생김.
3_4. merge 처리



### CMD 정리

# 프로젝트 생성
django-admin startproject [프로젝트명]

# 앱 생성
Python3 manage.py startapp [앱이름]

# 모델 작성 후 테이블 생성
python3 manage.py makemigrations

# *서버 실행 
python manage.py runserver 0.0.0.0:8000