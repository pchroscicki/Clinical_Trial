from datetime import datetime
import random
from datetime import date, timedelta
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from CT_platform.forms import AddDrugForm, AddStudySchemeForm, AddPatientForm, AddVisitForm, AddAdverseEventForm
from CT_platform.models import Drug, StudyScheme, Patients, Visit, AdverseEvent


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


class AddPatientView(LoginRequiredMixin, View):

    def get(self, request):
        form = AddPatientForm()
        return render(request, 'form.html', {'form': form})


    def post(self, request):
        form = AddPatientForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.patient_author = request.user
            patient.save()
            patient_id = Patients.objects.last().id
            return redirect(reverse ('add_visit',  kwargs={"patient_id": patient_id}))
        return render(request, 'form.html', {'form': form})


class PatientListView(LoginRequiredMixin, View):

    def get(self, request):
        patients_list = Patients.objects.all()
        patients_number = len(patients_list)
        study_scheme = StudyScheme.objects.last()
        enrolment_plan = study_scheme.patient_cohort * len(Drug.objects.all())
        enrolment_percent_status = (patients_number * 100) // enrolment_plan
        text1 = 'List of patients'
        if patients_number < enrolment_plan:
            text2 = f'Number of enrolled patients: {patients_number}/{enrolment_plan} ({enrolment_percent_status}% completed)'
        else:
            text2 = f'Patients enrolment into this study is completed! Total number of enrolled patients: {patients_number}/{enrolment_plan} ({enrolment_percent_status}% completed)'
        context = {'patients_list': patients_list, 'text1': text1, 'text2': text2}
        return render(request, 'main_page.html', context)


class PatientDetailView(LoginRequiredMixin, View):
    def get(self, request, patient_id):
        patient = Patients.objects.get(id=patient_id)
        visits = Visit.objects.filter(patient=patient).order_by('date')
        adverse_events = AdverseEvent.objects.filter(patient=patient).order_by('id')
        context = {'patient': patient, 'visits': visits,
                   'adverse_events': adverse_events}
        return render(request, 'patient_detail_view.html', context)


class AddVisitView(LoginRequiredMixin, View):
    def get(self, request, patient_id):
        form = AddVisitForm()
        title1 = 'Add Visit Form'
        title2 = f'Patient ID: {patient_id}'
        return render(request, 'form.html', {'form': form, 'title1': title1, 'title2': title2})

    def post(self, request, patient_id):
        patient = Patients.objects.get(id=patient_id)
        patient_visits = len(Visit.objects.filter(patient=patient))
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
            return redirect('main_page')
        title1 = 'Add Visit Form'
        title2 = f'Patient ID: {patient_id}'
        return render(request, 'form.html', {'form': form, 'title1': title1, 'title2': title2})

class AddAdverseEventView(LoginRequiredMixin, View):

    def get(self, request, patient_id):
        patient = Patients.objects.get(id=patient_id)
        form = AddAdverseEventForm()
        title1 = 'Adverse Event Form'
        title2 = f'Patient ID: {patient.id}'
        return render(request, 'form.html', {'form': form, 'title1': title1, 'title2': title2})

    def post(self, request, patient_id):
        patient = Patients.objects.get(id=patient_id)
        form = AddAdverseEventForm(request.POST)
        if form.is_valid():
            ae = form.save(commit=False)
            ae.patient = patient
            ae.author = request.user
            ae.save()
            return redirect(reverse ('patient_details',  kwargs={"patient_id": patient_id}))
        title1 = 'Adverse Event Form'
        title2 = f'Patient ID: {patient.id}'
        return render(request, 'form.html', {'form': form, 'title1': title1, 'title2': title2})


class UpdateAdverseEventView(LoginRequiredMixin, View):

    def get(self, request, patient_id, ae_id):
        patient = Patients.objects.get(id=patient_id)
        ae_to_be_updated = AdverseEvent.objects.get(id=ae_id)
        form = AddAdverseEventForm(instance=ae_to_be_updated)
        title1 = f'Adverse Event Form: Adverse Event ID: {ae_to_be_updated.id}'
        title2 = f'Patient ID: {patient.id}'
        return render(request, 'form.html', {'form': form, 'title1': title1, 'title2': title2})

    def post(self, request, patient_id, ae_id):
        patient = Patients.objects.get(id=patient_id)
        ae_to_be_updated = AdverseEvent.objects.get(id=ae_id)
        form = AddAdverseEventForm(request.POST, instance=ae_to_be_updated)
        if form.is_valid():
            ae = form.save(commit=False)
            ae.patient = patient
            ae.author = request.user
            ae.save()
            return redirect(reverse ('patient_details',  kwargs={"patient_id": patient_id}))
        title1 = f'Adverse Event Form: Adverse Event ID: {ae_to_be_updated.id}'
        title2 = f'Patient ID: {patient.id}'
        return render(request, 'form.html', {'form': form, 'title1': title1, 'title2': title2})

