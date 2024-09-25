from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('submit_form/',views.submit_form,name="submit_form"),
]
