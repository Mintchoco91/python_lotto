#!/usr/bin/env python
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'python_lotto.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from python_lotto_app.models import lottoBoard
import requests

from django.db.models import Max



# 디비에 저장된 마지막 회차 번호 불러오기
obj = lottoBoard.objects.aggregate(last_round=Max('round'))
n = obj['last_round'] + 1

# 이후 회차를 조회하여 디비에 저장
while True:
    params = {
            'method': 'getLottoNumber',
            'drwNo': n
    }

    # verify=False SSL 무시
    req = requests.get('https://www.dhlottery.co.kr/common.do', params=params, verify=True)
    result = req.json()

    if result['returnValue'] == 'fail':
        break

    lotto = lottoBoard(
        round=n,
        number_1=result['drwtNo1'],
        number_2=result['drwtNo2'],
        number_3=result['drwtNo3'],
        number_4=result['drwtNo4'],
        number_5=result['drwtNo5'],
        number_6=result['drwtNo6'],
        number_7=result['bnusNo'],
        date=result['drwNoDate']
    )
    lotto.save()
    n += 1

