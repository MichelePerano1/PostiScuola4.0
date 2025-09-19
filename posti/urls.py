from django.urls import path
from . import views


urlpatterns=[
    path('',views.posti,name='posti'),
    path('login/',views.login_view, name='login_page'),
    path('logout/',views.logout_view,name='logout'),
    path('posti/',views.cambiaPosti_view, name='cambia_posti')
]