"""ClinicalTrial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from CT_platform import views

urlpatterns = [
    path('add_drug/', views.AddDrugView.as_view(), name='add_drug'),
    path('drug_list/', views.DrugListView.as_view(), name='drug_list'),
    path('add_study_scheme/', views.AddStudySchemeView.as_view(), name='add_study_scheme'),
    path('study_scheme_list/', views.StudySchemeListView.as_view(), name='study_scheme_list'),
    path('add_patient/', views.AddPatientView.as_view(), name='add_patient'),
    path('add_visit/<int:patient_id>/', views.AddVisitView.as_view(), name='add_visit'),
]
