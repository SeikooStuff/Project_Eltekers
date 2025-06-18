# di web_eltekers/urls.py (jika ada)
from django.urls import path
from . import views

urlpatterns = [
    path('sasana/', views.create_sasana, name='create-sasana'),
    path('sasana/data/', views.list_sasana, name='list-sasana'),
    path('sasana/<uuid:id>/', views.detail_sasana, name='detail-sasana'),
    path('sasana/<uuid:id>/edit/', views.update_sasana, name='update-sasana'),
    path('sasana/<uuid:id>/delete/', views.delete_sasana, name='delete-sasana'),

    path('peserta/create/<uuid:sasana_id>/', views.create_peserta, name='create-peserta'),
    path('peserta/data/<uuid:sasana_id>/', views.list_peserta, name='list-peserta'),
    path('peserta/<uuid:id>/', views.detail_peserta, name='detail-peserta'),
    path('peserta/<uuid:id>/edit/', views.update_peserta, name='update-peserta'),
    path('peserta/<uuid:id>/delete/', views.delete_peserta, name='delete-peserta'),

    path('instruktur/create/<uuid:sasana_id>/', views.create_instruktur, name='create-instruktur'),
    path('instruktur/data/<uuid:sasana_id>/', views.list_instruktur, name='list-instruktur'),
    path('instruktur/<uuid:id>/', views.detail_instruktur, name='detail-instruktur'),
    path('instruktur/<uuid:id>/edit/', views.update_instruktur, name='update-instruktur'),
    path('instruktur/<uuid:id>/delete/', views.delete_instruktur, name='delete-instruktur'),

]
