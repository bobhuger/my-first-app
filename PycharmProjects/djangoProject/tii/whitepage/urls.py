
from django.urls import path
from whitepage import views
urlpatterns = [
    path('',views.home,name='home'),
    path('pdf.html',views.pdf,name='pdf'),
]
