from django.urls import path
from .views import index, about, welcome, contact, success, sign_up, signed_up, detalle_flan, favoritos, review_flan

urlpatterns = [
    path('', index, name='index'),
    path('acerca/', about, name='about'),
    path('bienvenido/', welcome, name='welcome'),
    path('contacto/', contact, name='contact'),
    path('exito/', success, name='success'),
    path('detalle/<slug:flan_slug>', detalle_flan, name='detalle_flan'),
    path('review/<slug:flan_slug>', review_flan, name='review_flan'),
    path('accounts/favoritos', favoritos, name='favoritos'),
    path('accounts/sign_up', sign_up, name='sign_up'),
    path('accounts/signed_up', signed_up, name='signed_up'),
]