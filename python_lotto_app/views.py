from .models import lottoBoard
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Q, Max
from django.http import HttpResponse
import requests
import json

# selectList
""""
class selectList(ListView):
    model = lottoBoard
    template_name = 'lotto_board/list.html'
"""""


def index(request):
    # lottoBoard_list = lottoBoard.objects.order_by('-round')[:10]
    list1 = []
    numbers = []
    counts = []
    
    total_round = lottoBoard.objects.count()
    last_round = lottoBoard.objects.aggregate(Max('round'))['round__max']
    
    for i in range(1, 46):
        count = lottoBoard.objects.filter(
            Q(number_1=i) | Q(number_2=i) | Q(number_3=i) | Q(number_4=i) | Q(number_5=i) | Q(number_6=i) | Q(number_7=i)
        ).count()
        list1.append((i,count))
    list1.sort(key = lambda element : element[1], reverse=True)
    
    for i, j in list1:
        numbers.append(i)
        counts.append(j)
        
    return render(request, 'lotto_board/index.html', {'numbers': numbers, 'counts': counts, 'total_round': total_round, 'last_round': last_round})


# 로또 api 이용해서 데이터 insert
def insertData(request):

    for n in range(917, 1060):
        params = {
            'method': 'getLottoNumber',
            'drwNo': n
        }
        # verify=False SSL 무시
        req = requests.get('https://www.dhlottery.co.kr/common.do',
                           params=params, verify=True)
        result = req.json()

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

    return redirect("python_lotto_app:index")


# 기간별 검색
def ajax(request):
    
    start_date = request.POST['start_date']
    end_date = request.POST['end_date']
    
    list1 = []
    numbers = []
    counts = []
    total_round = lottoBoard.objects.filter(date__range=(start_date, end_date)).count()
    
    for i in range(1, 46):
        count = lottoBoard.objects.filter(date__range=(start_date, end_date)).filter(
            Q(number_1=i) | Q(number_2=i) | Q(number_3=i) | Q(number_4=i) | Q(number_5=i) | Q(number_6=i) | Q(number_7=i)
        ).count()
        list1.append((i,count))
    list1.sort(key = lambda element : element[1], reverse=True)
    
    for i, j in list1:
        numbers.append(i)
        counts.append(j)

    data = {'numbers': numbers,
            'counts': counts,
            'total_round': total_round}
    return HttpResponse(json.dumps(data), content_type="application/json")


# 특정 회차 분석
def analyze(request):
    num = request.POST.get('round')
    obj = lottoBoard.objects.get(round=num)
    
    winning_numbers = []
    winning_numbers.append(int(obj.number_1))
    winning_numbers.append(int(obj.number_2))
    winning_numbers.append(int(obj.number_3))
    winning_numbers.append(int(obj.number_4))
    winning_numbers.append(int(obj.number_5))
    winning_numbers.append(int(obj.number_6))
    
    
    list1 = []
    categories = []
    data = []
    
    
    for i in range(1, 46):
        count = lottoBoard.objects.exclude(round__gte=num).filter(
            Q(number_1=i) | Q(number_2=i) | Q(number_3=i) | Q(number_4=i) | Q(number_5=i) | Q(number_6=i) | Q(number_7=i)
        ).count()
        dict1 = {}
        dict1['y'] = count
        if i in winning_numbers:
            dict1['color'] = 'black'
        else:
            pass
            # dict1['color'] = 'blue'
        
        list1.append((i, dict1))
    list1.sort(key = lambda element : element[1]['y'], reverse=True)
    
    for i, j in list1:
        categories.append(i)
        data.append(j)

    # print(categories)
    print(data)

    result = {'categories': categories, 'data': data, 'total_round': num}
    return HttpResponse(json.dumps(result), content_type="application/json")
    # return redirect("python_lotto_app:index")





def home(request):
    num = request.POST.get('numb')
    print(num)
    return render(request, 'lotto_board/home.html')