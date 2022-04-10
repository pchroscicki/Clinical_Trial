from datetime import datetime
import random
from datetime import date, timedelta
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from CT_platform.forms import AddDrugForm
from CT_platform.models import Drug


class IndexView(View):

    def get(self, request):
        return render(request, 'base.html', {'actual_date': date.today()})


class AddDrugView(LoginRequiredMixin, View):

    def get(self, request):
        form = AddDrugForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = AddDrugForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('drug_list')
        return render(request, 'form.html', {'form': form})


class DrugListView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'drug_list.html', {'drug_list': Drug.objects.all()})

