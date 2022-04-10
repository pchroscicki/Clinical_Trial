from django.shortcuts import render
from datetime import datetime
from datetime import date
from django.views import View


# Create your views here.
class IndexView(View):

    @staticmethod
    def get(request):
        return render(request, 'base.html', {'actual_date': date.today()})
