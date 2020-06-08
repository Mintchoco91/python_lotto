from .models import lottoBoard
from django.views.generic import ListView, DetailView
from django.shortcuts import render

#selectList
""""
class selectList(ListView):
    model = lottoBoard
    template_name = 'lotto_board/list.html'
"""""

def selectList(request):
    msg = 'my message'
    lottoBoard_list = lottoBoard.objects.order_by('-round')[:5]
    return render(request, 'lotto_board/list.html', {'lottoBoard_list' : lottoBoard_list})