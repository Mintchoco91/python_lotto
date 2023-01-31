# python_lotto

과거 회차별 로또 번호 통계확인

[Spec]
   - DEV language : Python
   - django-admin : 3.2.16
   - Storage : sqllite3
   - Repository : https://github.com/Mintchoco91/python_lotto
   
   ![image](https://user-images.githubusercontent.com/48236887/215729771-5b6bceca-89ab-4a54-8364-cbd512d740e9.png)

--------------------------
[Setting]

[초기 install]
   - pip3 install django-crontab
   - pip3 install 'Django<4.0'
   - pip3 install requests

[서버 실행]
   - python manage.py runserver

[접속]
   - http://127.0.0.1:8000/python_lotto_app/

[로또번호 갱신방법]
   - C:\lotto\python_lotto_app\views.py 에서 회차 수정

   - http://127.0.0.1:8000/python_lotto_app/insert
--------------------------
