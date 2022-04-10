from datetime import datetime
import random
from datetime import date, timedelta
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from CT_platform.forms import AddDrugForm, AddStudySchemeForm, AddPatientForm, AddVisitForm
from CT_platform.models import Drug, StudyScheme, Patients, Visit


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


class AddVisitView(View):
    def get(self, request, patient_id):
        form = AddVisitForm()
        title1 = 'Add Visit Form'
        title2 = f'Patient ID: {patient_id}'
        return render(request, 'form.html', {'form':form, 'title1': title1, 'title2': title2})

    def post(self, request, patient_id):
        patient = Patients.objects.get(id=patient_id)
        patient_visits = len(Visit.objects.all().filter(patient=patient_id))
        form = AddVisitForm(request.POST)
        if form.is_valid():
            weight = form.cleaned_data['weight']
            ogtt = form.cleaned_data['ogtt']
            discontinuation = form.cleaned_data['discontinuation']
            related_AE = form.cleaned_data['related_adverse_event']
            author = request.user
            if patient_visits == 0:
                visit_name = 'Visit 0'
            else:
                visit_name = f'Visit {patient_visits}'
            Visit.objects.create(patient=patient, name=visit_name,
                                 weight=weight, ogtt=ogtt, discontinuation=discontinuation,
                                 related_adverse_event= related_AE, author=author)
            return redirect('index')
        title1 = 'Add Visit Form'
        title2 = f'Patient ID: {patient_id}'
        return render(request, 'form.html', {'form': form, 'title1': title1, 'title2': title2})