from datetime import datetime
import random
from datetime import date, timedelta
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from CT_platform.forms import AddDrugForm, AddStudySchemeForm, AddPatientForm
from CT_platform.models import Drug, StudyScheme, Patients


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


class AddStudySchemeView(LoginRequiredMixin, View):

    def get(self, request):
        form = AddStudySchemeForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = AddStudySchemeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('study_scheme_list')
        return render(request, 'form.html', {'form': form})


class StudySchemeListView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'study_scheme_list.html', {'study_scheme_list': StudyScheme.objects.all()})


class AddPatientView(View):

    def get(self, request):
        form = AddPatientForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = AddPatientForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.patient_author = request.user
            patient.save()
            return redirect('index')
        return render(request, 'form.html', {'form': form})
